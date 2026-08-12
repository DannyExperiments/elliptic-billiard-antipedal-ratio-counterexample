# Public evidence integration contract

`N8_SUPPORTING_LINE_CERTIFICATE.zip` is the deterministic public-safe exact
certificate archive, with a detached SHA-256 sidecar. It contains the same
Lean and standard-library verifier sources integrated in this tree plus their
scope documents and pinned workflow specifications. No private candidate
archive, raw model return, source PDF, figure, screenshot, browser receipt, or
third-party source text is included.

Any future public evidence bundle may be added only after it:

1. contains solely author-controlled or clearly redistributable files;
2. states its exact relation to the canonical theorem;
3. uses repository-relative paths and contains no private identifiers;
4. includes a deterministic manifest and SHA-256 ledger;
5. is independently extracted and replayed in a clean temporary directory;
6. has a detached archive sidecar if distributed as an archive; and
7. is explicitly added to `PUBLIC_ALLOWLIST.txt`.

Archive integrity alone is not proof of the certificate or authorization to
redistribute its contents.
