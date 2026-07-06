---
name: nature-response
description: "Draft, audit, or revise Nature-style revision correspondence: point-by-point reviewer response letters, rebuttal letters, revision cover letters, and red-marked revised-manuscript excerpts. For reviewer comments, editor decision letters, 审稿意见回复, 返修回复, rebuttal."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, peer-review, nature, revision, response, rebuttal]
    related_skills: [academic-research-suite, papersprint]
    category: research
---

# Nature Reviewer Response

End-to-end pipeline for producing professional revision correspondence packages for **Nature-family journals** (Nature, Nature Communications, Nature Materials, etc.), also applicable to Science-family and other high-impact journals.

## When to Use

Use this skill when the user provides:
- An editor decision letter (pasted or uploaded)
- Reviewer comments
- Previously submitted manuscript
- Existing draft response

Trigger phrases: "审稿意见回复", "返修", "rebuttal letter", "response to reviewers", "修回信", "point-by-point response", "revised manuscript", "editor decision", "大修回复", "小修回复"

## Core Principles

1. **Never fabricate** — Do not invent experiments, citations, line numbers, figure panels, supplementary items, or manuscript changes. Mark anything the author must supply as `AUTHOR_INPUT_NEEDED`.
2. **Cooperative but not submissive** — Evidence-forward, concise, respectful. No accusations of reviewer misunderstanding.
3. **Traceability** — Every claimed revision has a manuscript location or visible placeholder. Every new figure/table/citation is named only if supplied.
4. **Professional tone** — Disagreement is evidence-based and narrow. Never lead with time, money, or convenience excuses.
5. **Readiness labels** — Always label the final output: `ready_to_submit`, `draft_with_placeholders`, `needs_author_input`, or `blocked`.

## Workflow

### Step 1: Intake and Routing

When the user provides material, first determine:
- **Task mode**: `draft` / `audit` / `revise` / `triage-only` / `cover-letter` / `revision-package` / `latex-template` / `appeal-like`
- **Decision type**: minor revision, major revision, revise-and-resubmit, transfer after review, or unclear
- **User language**: If the user writes Chinese, also produce a 中文核对 block
- **Minimum inputs**: manuscript metadata, decision type, editor instructions, reviewer reports, required files

If the user pastes a journal email, parse:
- Manuscript metadata (journal, manuscript ID, title)
- Decision type and editor instructions (IDs `E.1`, `E.2`, etc.)
- Reviewer comments (IDs `R1.1`, `R1.2`; `R2.1`, `R2.2` etc.)
- Deadlines and required files
- Build a **strategy summary** before drafting

### Step 2: Classify Each Comment

Use the following severity/type taxonomy:

| Severity | Type | Example |
|----------|------|---------|
| **BLOCKING** | Ethics/compliance | Missing IRB approval, data integrity concern |
| **CRITICAL** | Central evidence | Core claim unsupported, control missing |
| **MAJOR** | Methodology | Statistical test wrong, sample size insufficient |
| **MAJOR** | Scope | Claim overreach, missing discussion of limitations |
| **MAJOR** | Reproducibility | Code/data not available, insufficient detail |
| **MINOR** | Presentation | Figure quality, typo, unclear phrasing |
| **MINOR** | Citation | Missing citation, citation format |
| **COSMETIC** | Formatting | Reference style, section numbering |

### Step 3: Map to Action

For each classified comment, determine the response action:

| Action | Meaning |
|--------|---------|
| Revise text | Change manuscript wording at specified location |
| Add data/analysis | New experiment, supplementary analysis |
| Add citation | Insert reference |
| Clarify in response | Explain without manuscript change |
| Acknowledge limitation | Add to Discussion/Limitations |
| Decline (with reason) | Scope boundary, methodology constraint |
| Cross-reference | Link to another response |
| AUTHOR_INPUT_NEEDED | Cannot draft without author-supplied fact |

### Step 4: Draft Responses

For each reviewer comment, write a response following this structure:

1. **Acknowledge** the concern briefly and genuinely
2. **State the action taken** (revised, analyzed, clarified, etc.)
3. **Specify the manuscript location** (section, figure, line range if known)
4. **Quote revised text** in italics when pasting into the response
5. **Flag missing information** as `AUTHOR_INPUT_NEEDED` when applicable

#### Recommended patterns

```
We thank the reviewer for this constructive suggestion.
We agree that the original wording did not make this point sufficiently clear.
We have revised the manuscript to clarify...
To address this concern, we performed...
The new analysis shows...
We have therefore softened the claim from ... to ...
We now explicitly acknowledge this limitation in the Discussion.
```

