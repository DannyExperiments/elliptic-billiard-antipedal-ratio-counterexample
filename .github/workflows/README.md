# Workflow status

Four workflows are staged without badges:

- `verify.yml` runs the repository's exact integrity verifier;
- `replay-exact-verifier.yml` runs the inspected standard-library verifier in
  ordinary and optimized modes and compares exact output; and
- `lean-finite-certificate.yml` builds and kernel-checks the partial finite
  Lean certificate, compares exact axiom output, and rejects proof escapes;
  and
- `pdf.yml` rebuilds the frozen manuscript in a clean Linux runner, rejects
  unresolved references and layout warnings, and uploads the PDF plus build
  log for independent inspection.

Their actions are pinned to immutable commits, checkout credentials are not
persisted, and token permissions are read-only. The PDF workflow is a
build-and-inspection input, not a manuscript-acceptance or release assertion.
No release or DOI workflow is active. All four workflows run on every pull
request, so each can safely be required by branch protection. Badge targets
remain unauthorized until the matching remote checks pass and the resulting
artifact is independently inspected.
