---
name: nature-writing
description: "Draft, restructure, or plan Nature-style manuscript sections for high-impact journals. Use for writing/revising research articles, reviews, or perspectives in Nature-family format and academic tone."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, writing, nature, manuscript, journal]
    related_skills: [nature-response, nature-polishing, academic-research-suite]
    category: research
---

# Nature Writing

Draft, restructure, or plan Nature-style manuscript sections (Abstract, Introduction, Results, Discussion, Methods) for **Nature-family and other high-impact journals**.

## When to Use

Use this skill when the user needs to:
- Write or restructure a manuscript section in Nature-style format
- Plan a manuscript outline following Nature's article structure
- Convert existing text into Nature-style academic prose
- Draft specific sections (Abstract, Introduction, Results, Discussion, Methods)
- Write a Nature-style cover letter or summary paragraph

Trigger phrases: "Nature writing", "论文写作", "写abstract", "Introduction写作", "Discussion写作", "manuscript draft", "cover letter", "summary paragraph"

## Core Principles

1. **Nature articles tell a linear story** — One central message, supported by evidence, with minimal digression. Every paragraph advances the narrative.
2. **Concision** — Nature articles have strict length limits. Every sentence must earn its place.
3. **Accessible to non-specialists** — Nature has a broad readership. Define terms, avoid jargon, explain significance in context.
4. **Evidence anchored** — Every claim about results is directly supported by a figure, table, or supplementary item.
5. **Never fabricate** — Do not invent data, citations, figure references, or results.

## Nature Article Structure

### Summary Paragraph (Abstract)
- Strictly one paragraph, ~150–250 words
- Background and context (2–3 sentences)
- The gap/problem (1 sentence)
- The main result (2–3 sentences)
- Significance and broader impact (1–2 sentences)
- No citations unless essential

### Introduction
- ~2–3 paragraphs
- Broad context → specific gap → what this study does
- End with a clear statement of the contribution
- Minimal citations; only those essential for context

### Results
- Organized by scientific logic, not chronologically
- Each subsection: claim → evidence (figure) → brief interpretation
- References to figures in parentheses: (Fig. 1a, Extended Data Fig. 3)
- Do not repeat Methods detail

### Discussion
- Begin with a short restatement of the main finding
- Interpret the results in the context of the field
- Address limitations and alternative interpretations
- End with broader implications and future directions
- No repetition of Results

### Methods
- Sufficient detail for reproducibility
- Statistical information (tests, sample sizes, software)
- Data availability and code availability statements
- Ethics declarations, competing interests, author contributions

## Workflow

### Phase 1: Intake
Determine:
- **Section**: Abstract, Introduction, Results, Discussion, Methods, or full paper
- **Format**: Nature research article, review, perspective, or letter
- **Content**: Existing draft, rough notes, data only, or new from scratch
- **Length limit**: Word count or page limit (Nature typically ~3,000 words for Articles)

### Phase 2: Outline
Create a structured outline with:
- Each subsection's central claim
- Figures/tables that support each claim
- Logical flow between sections

### Phase 3: Draft
Write in Nature-style prose:
- Short paragraphs (3–5 sentences)
- Active voice where appropriate
- Clear topic sentences
- Each paragraph makes exactly one point
- No redundant phrases ("importantly", "notably", "interestingly") — the content should speak for itself

### Phase 4: Verify
Check against Nature author guidelines:
- Length within limits
- All claims supported by evidence
- All figures referenced correctly
- All citations present in reference list
- No jargon without definition
- No fabricated content

## Section Templates

### Abstract Template
```
[Broad context sentence]. [Specific background, narrowing to gap]. Here we [main finding/approach]. We show that [key result 1] and [key result 2], demonstrating [significance]. These findings reveal [broader implication] and provide [specific contribution to the field].
```

### Introduction End Template
```
Despite these advances, [specific gap or unresolved question] remains poorly understood. Here we [approach/method] to investigate [question]. We demonstrate that [main finding], establishing [contribution].
```

### Discussion Opening Template
```
Here we show that [main finding], revealing [broader insight]. This finding is consistent with [prior work] and extends it by [specific advance]. Our results suggest that [implication], with potential applications in [broader context].
```

## Style Guidelines

| Do | Don't |
|----|-------|
| Use active voice | Use passive voice where active works |
| Keep sentences under 30 words | Write long, winding sentences |
| Define acronyms on first use | Assume all readers know the jargon |
| Use precise quantitative language | Use vague qualifiers ("very", "highly") |
| Show, don't tell | Say "importantly, X is Y" |

## Anti-Patterns

> **Note**: This skill was adapted from Claude Code format. See `references/skill-conversion-guide.md` for the conversion pattern used to flatten multi-file Claude Code skills into single-file Hermes SKILL.md format.

1. **Overclaiming** — "For the first time", "groundbreaking", "revolutionary" are editorial judgments, not author claims.
2. **Citation stuffing** — More citations do not make a stronger paper. Only cite what is directly relevant.
3. **Methods in Results** — Do not describe experimental procedures in the Results section.
4. **Results in Discussion** — Do not introduce new results in the Discussion.
5. **Fabricated data or citations** — Every claim and every reference must be verifiable.
6. **Jargon without definition** — If a non-specialist would not understand it, define it.
7. **Overstating limitations** — Acknowledge limitations but don't undermine your own work.

## Verification

- [ ] Section type and format identified
- [ ] Word count within Nature guidelines
- [ ] Every claim supported by evidence
- [ ] No fabricated data, citations, or results
- [ ] Jargon defined
- [ ] Figures referenced correctly (Fig. X, Extended Data Fig. X)
- [ ] All citations in correct Nature format
- [ ] Abstract ≤250 words (for Articles)
- [ ] Tone is accessible to non-specialists
