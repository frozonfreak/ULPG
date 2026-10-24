# Universal Landing Page Guide (ULPG)

**Version:** 0.3.0 — Initial open-source edition\
**Status:** Design guideline, not a certified industry standard\
**Scope:** Web landing pages, homepages, product pages and campaign entry points\
**Dependencies:** None\
**Related references:** WCAG 2.2, established design systems, and optional companion approaches Web HIG and Design Decision Method (DDM). See [references and boundaries](references.md).

> **Edition scope:** An independent, openly licensed guide for people and AI agents. Adapted from the supplied proposed v0.3 guidelines; see [provenance](../NOTICE.md) and [change history](../CHANGELOG.md). No certification, measured conversion improvement, or completed implementation testing is claimed.

## 1. Purpose

A landing page should communicate its intended message clearly, help visitors recognize whether its offering or content is relevant, provide sufficient information for an informed decision, and support a meaningful next action.

The next action need not be a purchase or registration. It may be reading, exploring, contacting, comparing, subscribing, downloading or navigating elsewhere.

A successful landing page should be:

1. **Understandable:** Its primary purpose is recognizable quickly.
2. **Relevant:** Its information reflects audience needs and context.
3. **Informative:** It provides enough information to support decisions.
4. **Credible:** Claims are accurate and evidence is appropriately presented.
5. **Navigable:** Users can find information and move without confusion.
6. **Accessible:** The experience works across abilities and input methods.
7. **Responsive:** Information and functionality adapt to devices.
8. **Performant:** It loads and responds efficiently.
9. **Visually coherent:** The presentation reinforces its purpose and brand.
10. **Measurable:** Relevant outcomes can be evaluated without inventing results.

The objective is not maximum visual appeal, minimum page length or maximum conversion at any cost.

**Guiding objective:** The simplest effective presentation that communicates the required information without compromising comprehension, accessibility, trust or usability.

## 2. Requirement levels

- **MUST:** A foundational requirement necessary for this guideline's intended quality baseline.
- **SHOULD:** A strong recommendation that may be adapted when justified by the experience.
- **MAY:** An optional technique that can improve a particular experience.

These keywords express *this guideline's* requirements. They do not imply that all requirements are mandated by WCAG, Web HIG, browsers or another external standard.

For every requirement assessed, record an **outcome** (pass, fail, not applicable, or unverified) separately from the **validation method**: **proposed**, **heuristically reviewed**, **automatically checked**, **manually tested**, or **user-research validated**. Record the scope, evidence, conditions, and limitations. A proposed change is unverified until evaluated; using one validation method does not establish outcomes outside its scope.

**MUST NOT:** Claim a test result that has not been established. An untested item is **unverified**, not passed.

## 3. Establish context before design

Before selecting layouts, typography, imagery or color, identify:

| Dimension | Required consideration |
|---|---|
| Audience | Who will visit the page? |
| Purpose | Why does the page exist? |
| Visitor intent | What brought visitors here? |
| Familiarity | What do visitors already understand? |
| Primary questions | What must they know to proceed? |
| Decision | What choice or action is expected? |
| Trust requirements | What claims require evidence? |
| Device | How and where is the page used? |
| Language | Which languages and reading conventions matter? |
| Connectivity | Are low-bandwidth or unreliable networks important? |
| Brand | Which existing visual conventions must be preserved? |
| Success | What observable outcome demonstrates effectiveness? |

- **MUST:** Identify the page's primary audience and purpose.
- **MUST:** Preserve applicable existing brand, accessibility and platform requirements unless a redesign is explicitly intended and approved; legal and accessibility obligations remain applicable.
- **SHOULD:** Identify secondary audiences and determine whether they need separate journeys.
- **MAY:** Develop personas or journey maps when multiple audiences or complex decisions justify them.

Do not assume that demographic categories alone determine visual preferences or usability needs.

## 4. Information hierarchy

### 4.1 Primary hierarchy

