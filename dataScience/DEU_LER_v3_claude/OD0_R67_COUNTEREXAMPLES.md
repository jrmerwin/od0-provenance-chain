# OD0-R67 Counterexamples and corrections (append-only)

## CX-R67-1: in-round A1 assembly errors caught by the exactness
## discipline
The first in-round CGLMP assembly carried two index errors (a
plus-term at the wrong outcome difference; one enumeration
condition). The exact machinery itself exposed them BEFORE any
comparison: the deterministic local bound computed as 3 (impossible
for the standard form, whose bound is 2) and the value was
non-stationary. Corrected, the in-round computation gives
I_3 = 4/3 + (8/9) sqrt(3) exactly, and an independent worker
confirmed the identical value under the textbook phase gauge
((0, 1/2; 1/4, -1/4) with the CGLMP sign convention). Recorded as
a working note: the local bound is an effective checksum.

## CX-R67-2: precision of the frozen A2 phrasing
BELL1's 'S_infinity = the root of 16c^5 - 16c^3 + 2c^2 + 2c - 1'
is precisified: the quintic is the optimum's STATIONARITY
polynomial in c = cos(2 pi phi/3) (dS/dc = -(96/27) x quintic;
relevant root c* = 0.8889129786801, from the irreducible quartic
factor 8c^4 - 4c^3 - 6c^2 + 4c - 1); S itself satisfies the
irreducible quartic 531441 S^4 - 1574640 S^3 + 624024 S^2 -
25920 S - 115568 = 0 (531441 = 27^4), unique real root > 2. The
numeric value agrees to all frozen digits; no verdict affected.
