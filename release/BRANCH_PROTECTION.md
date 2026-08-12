# Protected-main plan

The repository remains private and Draft PR #1 is the current review surface.
After the accepted candidate reaches `main`, configure and re-read the live
rule before any public transition.

The protected-main rule must require:

- changes through pull requests;
- branches to be up to date before merge;
- all four unique checks: `Verify staging integrity`, `Python standard-library
  exact replay`, `Rebuild manuscript PDF`, and `Lean finite exact
  supporting-line certificate`;
- resolution of review conversations;
- linear history;
- no force pushes or branch deletion; and
- no administrator bypass.

Required workflows must run on every pull request without path filters that
could leave checks permanently pending. Branch protection is not inferred from
workflow files; it must be verified against the live GitHub rule after it is
configured.
