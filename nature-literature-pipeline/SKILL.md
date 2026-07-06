---
name: nature-literature-pipeline
description: "End-to-end literature processing pipeline: search, download, read, annotate, extract, and organize into a local knowledge base with Obsidian vault integration."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, literature-review, pipeline, obsidian, knowledge-base]
    related_skills: [nature-academic-search, nature-downloader, nature-reader, nature-citation]
    category: research
---

# Literature Pipeline

End-to-end literature processing pipeline: search → download → read → annotate → extract → organize into a local knowledge base.

## When to Use

Use this skill when the user needs a complete literature workflow:
- Systematic literature review
- Building a personal research knowledge base
- Processing a batch of new papers
- Keeping up with new publications in a field
- Integrating literature notes with Obsidian

Trigger phrases: "文献管理", "文献流水线", "literature pipeline", "文献综述", "systematic review", "文献整理"

## Pipeline Stages

### Stage 1: Search
- Define search strategy (keywords, databases, date range)
- Execute multi-source search (PubMed, CrossRef, arXiv)
- Deduplicate results
- Screen by title/abstract
- Output: candidate reference list

### Stage 2: Download
- For each candidate, determine best access source
- Download PDFs (legal open-access only)
- Save with standardized naming
- Track download status
- Output: local PDF archive

### Stage 3: Read
- Extract full text from PDF
- Build bilingual reader (Chinese-English)
- Extract figures and tables
- Build terminology ledger
- Output: Markdown reader file

### Stage 4: Annotate
- Key findings and contributions
- Methodology notes
- Figures/tables of interest
- Connections to other papers
- Critical evaluation
- Output: annotated literature note

### Stage 5: Extract & Organize
- Extract citations for reference management
- Tag by topic, method, material, finding
- Link to related papers (builds a citation graph)
- Integrate with Obsidian vault
- Output: structured knowledge base entries

## Literature Note Template

```markdown
---
title: "Paper Title"
authors: "Author A, Author B, ..."
year: 2026
journal: "Nature Communications"
doi: "10.1038/..."
tags: [topic, method, material]
status: read
rating: ⭐⭐⭐
---

## Summary
One-paragraph summary of the paper.

## Key Findings
1. Finding 1
2. Finding 2
3. Finding 3

## Methodology
- Technique: ...
- Model system: ...
- Key parameters: ...

## Relevance to My Research
- Direct relevance: ...
- Could inform: ...
- Contradicts/supports: ...

## Figures of Interest
- Fig 2: [description]
- Fig 4: [description]

## Connections
- Related to: [[Other Paper Note]]
- Cited by: ...
- Follow-up: ...

## Questions
- Unanswered questions from this paper
- Future directions

## Quotations
> "Key quotation with page/location reference"
```

## Knowledge Base Organization

```
{vault}/
  ├── Literature/
  │   ├── 2026_Smith_BiomaterialScaffolds.md
  │   ├── 2026_Zhang_Osteogenic.md
  │   └── ...
  ├── Topics/
  │   ├── Bone Tissue Engineering.md
  │   ├── BAM Scaffolds.md
  │   └── Succinate Polymers.md
  ├── Methods/
  │   ├── SEM Analysis.md
  │   ├── Mechanical Testing.md
  │   └── Cell Viability Assays.md
  ├── Literature Index.md
  └── Reading Queue.md
```

## Index File

```markdown
# Literature Index

## By Topic
### Bone Tissue Engineering
- [[2026_Smith_BiomaterialScaffolds]] — BAM scaffolds, porosity
- [[2026_Zhang_Osteogenic]] — Osteogenic differentiation

## Unread
- [ ] 2026_Wang_...

## By Status
- Read: 12 papers
- In Progress: 3 papers
- To Read: 8 papers
```

## Anti-Patterns

1. **Download without reading** — PDFs without notes are research debt. Read and annotate promptly.
2. **Isolated notes** — Every note should link to others. Isolated papers are forgotten papers.
3. **No relevance assessment** — Every paper needs a "why this matters" section.
4. **Citation without context** — Know why you're citing a paper, not just that it exists.
5. **Inconsistent tagging** — Use a consistent tag taxonomy across all notes.

## Verification

- [ ] Search strategy documented
- [ ] PDFs downloaded (where legally accessible)
- [ ] Reader files created for key papers
- [ ] Annotations include relevance assessment
- [ ] Tags applied consistently
- [ ] Cross-links to related papers
- [ ] Index updated
