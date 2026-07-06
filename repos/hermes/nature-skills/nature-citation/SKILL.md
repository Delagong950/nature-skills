---
name: nature-citation
description: "Add Nature/CNS journal citations to manuscript text. Split passages into citable segments, search Nature/Science/Cell portfolio journals, and export reference-manager-ready output."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, citation, references, nature, literature-search]
    related_skills: [nature-writing, nature-polishing, arxiv]
    category: research
---

# Nature Citation

Add **Nature-family / CNS (Cell-Nature-Science) journal citations** to manuscript text by splitting passages into citable segments, searching the accepted journal families, and exporting reference-manager-ready output.

## When to Use

Use this skill when the user wants to:
- Add Nature-series citations to a paragraph or manuscript
- Find CNS (Cell/Nature/Science) support for specific statements
- "分段引用" — segment text and find references for each claim
- Build a reference list with Nature/Science/Cell papers
- Export citations in RIS/EndNote/BibTeX format
- Fill missing references during paper writing

Trigger phrases: "补引用", "找引用", "找文献", "citations", "references", "Nature系列引用", "CNS", "支撑文献", "text-to-reference"

## Core Principles

1. **Strict journal scope** — Only search accepted Nature Portfolio journals, AAAS Science family, and Cell Press. Do not include other publishers unless explicitly requested.
2. **Never fabricate citations** — Every reference must be independently verifiable. AI-generated citations have ~40% error rate.
3. **Match by meaning** — Find papers that support the claim, not just papers with matching keywords.
4. **Be conservative** — Only mark a paper as "supporting" if it genuinely supports the claim. Title-level matching is insufficient; check abstracts.
5. **Export-ready** — Default to one reference-manager format (RIS/ENW/BibTeX) unless specified.

## Journal Scope

| Family | Includes |
|--------|----------|
| **Nature Portfolio** | Nature, Nature Communications, Nature Materials, Nature Methods, Nature Biotechnology, Nature Nanotechnology, Nature Chemistry, Nature Physics, Nature Medicine, Nature Genetics, etc. |
| **Science (AAAS)** | Science, Science Advances, Science Translational Medicine, Science Immunology, etc. |
| **Cell Press** | Cell, Cell Reports, Cell Metabolism, Cell Stem Cell, Molecular Cell, Developmental Cell, etc. |

User can specify: `Nature系列`, `CNS`, `CNS及子刊`, or `flagship-only`.

## Workflow

### Step 1: Segment the Text
Split the user's text into citable segments:
- Each segment = one claim or factual statement
- A segment is typically 1–3 sentences
- Label each segment: `[S1]`, `[S2]`, etc.

### Step 2: Generate Search Queries
For each segment, create specific search queries:
- Extract key concepts and entities
- Include relevant methods, materials, or model systems
- Use Boolean operators (AND, OR) for precision
- Add journal-family scope: `site:nature.com OR site:science.org OR site:cell.com`

### Step 3: Search and Verify
For each segment:
1. Search using the generated queries
2. Filter results to the accepted journal scope
3. Read abstracts/titles to verify genuine support
4. Grade each candidate:
   - `SUPPORTS` — directly supports the claim
   - `RELATED` — related but not direct support
   - `MISMATCH` — topic match but different claim

### Step 4: Assign References
- Map the best 1–3 references per segment
- Use the most specific and relevant papers
- Avoid duplicate references across segments
- Prioritize recent papers (within 5 years) unless seminal

### Step 5: Export
Default export format: RIS (compatible with EndNote, Zotero, Mendeley)

Include for each reference:
- Authors (last name, initials)
- Year
- Title
- Journal (abbreviated)
- Volume, issue, pages
- DOI

## Output Format

```
Segmented Reference Report
===========================

[S1] "Original claim text from manuscript..."
→ 1. Author A, Author B. Title. Journal Volume, Pages (Year). DOI
→ 2. Author C, et al. Title. Journal Volume, Pages (Year). DOI

[S2] "Next claim text..."
→ 3. Author D, et al. Title. Journal Volume, Pages (Year). DOI

Reference list (RIS format):
[RIS export block]
```

## Verification Guidelines

| Check | What to Verify |
|-------|----------------|
| Abstract match | Every citation's abstract genuinely supports the claim |
| Journal scope | Every source is from the accepted journal family |
| DOI | Every reference has a DOI that resolves |
| Authors | Author names match the actual publication |
| Year | Publication year is correct |
| Volume/pages | Check against publisher page |
| No fabrication | Zero invented references |

## Anti-Patterns

1. **Title-only matching** — Citing a paper because its title has the right keywords, without checking if the content supports the claim.
2. **Fabricating metadata** — Inventing volume, pages, or DOIs. Every field must be verified.
3. **Journal scope creep** — Including papers from non-CNS journals unless explicitly requested.
4. **Overcitation** — Citing more papers than needed. One strong reference per claim is better than five weak ones.
5. **Self-citation patterns** — Do not suggest the user's own papers or reviewer citations. Focus on objective literature support.
6. **Old papers for current claims** — Prefer recent literature (≤5 years) for claims about current understanding. Seminal older papers are acceptable for foundational context.

## Verification

- [ ] Text segmented into citable claims
- [ ] Journal scope confirmed with user
- [ ] Every citation verified against abstract/paper
- [ ] DOIs and metadata verified
- [ ] Export format matches user preference
- [ ] No fabricated references
- [ ] References genuinely support the attributed claim
- [ ] Output includes both inline mapping and reference list
