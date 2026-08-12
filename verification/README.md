# Exact verification

`verify_k607_stdlib.py` is an inspected, fail-closed reconstruction of the
finite `N=8` certificate using only Python's standard library. It checks exact
quotient-field arithmetic, the root bracket, conic data, common-caustic
tangency, all sixteen finite supporting-line intersections, both zero signed
areas, central inversion, and the quotient-domain failure. Its explicitly
labeled floating-point real-geometry and ray-direction checks are diagnostic,
not formal proofs.

Replay in ordinary and optimized modes:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B verification/verify_k607_stdlib.py > /tmp/replay.txt
diff -u verification/EXPECTED_K607_STDLIB.txt /tmp/replay.txt
PYTHONDONTWRITEBYTECODE=1 python3 -O -B verification/verify_k607_stdlib.py > /tmp/replay-O.txt
diff -u verification/EXPECTED_K607_STDLIB.txt /tmp/replay-O.txt
```

Both local modes pass and byte-match `REPLAY_ACTUAL.txt`; see
`REPLAY_RECEIPT.md`. This computation corroborates the proof. It cannot decide
source semantics, literature priority, peer review, or release readiness.

The legacy `src/`, `data/`, and `logs/` directories remain explanatory slots;
the canonical integrated artifacts are the four root files in this directory.
