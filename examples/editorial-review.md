# Worked example: an editorial landing page

**Fictional teaching example.** This page and its copy are invented for illustration. No live page, automated check, manual interaction test, or user study was run. Outcomes below refer only to a heuristic review of the stated fictional copy.

## Brief

- **Page:** “Neighborhood History Notes,” a collection of local-history articles.
- **Audience:** Residents and students exploring local history.
- **Purpose:** Help readers find a topic and begin reading.
- **Primary action:** Open an article; no subscription or purchase is required.
- **Baseline:** ULPG v0.3.0.
- **Available evidence:** The following copy excerpt only.

> Neighborhood History Notes\
> Discover the streets and stories around you.\
> Browse articles by neighborhood, period, or subject.\
> Button label: Continue\
> Footer claim: The city's most trusted history resource.

## Findings

| Guide section / requirement | Outcome | Validation method | Observation and evidence | Impact / next step |
| --- | --- | --- | --- | --- |
| 3, 4.1 — Audience and purpose | pass within copy scope | heuristically reviewed | Headline and supporting copy identify local-history exploration. | Validate comprehension with intended readers before drawing a research conclusion. |
| 8.1 — Communicate the action | fail within copy scope | heuristically reviewed | “Continue” does not identify the destination in this excerpt. | Replace with a destination-specific label such as “Browse articles,” if that is the actual destination. |
| 9 — Support material claims | unverified | heuristically reviewed | “Most trusted” has no evidence in the supplied excerpt; other evidence may exist. | Verify the basis or use a factual description without the unsupported ranking. |
| 14 — Page-type adaptation | not applicable to purchase journey | heuristically reviewed | The brief defines reading as the next action; no product or transaction is involved. | Do not add pricing or sales sections without a visitor need. |
| 10 — Keyboard access and responsive behavior | unverified | proposed | Copy provides no runtime or layout evidence. | Test the implementation and supported environments. |
| 12 — Field performance | unverified | proposed | No field data was supplied. | Evaluate against the adopted budget when suitable evidence exists. |

## Proposed revision

> Neighborhood History Notes\
> Discover the streets and stories around you.\
> Browse articles by neighborhood, period, or subject.\
> Link label: Browse articles\
> Footer description: Articles about local streets, buildings, and community history.

The revision removes an unsubstantiated superlative and makes the destination clearer. It is a proposal, not a tested improvement. The next review would inspect actual navigation, reading order, input behavior, responsive layout, sources, and the page's measured performance. No conversion increase or compliance claim follows from this example.
