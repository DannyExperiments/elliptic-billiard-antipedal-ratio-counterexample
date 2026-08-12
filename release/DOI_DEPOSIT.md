# DOI deposit plan

No DOI exists. The human owner authorized a deposit after the immutable
GitHub `v1.0.0` release and exact public-asset verification pass.

After an immutable GitHub `v1.0.0` release is published and anonymously
re-downloaded, the deposit lane must:

1. search Zenodo, DataCite, Crossref, DOI.org, and the authenticated deposit
   dashboard for duplicate title, repository, version, or draft records;
2. use the actual GitHub publication date and exact Version 1.0.0 bytes;
3. upload only the six immutable release assets and verify each SHA-256;
4. record `DannyExperiments` as an organizational creator with no affiliation;
5. use software type, version `1.0.0`, public access, and the all-rights-reserved
   rights statement, without inventing an open-source license;
6. link the exact GitHub release as the identical/supplementary public object;
7. compare the final metadata byte-for-byte with the approved release fields;
   and
8. after publication, verify version and concept DOI resolution, DataCite
   findability, exact file inventory, anonymous downloads, and byte parity.

Only after those checks may current-main `CITATION.cff` and the README receive
version/concept DOI metadata through a protected metadata-only pull request.
