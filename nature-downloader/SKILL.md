---
name: nature-downloader
description: "Download academic papers from PubMed Central, arXiv, CNKI, and other sources. Batch download, format conversion, and local paper archive management."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, download, papers, pdf, literture]
    related_skills: [nature-reader, nature-citation, nature-academic-search]
    category: research
---

# Nature Downloader

Download academic papers from PubMed Central, arXiv, CNKI, and other open-access sources. Supports batch download, format conversion, and local paper archive management.

## When to Use

Use this skill when the user needs to:
- Download PDFs of academic papers from DOIs or PMIDs
- Batch download from a reference list
- Download from PubMed Central (PMC) open-access
- Download from arXiv preprints
- Download from CNKI (知网) Chinese academic papers
- Organize downloaded papers into a local archive
- Convert between formats (PDF, XML, plain text)

Trigger phrases: "下载论文", "download papers", "论文下载", "批量下载", "文献下载", "PDF下载"

## Supported Sources

| Source | Access | Identifier |
|--------|--------|------------|
| PubMed Central (PMC) | Open Access (OA) | PMC ID, PMID, DOI |
| arXiv | Open Access | arXiv ID, DOI |
| CNKI (知网) | Subscription-based | CNKI ID, DOI |
| Unpaywall | Open Access | DOI |
| DOI direct | Varies | DOI |

## Workflow

### Step 1: Collect References
Accept input as:
- List of DOIs
- List of PMIDs/PMCIDs
- List of arXiv IDs
- Reference list text (extract identifiers)
- RIS/BibTeX file (extract DOIs)
- Search results (generate list first)

### Step 2: Resolve URLs
For each reference, determine the best download URL:
- PMC: `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{id}/pdf/`
- arXiv: `https://arxiv.org/pdf/{id}.pdf`
- DOI: Resolve via `https://doi.org/{doi}` or Unpaywall API

### Step 3: Download
Download each paper:
- Set appropriate User-Agent headers
- Handle rate limiting (delay between requests)
- Handle errors (404, 403, timeout)
- Retry with alternative source
- Save with standardized naming

### Step 4: Organize Archive
Standard naming convention:
```
{YYYY}_{FirstAuthorLastname}_{ShortTitle}_{Source}.pdf
```

Organize by topic or project folder. Create a metadata index file.

### Naming Convention
```
2026_Smith_BiomaterialScaffolds_PMC.pdf
2026_Zhang_OsteogenicDifferentiation_arXiv.pdf
```

## Download Methods

### PMC Open Access
```bash
# Via FTP
curl -O "https://ftp.ncbi.nlm.nih.gov/pub/pmc/{path}.pdf"
```

### arXiv
```bash
curl -L -o paper.pdf "https://arxiv.org/pdf/{id}.pdf"
```

### DOI via Unpaywall
Use Unpaywall API to find OA version, then download.

## Anti-Patterns

1. **Copyright violation** — Only download from legal open-access sources. Respect publisher paywalls.
2. **Rate limit abuse** — Add delays between requests (≥1 second). Respect robots.txt.
3. **No metadata tracking** — Always save DOI/PMID along with the PDF. Unlabeled PDFs are research debt.
4. **Duplicate downloads** — Check local archive before downloading.
5. **Overwriting** — Never overwrite existing files. Use versioning or skip.

## Verification

- [ ] All sources are legal open-access
- [ ] Rate limiting applied
- [ ] PDFs are valid (not error pages)
- [ ] Naming convention followed
- [ ] Metadata index updated
- [ ] No duplicate downloads
