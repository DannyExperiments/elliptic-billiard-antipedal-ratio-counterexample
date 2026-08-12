# Independent exact-verifier replay receipt

Date: 2026-08-12  
Verifier: `verify_k607_stdlib.py`  
Runtime dependency: Python standard library only  
Network/install: none

The inspected verifier was executed in ordinary and optimized modes:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B verification/verify_k607_stdlib.py
PYTHONDONTWRITEBYTECODE=1 python3 -O -B verification/verify_k607_stdlib.py
```

Both executions exited successfully and produced output byte-identical to
`verification/EXPECTED_K607_STDLIB.txt` and
`verification/REPLAY_ACTUAL.txt`:

```text
8db0d193ef6820c9ae10dcd4ecb4004d3091522f67ee716ad4da3f7b17c9c64a
```

The verifier uses explicit fail-closed `require` checks and contains no Python
`assert`, dynamic execution, subprocess, dependency-fetching, or network path.

The output's ray diagnostic is deliberately a failure result: the exact
certificate concerns complete supporting lines, while four lines cannot be
oriented as single half-rays containing both adjacent intersections.  That is
a scope boundary, not a verifier failure.

This replay corroborates the finite exact witness.  It does not establish
source semantics, literature priority, peer review, or release readiness.
