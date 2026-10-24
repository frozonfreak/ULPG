# Contributing to ULPG

Small corrections, practical examples, counterexamples, translations, and well-supported changes are welcome. Read the [guide](docs/guide.md) and [Code of Conduct](CODE_OF_CONDUCT.md) first.

## Propose a change

1. Open an issue describing the visitor problem, affected guide section, and evidence. Small wording or link fixes may go straight to a pull request.
2. Fork the repository and make a focused branch. Keep the canonical guide, affected workflows, templates, and examples consistent.
3. Explain whether a proposal changes a requirement, a recommendation, or an optional technique. Describe page types where it does and does not apply.
4. Cite primary sources for external standards, technical thresholds, or legal claims. Label hypotheses and illustrative examples clearly. Avoid presenting one jurisdiction's requirements as universal.
5. Run `python scripts/check_docs.py` and `git diff --check`. These check documentation integrity, not product quality.
6. Submit a pull request with rationale, validation performed, and unresolved limitations. Record substantive changes in [CHANGELOG.md](CHANGELOG.md).

Do not add private user data, unlicensed assets, fabricated research, vendor promotion, or credentials. AI-assisted contributions are welcome; the contributor remains responsible for accuracy, rights, and the evidence stated in the proposal.

## Editorial conventions

- Prefer plain language and concrete visitor needs.
- Keep `MUST`, `MUST NOT`, `SHOULD`, and `MAY` consistent with guide section 2.
- Reference requirements by guide version, section number, and a short quotation or description; individual bullets do not yet have stable IDs.
- Preserve necessary information and meaningful exceptions. A simple page and a detailed page can both be appropriate.
- Treat outcomes and validation methods as separate fields. Never replace “unverified” with “pass” because a check could not be run.
- Use relative links for repository files. Keep examples fictional or provide permission and provenance for real material.

## Translations

Propose translations under `translations/<language-tag>/` with a README identifying the source version, translator credit, and review status. Link to the canonical English guide and record any intentional adaptation. Do not describe an unreviewed translation as authoritative.

## License

By submitting a contribution, you agree to license your contribution under this repository's [MIT License](LICENSE), and confirm that you have the right to contribute it. No separate contributor agreement is required.
