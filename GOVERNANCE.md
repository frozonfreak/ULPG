# Governance and releases

ULPG is a maintainer-led documentation project. Repository maintainers review issues and pull requests; contributors can propose changes through the same public process. This document does not claim an elected committee or external standards authority.

Requirement changes should include the problem, affected page types, evidence, alternatives, and migration implications. Maintainers should record accepted rationale and unresolved objections in the issue or pull request. Disagreement is evaluated against visitor needs and evidence, not popularity alone.

## Versioning

- **Patch:** Clarifications, references, and corrections that do not intentionally change the requirements.
- **Minor:** Additional guidance or intentional changes to the pre-1.0 baseline, with adoption implications recorded.
- **Major:** Broad restructuring or incompatible changes after a stable 1.0 baseline.

The first open-source edition is **0.3.0**, derived from the supplied proposed v0.3 document. It is a public working guide, not a certification scheme. Before 1.0, readers should review each release's change notes before updating an adopted baseline.

## Release checklist

1. Reconcile the guide, README, templates, and examples.
2. Recheck changed external claims against primary sources.
3. Run documentation checks and inspect the final diff.
4. Update version references and the changelog; record known limitations.
5. Tag the reviewed commit and publish release notes when hosting and maintainer authorization are available. Do not describe a planned tag or release as already published.
