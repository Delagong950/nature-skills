---
name: nature-paper2ppt
description: "Convert academic papers into presentation slides. Extract key messages, figures, and data into structured slide decks for conferences, group meetings, or journal clubs."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, presentation, ppt, slides, conference]
    related_skills: [nature-reader, nature-figure]
    category: research
---

# Paper to Presentation

Convert academic papers into structured presentation slides for conferences, group meetings, journal clubs, or thesis defenses.

## When to Use

Use this skill when the user needs to:
- Create a conference presentation from a paper
- Prepare a group meeting/journal club presentation
- Convert thesis/dissertation chapters into defense slides
- Generate a talk outline from research results
- Create slides presenting others' work (literature review)
- 论文转PPT, 文献汇报, 组会PPT, 学术汇报, 会议报告

## Core Principles

1. **One slide = one message** — Each slide should communicate exactly one main idea.
2. **Visual > Text** — Use figures, diagrams, and data visualizations. Minimize text blocks.
3. **Audience-aware** — Conference talks need broader context; group meetings can be more technical.
4. **Story arc** — Every presentation has a narrative: problem → approach → results → implications.
5. **Never fabricate** — Use only data and figures from the source paper.

## Presentation Structure

### Standard Conference Talk (12–15 min)

| Slide | Content | Time |
|-------|---------|------|
| 1 | Title slide: title, authors, affiliation | 30s |
| 2 | Background / Motivation | 1 min |
| 3 | Gap / Problem statement | 30s |
| 4 | Approach / Study design | 1 min |
| 5–8 | Results (2–4 slides) | 5–7 min |
| 9 | Summary / Conclusion | 1 min |
| 10 | Future directions / Outlook | 30s |
| 11 | Acknowledgments / Thank you | 15s |
| * | Backup slides (as needed) | — |

### Journal Club / Group Meeting

| Slide | Content |
|-------|---------|
| 1 | Title & background |
| 2 | Why this paper matters |
| 3 | Key question / hypothesis |
| 4–6 | Results (3 slides max) |
| 7 | Strengths of the study |
| 8 | Limitations & caveats |
| 9 | Relevance to our work |
| 10 | Discussion questions |

### Thesis Defense (45–60 min)

| Section | Slides | Content |
|---------|--------|---------|
| Introduction | 3–5 | Background, gap, hypothesis |
| Methods | 2–4 | Approach overview |
| Results | 8–12 | Key findings organized by aim |
| Discussion | 3–5 | Interpretation, limitations |
| Conclusions | 1–2 | Summary, significance |
| Future | 1–2 | Next steps |

## Slide Design Guidelines

### Text
- Maximum 6–8 lines of text per slide
- Font size: title 28–32pt, body 20–24pt
- Use bullet points, not paragraphs
- Consistent formatting throughout

### Figures
- One key figure per slide; spread multi-panel across slides
- Label all axes, include legends
- Highlight the takeaway message on the figure
- Use arrows or annotations to direct attention

### Layout
- 70% figure, 30% text (ideal for results slides)
- Title at top, content below
- Consistent placement of logos, page numbers

## Workflow

### Phase 1: Extract Key Content
From the paper, identify:
- Central finding / main message
- 3–5 key results that support the main message
- Most compelling figures (1–2 hero figures)
- Context needed for the audience
- Limitations and future directions

### Phase 2: Structure the Story
1. Define the narrative arc
2. Select slides that advance the story
3. Remove details that don't support the narrative
4. Create logical transitions between slides

### Phase 3: Build Slides
For each slide:
1. Write a clear title (not "Results" but "BAM scaffolds support osteogenic differentiation")
2. Add supporting text (bullet points, not paragraphs)
3. Insert relevant figure or data
4. Add annotations to highlight key points

### Phase 4: Review
- Can someone follow the story without reading the paper?
- Is every slide necessary?
- Are figures readable at a distance?
- Is the take-home message clear?

## Anti-Patterns

1. **Text overload** — Slides full of text are handouts, not presentations. Your audience should listen, not read.
2. **No story** — Presenting results in chronological order without a narrative arc.
3. **Too many figures** — One clear figure per slide. Grouping 4+ figures on one slide overwhelms the audience.
4. **Reading from slides** — Slides support the talk; they are not the talk.
5. **Jargon without context** — Not all audience members are experts in the specific subfield.
6. **Inconsistent formatting** — Mixing font sizes, colors, and layouts across slides.

## Verification

- [ ] One main message per slide
- [ ] Clear narrative arc (problem → approach → results → conclusion)
- [ ] Figures are readable at presentation distance
- [ ] Text minimized (6–8 lines max per slide)
- [ ] All content traceable to source paper
- [ ] Audience-appropriate level of detail
- [ ] Slide count matches time allocation
- [ ] No fabricated data or figures
