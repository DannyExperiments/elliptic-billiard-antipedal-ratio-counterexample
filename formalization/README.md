# Formalization status

The inspected dependency-free Lean 4 certificate is integrated under
`lean/`. It kernel-checks a partial finite algebraic certificate for the exact
`N=8` supporting-line data; it does not formalize the complete real-geometric
counterexample theorem. Its scope and missing bridges are fixed in
`THEOREM_SCOPE.md` and `lean/SCOPE_BOUNDARY.md`.

The project pins Lean 4.30.0 and has zero external Lake packages. Local build,
`leanchecker`, exact axiom-output comparison, and proof-escape scanning pass.
Every exported theorem reports only `propext`, `Classical.choice`, and
`Quot.sound`.

No Aristotle-generated artifact is claimed. The `aristotle/` directory is a
reserved receipt-and-review slot, not evidence of a run.
