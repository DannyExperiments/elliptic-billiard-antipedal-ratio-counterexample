# Workflow and badge activation

The fail-closed integrity/release workflow, bounded exact-replay workflow,
partial-Lean workflow, and clean PDF-build workflow are staged. The latter
three validate or build exact artifacts but do not authorize public release;
the release workflow remains expected to block while release gates are open.

Do not add a passing mathematical, replay, PDF, Lean, release, or DOI badge
until the exact corresponding artifact exists on the public branch and its
gate has been independently rechecked. Badge target, displayed state, and
public evidence must agree.

Future workflow additions require source review, immutable action pins, least
privilege, no dependency fetching unless separately approved, and successful
local dry runs before activation.
