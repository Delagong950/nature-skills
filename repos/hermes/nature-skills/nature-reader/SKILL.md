---
name: nature-reader
description: "Build full-paper Chinese-English side-by-side Markdown readers for journal/conference papers. Read papers from PDF, DOI, arXiv, publisher HTML, or pasted text with figure/table placement."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, reading, translation, paper-analysis, literature]
    related_skills: [nature-citation, arxiv, academic-research-suite]
    category: research
---

# Full-Paper Reader

Build bilingual (Chinese-English side-by-side), figure/table-aware, source-grounded Markdown readers for academic papers from PDF, DOI, arXiv, publisher HTML, or pasted text.

## When to Use

Use this skill when the user wants to:
- Read and translate an academic paper in detail
- Build 中英文对照/原文对照 Markdown readers
- Extract figures and tables with their captions
- Understand a paper with source-anchored analysis
- 读论文, 精读论文, 论文翻译, 文献阅读

**Do NOT** degrade to a summary-only output unless the user explicitly asks for a summary.

## Core Principles

1. **Full paper, not summary** — Produce a complete reader that preserves the full content, not a condensed version.
2. **Bilingual by default** — Chinese-English side-by-side. Translate for meaning, not word-for-word.
3. **Figure/table-aware** — Place figures and tables near their relevant prose, not all at the end.
4. **Source-grounded** — Every block is traceable to its source location. Exact anchors for every claim.
5. **Terminology consistency** — Build a terminology ledger for recurring technical terms.

## Workflow

### Step 1: Detect Source Format
Identify the input type:
- `pdf-text` — selectable-text PDF (default)
- `scanned-pdf` — image-only or OCR-required PDF
- `html` — publisher or preprint HTML page
- `doi-arxiv` — bare DOI or arXiv link (resolve first)
- `pasted-text` — pasted prose, no original layout

### Step 2: Extract Content
For each source type:
- **PDF**: Extract text, identify sections, extract figure/table references
- **HTML**: Parse structured content, extract figures with captions
- **DOI/arXiv**: Resolve to PDF or HTML first
- **Pasted text**: Use as-is, note missing layout context

### Step 3: Build Terminology Ledger
Create a recurring-term table for key technical terms:
- English term → preferred Chinese translation
- Acronym expansions
- Field-standard translations

### Step 4: Construct the Reader
Output format: Single Markdown file with:

```
# Paper Title | 论文标题
Source: DOI / arXiv / URL

## Terminology Ledger | 术语表
| English | 中文 | Notes |
|---------|------|-------|

## Abstract | 摘要
EN: [English text]
CN: [中文翻译]

## Section 1: Introduction | 引言
EN: [English text]
CN: [中文翻译]

[Figure 1: Caption]
[Figure 1: 图注]

## Section 2: Results | 结果
...
```

### Step 5: Preserve Content Integrity
- Every section from the original paper is represented
- Figures are placed near the prose that discusses them
- Tables are preserved in their original structure
- Equations are reproduced accurately
- Citations maintain their original format

## Verification

- [ ] Source format correctly detected
- [ ] Full paper preserved (no sections omitted)
- [ ] Figures placed near relevant prose
- [ ] Terminology ledger built and consistently applied
- [ ] Translation is meaning-based, not word-for-word
- [ ] All section headings preserved from original
- [ ] Equations reproduced accurately
- [ ] Citations maintained
- [ ] Source traceability documented