Organize information according to visitors' decision needs. A typical commercial page may progress through: **relevance → value → explanation → suitability → evidence → commitment**. An editorial page may instead emphasize subject, context, reading and exploration. These are information needs, not mandatory page sections.

- **MUST:** Make the primary purpose identifiable without exploration of unrelated content.
- **MUST:** Keep information necessary for a decision discoverable before that decision.
- **SHOULD:** Prioritize information by relevance and consequences rather than internal business organization.
- **SHOULD:** Use progressive disclosure for optional complexity.
- **MUST NOT:** Remove essential information solely to create whitespace or a shorter page.

### 4.2 Above the fold

The first viewport is the initially visible portion of a page; its dimensions vary by device, browser UI, zoom and settings. It **SHOULD** communicate the subject or offering, relevant audience where needed, primary value or message, and a route to the next meaningful action or content.

A commercial landing page commonly has a headline, supporting text, primary action and meaningful visual. No universal hero height, word count or image percentage applies.

- **MUST:** Make the essential proposition understandable without requiring animation, a carousel or a hidden panel.
- **SHOULD:** Make the primary next step discoverable early.
- **MUST NOT:** Compress information until readability or comprehension suffers.
- **MAY:** Let imagery continue below the initial viewport, especially on narrow screens.

### 4.3 Below the fold

Depending on the page, useful depth may include problems and benefits, capabilities, workflows, examples, pricing and terms, comparisons, evidence, FAQs, related content and contact or exploration routes.

- **SHOULD:** Arrange content in a meaningful progression, avoiding repetitive promotion.
- **MUST:** Keep essential information accessible without a required animation or scroll sequence.
- **MAY:** Provide summaries, anchor navigation, expandable details or dedicated pages.

### 4.4 Page length

No universal page-length limit applies. Choose length according to complexity, visitor familiarity, decision consequences and necessary evidence.

- **SHOULD:** Remove repetitive sections that add no understanding.
- **MUST NOT:** Require a fixed number of sections across unrelated websites.

## 5. Text and information density

### 5.1 Writing principles

Content **SHOULD** be concise, specific, understandable and appropriate to its audience. Prefer recognizable concepts and outcomes over unexplained internal terminology.

- **MUST:** Preserve important meaning while simplifying language.
- **SHOULD:** Use descriptive headings and coherent paragraphs.
- **SHOULD:** Explain unfamiliar terms when needed.
- **MUST NOT:** Replace precise explanations with vague promotional claims.
- **MAY:** Use lists, tables and illustrations when these help scanning.

### 5.2 Content density

| Context | Recommended direction |
|---|---|
| Marketing hero | Focused and immediately understandable |
| Product explanation | Moderate detail with examples |
| Pricing | Information-rich and comparable |
| Technical evaluation | Precise details and documentation links |
| Editorial content | Reading-oriented flow |
| Professional dashboard preview | Realistic density and sufficient context |

- **MUST:** Preserve necessary labels, units, prices, conditions and qualifications.
- **SHOULD:** Group related information visually and semantically.
- **MUST NOT:** Enforce universal character, word or card-count quotas.

## 6. Visual representation

Select representations by their communicative purpose:

| Purpose | Suitable representation |
|---|---|
| Establish context or emotion | Authentic photography |
| Demonstrate software | Real product screenshots |
| Explain a sequence | Diagram or interactive walkthrough |
| Compare alternatives | Table or structured comparison |
| Show a trend | Chart with readable data |
| Show physical products | Accurate product photography |
| Demonstrate interaction | Accessible video or interactive example |
| Explain a concept | Illustration if it adds understanding |
| Present exact facts | Text, lists or tables |

- **MUST:** Make essential meaning available as accessible text or equivalent content.
- **MUST NOT:** Fabricate product screenshots, testimonials, results or customer evidence.
- **SHOULD:** Prefer meaningful imagery over decorative stock images.
- **SHOULD:** Optimize image loading and reserve layout space.
- **MAY:** Include interactive demonstrations when they materially aid understanding.

A text-heavy page is not inherently inferior to a visual-heavy one.

