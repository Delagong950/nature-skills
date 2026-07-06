---
name: nature-paper-to-patent
description: "Convert academic research papers into patent applications. Draft patent abstracts, claims, descriptions, and identify patentable subject matter from research findings."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, patent, ip, invention, technology-transfer]
    related_skills: [nature-writing]
    category: research
---

# Paper to Patent

Convert academic research findings into patent application drafts. Identify patentable subject matter, draft claims, and structure patent descriptions.

## When to Use

Use this skill when the user wants to:
- Identify patentable inventions from research results
- Draft a provisional patent application
- Write patent claims from experimental data
- Structure a patent description/ specification
- Assess novelty and inventiveness of research findings
- Bridge from academic publication to IP protection

Trigger phrases: "专利", "patent", "发明", "专利申请", "知识产权", "IP", "技术转化", "专利撰写"

## Core Principles

1. **Patent is not a paper** — Different audience, different goals. Patents protect inventions; papers communicate discoveries.
2. **Enablement** — The patent must enable a person skilled in the art to make and use the invention without undue experimentation.
3. **Best mode** — Disclose the best way to practice the invention known at the time of filing.
4. **Novelty and non-obviousness** — Focus on what is new and not obvious to someone skilled in the art.
5. **Never fabricate** — Do not invent experimental results, embodiments, or working examples. All claims must be supported by the specification.

## Structure of a Patent Application

### Title
Short, specific, descriptive of the invention.

### Abstract
Brief technical summary (150 words max). Not used for claim interpretation but for prior art searching.

### Field of the Invention
The technical field to which the invention pertains.

### Background
- Problem in the prior art
- Limitations of existing solutions
- No need to cite specific references (unlike academic papers)

### Summary of the Invention
- Broad description of the invention
- Technical problem → solution → advantages
- Corresponds roughly to the Abstract and Introduction of a paper

### Brief Description of the Drawings
List of figures with short descriptions.

### Detailed Description
- Enablement section: how to make and use the invention
- Working examples (from experimental data)
- Alternative embodiments
- Best mode disclosure

### Claims
- Define the legal scope of protection
- **Independent claims**: broadest scope
- **Dependent claims**: narrow, specific limitations
- Each claim is a single sentence

## Paper-to-Patent Mapping

| Paper Section | Patent Section |
|--------------|---------------|
| Title | Title |
| Abstract | Abstract |
| Introduction | Background + Field |
| Results | Detailed Description (examples) |
| Methods | Detailed Description (how to make) |
| Discussion | Summary (advantages) |
| Figures | Brief Description of Drawings |
| — | Claims (new) |

## Claim Drafting Examples

### Independent Claim (Composition)
```
1. A biocompatible scaffold composition for bone tissue engineering,
   comprising:
   a biodegradable polymer matrix; and
   succinate groups covalently incorporated into the polymer matrix
   at a concentration of 5% to 25% by weight,
   wherein the scaffold has a porosity of 70% to 95% and
   compressive modulus of 0.5 to 5 MPa.
```

### Dependent Claim
```
2. The scaffold of claim 1, wherein the biodegradable polymer matrix
   comprises polycaprolactone (PCL).
```

## Workflow

### Phase 1: Invention Disclosure
1. Identify the core invention from research findings
2. Document: problem solved, solution, key experimental results
3. Assess novelty over prior art
4. Determine patent category (composition, method, device, use)

### Phase 2: Prior Art Search
- Search existing patents and published applications
- Search academic literature (using nature-academic-search or nature-citation)
- Identify what distinguishes the invention from prior art

### Phase 3: Draft Specification
1. Write Background section
2. Draft Summary of the Invention
3. Write Detailed Description with working examples
4. Prepare figures
5. Draft Abstract

### Phase 4: Draft Claims
1. Write broad independent claims
2. Add dependent claims with narrowing limitations
3. Ensure claims are supported by the specification
4. Check: every claim element appears in the detailed description

## Claim Types

| Type | Protects | Example |
|------|----------|---------|
| Composition | Material, compound, formulation | "A scaffold comprising..." |
| Method of making | Process, synthesis, fabrication | "A method of preparing..." |
| Method of using | Application, treatment method | "A method of treating..." |
| Article/device | Physical product | "An implantable device..." |

## Anti-Patterns

1. **Paper-style writing** — Patents use different language. "We demonstrate" → "The invention provides". Avoid academic hedging ("may", "could", "potentially").
2. **Insufficient enablement** — If a person skilled in the art cannot reproduce the invention from the description, the patent is invalid.
3. **Overly narrow claims** — Claims that are too specific are easy to design around. Find the right breadth.
4. **Overclaiming** — Claiming what hasn't been demonstrated risks invalidity.
5. **No best mode** — Failing to disclose the best-known embodiment.
6. **Inventing data** — Never fabricate working examples. This is fraud on the patent office.

## Verification

- [ ] Patent category identified (composition/method/device/use)
- [ ] Novelty assessed against prior art
- [ ] Specification supports all claims
- [ ] Claims are clear, concise, and enabled
- [ ] Best mode disclosed
- [ ] No fabricated experimental results
- [ ] All drawings referenced in description
- [ ] Legal disclaimers included (this is a draft, not legal advice)
