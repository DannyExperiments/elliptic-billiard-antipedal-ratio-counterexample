# Changelog from the canonical proof

This file records manuscript-only editorial changes relative to the frozen
Candidate-B proof base. It is not a mathematical dependency ledger; the
claim-level mapping remains in `SOURCE_TO_CANONICAL_COMPARISON.md`.

## Source-audit repairs

- The 2020-10-28 experimental one-focus `N=6`, `a/b=2` precursor is named,
  cited, and excluded from the novelty-bearing `N=8` simultaneous-zero claim.
- The Garcia--Reznik 2022 bibliography entry uses the version-of-record title,
  journal, volume, pages, and DOI while retaining the distinct arXiv-preprint
  title as a note.

Both repairs passed the focused post-repair re-audit. They changed no theorem,
witness parameter, formula, or proof inference.

## Repository-template parity edit

The article follows the recent solve-repository convention used by the
project's mature public releases:

- the article itself has no author byline or affiliation;
- the article date is empty;
- PDF title, subject, keyword, and author metadata are left blank by the
  source rather than populated from private or repository identity fields;
- repository and preferred-citation authorship remain `DannyExperiments` in
  the root `CITATION.cff`; and
- AI assistance and production provenance are documented in the root
  `AI_DISCLOSURE.md` and `PROVENANCE.md`, not in the mathematical article.

The first remote authorless build exposed an `amsart` running-mark defect on
even pages: the empty article-author field yielded clipped fragments instead
of a stable header. The source now sets the same short public title mark on
both sides with `\markboth{FOCAL ANTIPEDAL AREAS}{FOCAL ANTIPEDAL AREAS}`.
This is a pagination-only repair modeled on the established authorless
solve-paper template; it changes no article text, theorem, formula, or proof.

This edit removes only presentation and attribution-surface text. The abstract,
problem statement, theorem statements, proof, formulas, references, scope,
priority qualification, verification description, and limitations are
otherwise unchanged. The fresh exact-head build, source/PDF comparison,
metadata and privacy scan, and page-by-page visual preflight subsequently
passed on all six pages. None of these editorial operations reopens the frozen
mathematical or literature adjudications.
