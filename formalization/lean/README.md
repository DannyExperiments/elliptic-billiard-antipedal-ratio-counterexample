# Lean finite exact certificate

This directory contains the inspected partial finite exact certificate for the
canonical `N=8` supporting-line data.

Replay locally with the pinned Lean 4.30.0 toolchain:

```sh
lake build
lake env leanchecker K607FiniteCertificate
lake env lean AxiomAudit.lean > AXIOM_REPORT.actual.txt
diff -u AXIOM_REPORT.txt AXIOM_REPORT.actual.txt
```

`lake-manifest.json` contains zero external packages. The frozen axiom output
lists only `propext`, `Classical.choice`, and `Quot.sound`. Read
`SCOPE_BOUNDARY.md` before quoting the result: this is a partial finite exact
certificate, not a full formalization of the real-geometric theorem.
