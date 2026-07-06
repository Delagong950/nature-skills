---
name: nature-academic-search
description: "Multi-source academic literature search, citation verification, MeSH search strategy, and reference management. Search PubMed, CrossRef, arXiv, Scopus for coordinated literature workflows."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, literature-search, citation, pubmed, reference-management]
    related_skills: [nature-citation, nature-reader, arxiv]
    category: research
---

# Academic Search

Multi-source literature search, citation verification, and reference management across PubMed, CrossRef, arXiv, and other academic databases.

## When to Use

Use this skill for:
- Multi-source literature search across databases
- Citation verification (check if references exist and are accurate)
- Building MeSH search strategies for PubMed
- Reference management (BibTeX, RIS, .nbib files)
- Strict independent other-citation audits (排除自引)
- Finding who cited your paper and their profiles
- 文献检索, 查文献, 找文献, 文献综述检索, 引文核对, 他引判定

## Workflows

### Workflow 1: Multi-Source Search
Search across multiple databases with fallback chain:
1. **T1: PubMed/MEDLINE** — biomedical and life sciences
2. **T2: CrossRef** — DOI-based, broad academic coverage
3. **T3: arXiv** — preprints, CS/physics/math

For each query:
- Use Boolean operators (AND, OR, NOT)
- Apply date range filters
- Sort by relevance or date
- Deduplicate across sources

### Workflow 2: Citation Verification
Verify citations from a manuscript:
1. Check each reference exists (DOI or PubMed ID)
2. Verify author names, year, title, journal, volume, pages
3. Flag discrepancies: author fabrication, page errors, volume-year conflicts
4. Grade: `VERIFIED` / `PARTIAL` / `FLAGGED` / `NOT_FOUND`

### Workflow 3: MeSH Search Strategy
Build PubMed search strategies using MeSH terms:
1. Decompose research question into PICO components
2. Map to MeSH terms (use PubMed's MeSH database)
3. Build Boolean query with MeSH headings and subheadings
4. Apply filters (article type, language, date, species)

### Workflow 4: Citation File Management
Convert between reference formats:
- `.nbib` (PubMed) ↔ `.ris` (EndNote/Zotero) ↔ `.bib` (BibTeX/LaTeX)
- Deduplicate references
- Merge multiple files

### Workflow 5: Strict Other-Citation Audit
Determine independent citations (排除自引):
1. Identify all citation contexts
2. Exclude self-citations (any author overlap)
3. Build article-level citation metric table
4. Profile influential citers (academy members, fellows, field leaders)
5. Extract how they cited the target paper

## Search Query Guidelines

| Database | URL/Source | Strength |
|----------|-----------|----------|
| PubMed | pubmed.ncbi.nlm.nih.gov | Biomedical gold standard, MeSH terms |
| CrossRef | api.crossref.org | DOI resolution, broad coverage |
| arXiv | export.arxiv.org | Preprints, open access |
| Semantic Scholar | api.semanticscholar.org | Citation context, influence ranking |

## Output Format

```
Search Results: [Topic]
===========================
Source: PubMed (n=15) + CrossRef (n=8) + arXiv (n=3)

After dedup: 20 unique references

Top results by relevance:
1. Author A (Year). Title. Journal. DOI [SUPPORTS]
2. Author B (Year). Title. Journal. DOI [SUPPORTS]
...

Deduplication report:
- Removed 6 duplicates across sources
- 2 references from arXiv also have published versions
```

## Anti-Patterns

1. **Single-source bias** — Always search multiple databases. No single source covers all literature.
2. **Ignoring dedup** — Same paper from different sources must be merged, not double-counted.
3. **Fabricated metadata** — Never invent citation details. Mark missing data as `AUTHOR_INPUT_NEEDED`.
4. **Self-citation inflation** — In citation audits, strictly exclude all author self-citations.
5. **Outdated search strategy** — Use appropriate date ranges. 10+ year old strategies need updating.

## Verification

- [ ] Workflow correctly identified
- [ ] Multiple sources searched
- [ ] Results deduplicated
- [ ] Citations verified against source
- [ ] Self-citations excluded in audit mode
- [ ] Output formatted as requested