## 7. Visual identity and color

### 7.1 Existing visual systems

- **MUST:** Respect an established design system unless changes are approved in the brief.
- **SHOULD:** Use semantic tokens for surfaces, text, actions, borders and states.
- **MUST:** Maintain applicable accessibility contrast requirements.
- **MUST NOT:** Communicate critical meaning through color alone.

### 7.2 Industry conventions

Industry conventions **MAY** inform direction, but must not prescribe it.

- **MUST NOT:** Automatically select a palette solely by industry classification.
- **SHOULD:** Consider brand recognition, cultural context, content, contrast and audience research.

### 7.3 Modernity

Modern presentation is not defined by gradients, glass effects, animation, oversized type, bento grids or minimalism.

- **SHOULD:** Favor coherent typography, intentional spacing, hierarchy and predictable interaction.
- **MAY:** Use expressive techniques where they reinforce purpose.
- **MUST NOT:** Sacrifice performance, accessibility or comprehension for fashion.

## 8. Calls to action, visitor journeys and compliance UI

### 8.1 Calls to action

A CTA is a meaningful next action, including exploring further content.

- **MUST:** Communicate what an action will do.
- **SHOULD:** Make a primary action visually distinguishable when one exists.
- **SHOULD:** Avoid unnecessary competing actions.
- **MUST:** Use understandable accessible names and appropriate link/button semantics.
- **MUST NOT:** Misrepresent cost, eligibility, availability or outcomes.
- **MUST NOT:** Use fabricated scarcity, deceptive countdowns or misleading confirmation.
- **MAY:** Offer different paths for genuinely different audiences.

### 8.2 Privacy, cookie consent and compliance UI

Consent notices, age gates, regional disclaimers and other compliance interfaces have different purposes and legal requirements. Determine the applicable jurisdictions, processing purposes and required user choices **before** selecting a pattern. This guideline is not legal advice and does not declare one jurisdiction's specific interface rules universal.

- **MUST:** Make compliance controls keyboard accessible, readable and operable with appropriate semantics.
- **MUST:** Match focus behavior to the actual interaction: a **modal dialog** restricts interaction with the underlying page and needs appropriate modal semantics and focus management; a **nonmodal notice** must not trap focus or incorrectly claim that the page is modal.
- **MUST:** Fulfill applicable consent and disclosure obligations; do not defer or hide a legally required choice merely to improve the hero's appearance.
- **MUST NOT:** Use deceptive consent patterns such as hidden choices, misleading preselected options or manipulated descriptions of consequences. Check jurisdiction-specific requirements for button presentation and choice equivalence; do not assume identical styling is a universal legal mandate.
- **MUST:** Avoid *unnecessary unexpected* layout shifts when the notice appears or closes, and satisfy the adopted CLS requirements. Reserve space or use a suitable overlay when appropriate; do not require literal zero CLS in every context.
- **SHOULD:** Keep page navigation and important context discoverable where legally permissible, without obscured keyboard focus or unreachable controls.
- **SHOULD:** Minimize data collection to what is necessary for the stated purpose and disclose the use of optional analytics and marketing technologies accurately.

## 9. Evidence, trust and credibility

Trust comes from verifiable information rather than decorative symbols. Evidence may include genuine demonstrations, customer case studies, reviews with provenance, pricing, support contacts, security details and return or cancellation terms.

- **MUST:** Represent evidence and limitations accurately.
- **MUST NOT:** Invent reviews, certifications, savings or usage statistics.
- **SHOULD:** Place relevant reassurance near the decision it affects.
- **SHOULD:** Distinguish measurements from illustrative examples.
- **SHOULD:** Review the freshness of material claims (for example, pricing, availability or supported features) as part of content maintenance.

## 10. Responsive, accessible and localized experiences

### 10.1 Accessibility and responsiveness

Landing pages **MUST** meet applicable project accessibility obligations and **SHOULD** target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/) as the baseline where no stricter requirement applies. Teams adopting Web HIG must follow its applicable normative requirements.

