"""Run 10c (Duet): is there room for a fourth body between R1003's 2.88-d pair and the
206.6-d Gaia orbit?

Mardling & Aarseth (2001): a hierarchical orbit is stable if
  a_out / a_in > 2.8 (1 + q_out)^(2/5) (1 + e_out)^(2/5) (1 - e_out)^(-6/5) (1 - 0.3 i/180deg).
A fourth body m4 on a P4 orbit around the 2.0 Msun pair must be stable both as the outer
body of (pair, m4) and as the inner orbit of ((pair + m4), m3) with Gaia's e3 = 0.491.
Prints the allowed P4 range for each m4, e4 and mutual inclination; an empty range means
no such fourth body can exist. Standard library only.
usage: python3 fourth_body_window.py
"""
import math

P_IN, M12 = 2.8787113, 2.0
P3, E3 = 206.587, 0.491


def ma(q, e, i_deg):
    return 2.8 * (1 + q) ** 0.4 * (1 + e) ** 0.4 * (1 - e) ** -1.2 * (1 - 0.3 * i_deg / 180)


def a_au(M, P_d):
    return (M * (P_d / 365.25) ** 2) ** (1 / 3)


def p_from_a(M, a):
    return 365.25 * math.sqrt(a ** 3 / M)


print("m3    m4    e4   i(deg)  P4 min (d)  P4 max (d)  window")
for m3 in (0.23, 0.864):
    for m4 in (0.05, 0.1, 0.3, 0.6):
        for e4 in (0.0, 0.2):
            for i in (0, 60, 90, 180):
                lo = p_from_a(M12 + m4, a_au(M12, P_IN) * ma(m4 / M12, e4, i))
                a3 = a_au(M12 + m4 + m3, P3)
                hi = p_from_a(M12 + m4, a3 / ma(m3 / (M12 + m4), E3, i))
                print(f"{m3:5.3f} {m4:4.2f} {e4:4.1f} {i:5d}  {lo:9.1f}  {hi:9.1f}   {'yes' if hi > lo else 'none'}")
