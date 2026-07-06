---
name: nature-ref-verifier
description: "Multi-source cross-validation of academic references. Verify authors, title, year, volume, issue, and pages against PubMed, CrossRef, and publisher pages. Detect fabricated citations."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, citation, verification, reference-check, integrity]
    related_skills: [nature-citation, nature-academic-search]
    category: research
---

# Reference Verifier

Multi-source cross-validation of academic references. Field-by-field comparison of authors, title, year, volume, issue, pages against authoritative databases.

## When to Use

Use this skill when the user needs to:
- Verify citations in a manuscript before submission
- Detect fabricated or hallucinated references
- Audit a reference list for accuracy
- Check for citation errors (wrong volume, pages, year, authors)
- Ensure all references exist and are correctly cited
- 引用核对, 参考文献验证, 引文核查

**Essential before submission** — AI-generated citations have ~40% error rate. Every reference must be independently verified.

## Core Principle

**If you cannot verify a source exists, it cannot remain in the manuscript.** Gray zone = FAIL.

## Verification Workflow

### Step 1: Extract References
Parse the reference list. For each reference, extract:
- Authors (last name, initials)
- Year
- Title
- Journal (full or abbreviated)
- Volume
- Issue/pages
- DOI (if available)
- PMID (if available)

### Step 2: Search Multi-Source
Search each reference against:
1. **T1: CrossRef** (by DOI or title+author+year)
2. **T2: PubMed** (by PMID, author+title, or journal+volume+page)
3. **T3: Publisher page** (verify DOI resolves correctly)

### Step 3: Field-by-Field Comparison
For each field, compare the manuscript reference against the database record:

| Field | What to Check |
|-------|---------------|
| Authors | Names match? Order correct? Missing authors? |
| Year | Publication year matches? |
| Title | Exact or near-exact match? |
| Journal | Name correct? Abbreviation accurate? |
| Volume | Matches? |
| Issue/Pages | Within correct range for volume? |
| DOI | Resolves to the correct article? |

### Step 4: Grade Each Reference

| Grade | Meaning |
|-------|---------|
| **VERIFIED** | All fields match authoritative source(s) |
| **PARTIAL** | Most fields match, minor discrepancies (e.g., page range off by 1) |
| **FLAGGED** | Significant discrepancies (wrong year, wrong journal, missing volume) |
| **NOT_FOUND** | Reference cannot be found in any database |
| **FABRICATED** | Authors/DOI/title do not correspond to any real publication |

### Step 5: Generate Report

```
Reference Verification Report
==============================

Total references: 45
VERIFIED: 38 (84%)
PARTIAL: 4 (9%)
FLAGGED: 2 (4%)
NOT_FOUND: 1 (2%)
FABRICATED: 0 (0%)

Details:

[1] Author A, et al. (2020) ... → VERIFIED
  ✓ PubMed: PMID 12345678
  ✓ CrossRef: DOI 10.xxx/...
  ✓ All fields match

[2] Author B, et al. (2021) ... → FLAGGED
  ✗ Year mismatch: manuscript says 2021, database shows 2020
  ✗ Volume mismatch: manuscript says 12, database shows 15
  → Needs correction before submission

[3] Author C, et al. (2022) ... → NOT_FOUND
  ✗ No matching record in PubMed, CrossRef, or publisher sites
  → Verify with author or remove
```

## Common Citation Errors Detected

| Error Type | Example | Detection |
|------------|---------|-----------|
| Author fabrication | Names that don't match any publication | Cross-referencing |
| Year slip | Year off by 1–2 years | Year field comparison |
| Volume/page error | Wrong volume or page range | Cross-referencing |
| Journal confusion | Wrong journal for the title | Title+j comparison |
| Citation hallucination | Entirely fabricated reference | NOT_FOUND grade |
| Author order | First/last author swapped | Author list comparison |
| Missing authors | "et al." hides errors | Check full author list |

## Anti-Patterns

1. **Verifying only DOIs** — DOIs can be real even when other fields (authors, year) are wrong. Always do full field-by-field comparison.
2. **Trusting one source** — A reference found in CrossRef but not PubMed warrants further checking. Use multiple sources.
3. **Accepting "close enough"** — Minor errors (off-by-one pages) should still be flagged for author correction.
4. **No action on NOT_FOUND** — If a reference cannot be verified, it must be removed or the author must supply proof.
5. **Ignoring semantic matches** — A reference might have a different title than what's cited but be the correct paper. Check carefully.

## Verification

- [ ] Every reference checked against ≥2 sources
- [ ] Field-by-field comparison completed for each reference
- [ ] Grades assigned (VERIFIED/PARTIAL/FLAGGED/NOT_FOUND/FABRICATED)
- [ ] Report generated with actionable recommendations
- [ ] NOT_FOUND and FABRICATED references clearly marked
- [ ] All discrepancies explained for author correction