Core expectations include semantic headings, logical reading order, keyboard accessibility, visible focus, sufficient contrast, useful image alternatives, usable targets, responsive reflow, resizing, accessible media and reduced-motion support.

- **MUST:** Preserve essential meaning, content and actions across supported viewports.
- **MUST:** Not depend exclusively on hover or motion for essential actions.
- **SHOULD:** Test representative mobile, tablet and desktop contexts.

### 10.2 Layout elasticity and localized content

Text expansion differs by language, phrase, script, context and interface element. A single horizontal expansion percentage cannot guarantee localization quality.

- **MUST:** Preserve critical text, meaning and functionality without unintended clipping, overlap or inaccessible controls in the locales the product supports.
- **SHOULD:** Prefer content-driven sizing, flexible wrapping and resilient layout over brittle fixed-height text containers; a fixed size is permissible only if content remains accessible and its constraints are justified.
- **SHOULD:** Test translated navigation, CTA labels, cards, prices and form content across representative viewport and zoom settings.
- **SHOULD:** Verify directionality, logical properties and bidirectional behavior when right-to-left or mixed-direction languages are supported.
- **SHOULD:** Test font support, line height and character shaping for non-Latin scripts, including relevant languages such as Tamil.
- **MAY:** Use 40% text expansion as **one stress-test heuristic**, not a universal MUST threshold or proof of multilingual readiness. Define any project-specific expansion tests and failure criteria explicitly.

## 11. Motion and interaction

Motion may communicate feedback, continuity, spatial relationships or narrative.

- **MUST:** Preserve essential content and actions without animation.
- **MUST:** Respect applicable reduced-motion requirements.
- **SHOULD:** Prefer motion with an identifiable purpose.
- **MUST NOT:** Make scroll-controlled animation the only route to essential information.
- **SHOULD:** Avoid unnecessary animation on routine controls.
- **MAY:** Use expressive sequences or interactive storytelling when suitable.

## 12. Performance and technical quality

### 12.1 Core Web Vitals

