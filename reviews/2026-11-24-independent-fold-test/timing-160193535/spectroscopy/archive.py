"""Record the actual responses and requests for the infrared and Gaia archive checks."""
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
import json
from pathlib import Path
from xml.etree import ElementTree

from astropy.io.votable import parse
import requests

HERE = Path(__file__).resolve().parent
TARGET = (257.0919764360422, 86.82191218419102)


def apogee(position):
    params = {"-source": "III/286/allvis", "-out": "RAJ2000,DEJ2000",
              "-out.max": 5}
    if position:
        params.update({"-c": "%s %s" % position, "-c.rs": 72})
    for service in ("https://vizier.idia.ac.za", "https://vizier.cds.unistra.fr", "https://vizier.nao.ac.jp",
                    "https://vizier.iucaa.in", "https://vizier.cfa.harvard.edu"):
        try:
            reply = requests.get(service + "/viz-bin/votable", params=params, timeout=(6, 30))
            reply.raise_for_status()
            root = ElementTree.fromstring(reply.content)
            info = list(root.iterfind(".//{*}INFO"))
            if any(tag.get("value") == "ERROR" or tag.get("name") == "Error" for tag in info):
                raise ValueError(f"{service} reported an archive error")
            vo = parse(BytesIO(reply.content))
            tables = list(vo.iter_tables())
            if not tables:
                # VizieR omits the entire catalogue resource on an empty cone.
                if b'VizieR' not in reply.content or b'QUERY_STATUS' not in reply.content:
                    raise ValueError("unrecognized empty response")
            rows = [[float(row[0]), float(row[1])] for tab in tables for row in tab.array]
            return dict(url=reply.url, rows=rows, tables=[tab.name for tab in tables])
        except (ValueError, ElementTree.ParseError, requests.RequestException) as exc:
            error = str(exc)
    return dict(error=error)


def sdss(position):
    url = "https://api.sdss.org/valis/query/cone"
    params = dict(ra=position[0], dec=position[1], radius=.02, units="degree", release="DR20")
    reply = requests.get(url, params=params, timeout=(8, 30))
    return dict(url=reply.url, status=reply.status_code, body=reply.text[:3200])


def gaia():
    query = ("select source_id,parallax,phot_g_mean_mag,bp_rp,has_rvs,has_xp_sampled,"
             "has_xp_continuous,teff_gspphot,logg_gspphot from gaiadr3.gaia_source "
             "where source_id=1727862804856539264")
    reply = requests.get("https://gea.esac.esa.int/tap-server/tap/sync",
                         params=dict(REQUEST="doQuery", LANG="ADQL", FORMAT="csv", QUERY=query),
                         timeout=(8, 40))
    reply.raise_for_status()
    return dict(url=reply.url, body=reply.text)


if __name__ == "__main__":
    jobs = dict(apogee_target=lambda: apogee(TARGET), apogee_sample=lambda: apogee(None),
                sdss_target=lambda: sdss(TARGET), sdss_control=lambda: sdss((315.78, -3.2)),
                gaia=gaia)
    result = {}
    with ThreadPoolExecutor() as pool:
        futures = {key: pool.submit(fn) for key, fn in jobs.items()}
        for key, future in futures.items():
            try:
                result[key] = future.result()
            except (RuntimeError, ValueError, requests.RequestException) as exc:
                result[key] = dict(error=str(exc))
    if result["apogee_sample"].get("rows"):
        result["apogee_cone_control"] = apogee(tuple(result["apogee_sample"]["rows"][0]))
    (HERE / "archive.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
