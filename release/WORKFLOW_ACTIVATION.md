# Workflow activation

The public repository runs four scoped workflows on every pull request and
push: repository integrity, exact standard-library replay, partial Lean finite
certificate, and clean PDF build. They use pinned action/toolchain identities,
read-only permissions, and no path filters.

All four passed on exact release commit
`d577ee6b199f5954dc74893834820df2656d56cb`: repository integrity run
`31617801307`, exact replay run `31617800526`, PDF run `31617800543`, and
partial Lean run `31617801245`. A protected post-DOI metadata change must pass
the same four checks before merge.

These workflows validate exact repository bytes and their declared artifacts.
They do not authorize mathematical scope expansion, establish novelty, replace
human peer review, or turn the partial Lean certificate into a formalization of
the full theorem.
