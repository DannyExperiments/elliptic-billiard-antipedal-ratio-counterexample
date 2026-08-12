# Protected-main receipt

The public repository's live `main` rule (GitHub rule ID `81661500`) was
re-read after the visibility transition. It requires:

- changes through pull requests;
- branches to be up to date before merge;
- all four unique checks: `Verify staging integrity`, `Python standard-library
  exact replay`, `Rebuild manuscript PDF`, and `Lean finite exact
  supporting-line certificate`;
- resolution of review conversations;
- linear history;
- no force pushes or branch deletion; and
- no administrator bypass.

The rule applies to public `main`. Required workflows run on every pull request
without path filters that could strand a required check. GitHub release
immutability is also enabled. Branch protection and immutability are live
repository settings, not conclusions inferred from workflow files.
