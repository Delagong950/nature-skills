---
name: nature-reviewer
description: "Simulate a Nature-style peer review from the referee perspective. Generate 3 independent reviewer reports plus cross-review synthesis for pre-submission self-assessment."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, peer-review, reviewer, nature, manuscript-evaluation]
    related_skills: [nature-response, nature-writing, academic-research-suite]
    category: research
---

# Nature Reviewer Assessment

Simulate a **Nature-style reviewer assessment** package from the referee perspective. Use for pre-submission review, mock peer review, or submission readiness evaluation.

## When to Use

Use this skill when the user wants:
- Pre-submission review of a manuscript
- Reviewer-style manuscript evaluation
- Novelty/significance/technical soundness assessment
- 审稿人视角评估, 预审稿意见, 模拟审稿
- Identifying weaknesses before submission

**Do NOT use** for drafting author rebuttals (use `nature-response` instead).

## Default Stance

- Ground the review only in the manuscript facts supplied by the user
- Evaluate against: `originality`, `scientific importance`, `interdisciplinary readership`, `technical soundness`, `readability for nonspecialists`
- Return **3 reviewer reports + 1 cross-review synthesis** unless the user explicitly asks for another format
- The three reviewers may differ only in **emphasis**; do NOT invent reviewer identities, specialties, institutions, or biographies
- Distinguish clearly between: what is **supported**, what is **weak**, and what is **not assessable** from provided material
- Do NOT claim the editor's final decision or certainty about fit to a specific journal

## Accepted Inputs

- Full manuscript draft
- Abstract, summary paragraph, or cover-summary text
- Introduction, Results, Discussion, or Methods excerpts
- Figure legends, selected figures, or result notes
- Author notes in Chinese or English describing the claimed contribution
- Pre-submission positioning notes

If the provided material is partial, perform a bounded review and mark the assessment boundary explicitly.

## Workflow

### Step 1: Extract Manuscript Facts
Identify:
- Main claim / central finding
- Evidence provided (figures, data, analysis)
- Claimed significance and novelty
- Likely readership
- Visible limitations and gaps
- Missing materials affecting confidence

### Step 2: Evaluate Against Axes
Each axis is scored individually:

| Axis | What to Assess |
|------|----------------|
| **Originality** | Is the finding/concept new? How does it differ from prior work? |
| **Scientific importance** | Does it advance the field? Would the result change current thinking? |
| **Interdisciplinary readership** | Would researchers outside the subfield care? |
| **Technical soundness** | Are the methods appropriate? Controls adequate? Statistics correct? |
| **Readability** | Can a non-specialist follow the logic? Is jargon defined? |

### Step 3: Generate 3 Reviewer Reports

**Reviewer 1** — Emphasis on technical soundness and methodology
- Evaluates experimental design, controls, statistics, reproducibility
- Identifies specific technical failings
- Suggests additional controls or analyses

**Reviewer 2** — Emphasis on significance and novelty
- Assesses contribution relative to existing literature
- Evaluates whether the claims match the evidence
- Considers broader impact

**Reviewer 3** — Emphasis on writing and completeness
- Assesses clarity, organization, readability
- Checks for missing details, unclear figures, incomplete methods
- Evaluates accessibility to non-specialists

Each report includes:
- Overall assessment
- Who would be interested, and why
- Major strengths
- Major concerns (specific, actionable)
- Technical failings that need to be addressed
- Assessment against criteria
- Recommendation posture

### Step 4: Cross-Review Synthesis
- Consensus strengths
- Consensus technical risks
- Where emphasis differs across reviewers
- Broad-interest / significance readout
- Most important issues to resolve before submission

## Output Format

```
Review setup
- Input scope:
- Assessment boundary:
- Shared manuscript claim summary:
- Visible evidence base:
- Missing materials affecting confidence:

Reviewer 1
- Overall assessment:
- Who would be interested, and why:
- Major strengths:
- Major concerns:
- Technical failings:
- Recommendation posture:

Reviewer 2
[Same structure]

Reviewer 3
[Same structure]

Cross-review synthesis
- Consensus strengths:
- Consensus technical risks:
- Where emphasis differs:
- Most important issues to resolve:

Risk / unsupported claims
- [specific items]
```

## Red Lines

1. Do NOT invent reviewer identities, specialty roles, or selection history
2. Do NOT invent experiments, validations, controls, citations, figure details, or line numbers
3. Do NOT turn reviewer assessment into author rebuttal drafting
4. Do NOT present the review as an editorial decision letter
5. Do NOT state that a manuscript "belongs in Nature" as a settled fact
6. Do NOT omit technical failings when the evidence does not establish the author's case
7. Do NOT be vague — every concern must cite specific passages and suggest concrete fixes

## Verification

- [ ] Input scope clearly stated
- [ ] Assessment boundary marked when material is partial
- [ ] 3 distinct reviewer reports with different emphasis
- [ ] No invented reviewer identities
- [ ] Every concern cites specific manuscript content
- [ ] No fabricated evidence or citations
- [ ] Cross-review synthesis captures consensus and divergence
- [ ] Not presented as an editorial decision
- [ ] Readable, actionable, professional tone
