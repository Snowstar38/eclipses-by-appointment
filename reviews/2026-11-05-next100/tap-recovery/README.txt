Alternative catalogue access attempt: CDS TAPVizieR API.
Official service documentation: https://tapvizier.cds.unistra.fr/ and https://tapvizier1.cds.unistra.fr/adql/about.html
Previous controls used the asu-tsv CGI route. This bounded independent route
requested TOP1 from each missing table to test transport/table availability,
not target nonmatches and not known-object positive controls. All four timed
out with20second timeouts, concurrency2. No catalogue content was obtained;
UNKNOWN remains UNKNOWN. Full ADQL, URLs, UTC times and errors are recorded
in schema-probes.json. No per-target fanout after these failures.