#### Disagreement pattern

```
We appreciate the reviewer raising this issue. We respectfully disagree that [narrow point],
because [evidence or scope reason]. To make this clearer, we have revised [location] to state
that [revised text].
```

#### Out-of-scope pattern

```
We agree that [requested work] would provide an additional test of [claim]. However, the central
conclusion of the present study is based on [existing evidence], and [requested work] requires
[new system/design] beyond the scope of this revision. To avoid overstatement, we have revised
[location] to acknowledge this limitation.
```

### Step 5: Impossible or Difficult Cases

#### Impossible experiment

1. Acknowledge scientific value
2. Explain study-design or scope boundary
3. Offer alternative evidence if available
4. Soften the claim or add a limitation
5. Do NOT lead with time, budget, convenience, or ability excuses

#### Reviewer factual error

1. Do NOT accuse the reviewer
2. Cite the existing manuscript location
3. Clarify wording if the manuscript invited confusion
4. Consider a small revision even when the reviewer is wrong

#### Conflicting reviewer requests

1. Surface the conflict in the strategy summary
2. Prioritize explicit editor instructions
3. Find the minimal revision satisfying both concerns

#### Major statistical critique (BLOCKING until details supplied)

Request: test name, replicate unit, sample size, effect size, confidence interval, p-value, multiple-testing correction, software + version, Methods/Results locations. Do NOT invent statistical output.

#### Ethics/data-integrity critique (BLOCKING)

Request: ethics approval body + number, consent statement, animal/human-subject reporting, competing-interest correction, data/code/accession information.

### Step 6: QA Checklist

Before finalizing, verify:

- [ ] Every reviewer comment has a stable ID
- [ ] Every ID has a response or explicit unresolved flag
- [ ] No major concern answered only with thanks
- [ ] Editor-specific instructions addressed before reviewer comments
- [ ] Every claimed revision has a manuscript location or placeholder
- [ ] No invented data, p-values, sample sizes, DOIs, accession numbers
- [ ] No accusations of reviewer incompetence or misunderstanding (unless appeal with evidence)
- [ ] Disagreement is evidence-based and narrow
- [ ] Time/money/convenience not the primary stated reason for declining requested work
- [ ] Missing author inputs are concrete and flagged
- [ ] Readiness label is honest: `ready_to_submit`, `draft_with_placeholders`, `needs_author_input`, or `blocked`

### Step 7: Output Package

The final output should include:

1. **Cover letter** (optional) — Brief summary of revisions for the editor
2. **Point-by-point response** — All reviewer comments with responses
3. **Revision summary** — List of all changes made (section by section)
4. **Readiness label** — One of the four readiness states

#### LaTeX output

When requested, produce:
- Cover letter: `\documentclass{article}` with `\maketitle`
- Response letter: each reviewer starts on a new page
- Revised text: `\revised{...}` macro for red text
- Pasted excerpts in responses: `\RevisedExcerpt{...}` for italic excerpts

#### Chinese author alignment

If the user writes in Chinese, add a 中文核对 block:
- 逐条核对：审稿人意见 → 修改内容 → 修改位置 → 状态
- 大修/小修分类
- 未修改项标注原因
- 高风险项预警

## Anti-Patterns

1. **Fabricating evidence** — Never invent experiments, data, citations, or line numbers. This is the most common and most serious failure mode.
2. **Empty thanks** — "Thank you for the comment" without substantive response is unacceptable.
3. **Defensive tone** — "The reviewer misunderstood" or "The reviewer is wrong" must never appear. Treat misunderstandings as presentation signals.
4. **Vague locations** — "We have revised accordingly" without specifying WHERE is not acceptable.
5. **Leading with excuses** — Budget, time, convenience, or ability should not be the primary stated reason for declining requested work.
6. **Optimistic readiness** — Do not label a package `ready_to_submit` if any `AUTHOR_INPUT_NEEDED` or `blocked` items remain.
7. **Appeal as default** — Route appeal-like cases separately; do not draft an appeal as the default response path.

## Verification

- [ ] Task mode correctly identified
- [ ] All reviewer comments extracted and classified
- [ ] Strategy summary approved by user before drafting full responses
- [ ] Every claim is traceable to a manuscript location or explicit `AUTHOR_INPUT_NEEDED`
- [ ] Tone is professional, no accusations
- [ ] Readiness label matches actual completion state