A modern landing page should prioritize meaningful content availability, responsiveness and stability. Use the [Core Web Vitals good-experience reference thresholds](https://web.dev/articles/vitals) at the 75th percentile of visits, segmented by mobile and desktop:

| Metric | Good threshold |
|---|---|
| Largest Contentful Paint (LCP) | ≤ 2.5 seconds |
| Interaction to Next Paint (INP) | ≤ 200 milliseconds |
| Cumulative Layout Shift (CLS) | ≤ 0.1 |

- **MUST:** Preserve stricter targets imposed by the adopting project.
- **SHOULD:** Avoid unnecessary JavaScript, oversized imagery, blocking resources and unexpected layout shifts.
- **SHOULD:** Provide functional content before nonessential enhancement loads.
- **MUST NOT:** Claim field performance based solely on laboratory testing.

### 12.2 Third-party scripts and analytics governance

Analytics, tag managers, marketing pixels, chat widgets and other third-party code may affect user experience, security and privacy. Cumulative execution time alone does not describe third-party blocking impact; no universal **250 ms MUST** applies.

- **MUST:** Identify and document third-party scripts, their purpose, owner, necessity, data processing and performance/security implications.
- **MUST:** Respect applicable consent and data-processing requirements before loading or activating optional scripts where consent is required.
- **SHOULD:** Define **project-specific, measurable** third-party performance budgets with documented devices, network conditions, time windows, attribution method and pass/fail rules. Evaluate impact on INP, LCP, CLS and main-thread responsiveness where relevant.
- **SHOULD:** Defer noncritical scripts when doing so does not break required functionality, consent handling or justified measurement needs. `requestIdleCallback` and post-LCP loading are options, not universal prescriptions.
- **SHOULD:** Prevent third-party popups and widgets from unexpectedly shifting content, blocking essential actions or stealing focus.
- **SHOULD:** Review the third-party inventory periodically, on a cadence appropriate to project risk; quarterly is one optional operational schedule, not a universal MUST.
- **MAY:** Include a **250 ms diagnostic budget** in a project-specific experiment if the metric, measurement procedure and rationale are explicitly defined. Do not present it as a Core Web Vitals threshold or a universal total script-execution limit.

## 13. SEO and content discoverability

Where search discovery is relevant:

- **SHOULD:** Provide a descriptive title and useful metadata.
- **SHOULD:** Use appropriate semantic heading structure.
- **SHOULD:** Keep important content accessible in crawlable document content.
- **SHOULD:** Use canonical URLs and relevant structured data where warranted.
- **MUST NOT:** Add misleading structured data or unsupported claims.
- **MAY:** Develop dedicated pages for distinct topics or search intent.

Search optimization must not reduce comprehension or create repetitive content.

## 14. Page-type adaptations

Priorities change with purpose; none of these is a mandatory template.

- **SaaS / Software:** Product value, recognizable workflows, authentic interfaces, pricing clarity, onboarding and trial limitations.
- **Ecommerce:** Discovery, variations, transparent price, delivery, availability, returns and checkout routes.
- **Professional Services:** Expertise, relevant work, scope, process, credibility and contact options.
- **Portfolio / Creative:** Representative work, authorship, discovery and context; transactional CTAs are optional.
- **Editorial / Educational:** Comprehension, reading comfort, organization, evidence and exploration.
- **AI-enabled Services:** Concrete capabilities, examples, limitations, data handling, user control and truthful execution status; never imply a demo executed an action unless it did.

## 15. Validation and quality assurance

### 15.1 Before implementation

Confirm audience and purpose, hierarchy, evidence, existing design system, applicable requirements and documented trade-offs.

### 15.2 During implementation

Check semantics, responsive behavior, loading/error fallback where relevant, media optimization, focus, motion preferences, consent interface behavior, localized text and SEO metadata.

### 15.3 After implementation

Use purpose-specific evaluation:

| Evaluation | Question |
|---|---|
| First-impression comprehension | Can visitors understand the page's purpose? |
| Relevance | Can the target audience identify suitability? |
| Information discovery | Can visitors locate decision-critical details? |
| First-click testing | Can visitors identify how to proceed? |
| Trust | Are material claims supported? |
| Accessibility | Are applicable requirements met with relevant assistive technologies? |
| Performance | Does the page meet measured budgets and relevant Core Web Vitals thresholds? |
| Consent/localization | Are relevant interaction modes and supported locales functional? |
| Conversion | Does the intended journey perform as measured? |

Define business-specific conversion and comprehension thresholds rather than inventing universal figures. Record what was actually tested and untested.

## 16. Non-regression policy

When improving an existing landing page, **MUST NOT**:

- Remove critical information without an equivalent accessible alternative.
- Break existing routes or supported journeys.
- Weaken accessibility requirements, security or privacy behavior.
- Degrade performance beyond approved project budgets.
- Replace a coherent identity without authorization.
- Remove required product limitations or transaction information.
- Present proposed or experimental functionality as already available.

**SHOULD:** Compare baseline and candidate pages, preserve functionality and SEO-relevant routes, evaluate comprehension and usability, and record justified trade-offs and unresolved limitations.

## 17. Relationship to DDM and Web HIG

### 17.1 Functional boundaries

This guideline is compatible with both projects while remaining independent.

- **DDM determines:** Audience, purpose, information priorities, visual-system selection, relevant user-recognizable objects and relationships, project-specific rationale, and acceptance criteria.
- **Web HIG governs:** Applicable interface behavior, accessibility, semantic implementation, performance, motion, interaction states and its conformance contract.
- **ULPG contributes:** Communication principles, content prioritization, evidence placement, page-type adaptations and journey evaluation.

### 17.2 Contextual conflict resolution

Do **not** apply a fixed ranking that automatically places generic landing-page guidance above DDM, an established brand or an explicit project brief.

1. Identify **binding obligations** first: applicable law, security/safety constraints, accessibility obligations and supported-platform requirements. Their exact scope depends on jurisdiction and deployment; a recommendation should not be presented as statute.
2. Check the **approved project brief**, the existing design system, supported users and the consequences of error. Resolve competing nonbinding recommendations according to these circumstances.
3. Apply **DDM** to document consequential design decisions and relevant source adaptations. Apply **Web HIG** where adopted to the applicable archetype/surface and technical quality contract.
4. Apply **ULPG** as specialized landing-page guidance only where compatible with the foregoing. When guidance conflicts, choose the least complex compliant outcome that preserves comprehension, user control and necessary information.
5. **MUST:** Record unresolved conflicts and deliberate deviations, including the source requirement, proposed adaptation, rationale, testing and responsible reviewer. **MUST NOT:** Silently lower accessibility, security or explicit contractual requirements.

DDM is not a lower-priority category of business preference; it is a **decision method**. Web HIG is not automatically universal law; it is the interface standard when adopted. ULPG does not supersede either.

## 18. Design acceptance checklist

Mark each item **pass, fail, not applicable or unverified**, with evidence where available.

- [ ] Audience and purpose are clear.
- [ ] Essential information follows a meaningful hierarchy.
- [ ] The initial viewport communicates the proposition.
- [ ] Below-the-fold content adds useful information.
- [ ] Text and visuals have a purpose.
- [ ] Visual system and brand are consistent with approved requirements.
- [ ] Typography, contrast and interaction are accessible.
- [ ] Material claims are accurate and supported.
- [ ] Next actions are discoverable and understandable.
- [ ] Consent/compliance UI uses the correct modal or nonmodal pattern; applicable legal requirements, keyboard behavior and page stability are addressed.
- [ ] Primary content and actions remain usable without animation.
- [ ] Responsive layouts and supported localized content preserve meaning and functionality; no universal 40% test is required.
- [ ] Performance is evaluated against adopted Core Web Vitals and **project-defined** third-party budgets; no universal 250 ms cap is imposed.
- [ ] Third-party scripts, purposes and applicable consent dependencies are documented.
- [ ] SEO essentials are addressed where applicable.
- [ ] Relevant comprehension and usability tests have been considered/performed.
- [ ] Untested items and limitations are disclosed.
- [ ] Existing supported behavior has not regressed.

## 19. Guiding principle

**A modern landing page should reveal the right information, at the right level of detail, in the most understandable form, when visitors need it.**

It should be appropriate without decorative excess, concise without withholding necessary information, persuasive without misleading, and technically modern without sacrificing usability. Evaluate against intended users and purpose—not a universal page template.

## 20. Glossary

- **Above the fold:** The portion of a page visible before scrolling, dependent on viewport and settings.
- **Cumulative Layout Shift (CLS):** A Core Web Vitals metric of unexpected visual layout shifts over a page visit, using a defined session-window aggregation.
- **Deceptive pattern:** An interface that misleads or manipulates people into decisions they might not otherwise choose.
- **Interaction to Next Paint (INP):** A Core Web Vitals responsiveness metric based on high-latency interactions over the visit, with adjustment for pages containing many interactions; not a simple sum of every interaction delay.
- **Largest Contentful Paint (LCP):** A loading-performance metric indicating when the largest qualifying visible content element renders.
- **Modal dialog:** A dialog that makes underlying content temporarily unavailable for interaction and therefore requires suitable semantics and focus handling.
- **Nonmodal notice:** A notice that does not prevent interaction with the underlying page and should not trap focus as if modal.
- **Progressive disclosure:** Revealing advanced or secondary information when relevant while keeping essential information available.
- **Semantic tokens:** Design tokens named for their role, such as `surface-primary` or `action-danger`, instead of a raw visual value.

---

**Release status:** Initial open-source edition v0.3.0; independent implementation and user evaluations have not been run. No modifications to Web HIG, DDM, or any product repository are implied. Use the [human workflow](human-workflow.md), [agent workflow](agent-workflow.md), and [review template](../templates/review.md) to apply and evaluate this guide.
