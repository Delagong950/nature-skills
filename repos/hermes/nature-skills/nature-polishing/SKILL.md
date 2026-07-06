---
name: nature-polishing
description: "Polish, restructure, or translate academic prose into Nature-style language. Covers language polishing, structural reorganization, Chinese-to-English academic translation, and readability improvement for journal submission."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, polishing, editing, translation, nature, language]
    related_skills: [nature-writing, nature-response]
    category: research
---

# Nature Polishing

Polish, restructure, or translate academic prose into **Nature-style language** for high-impact journal submission.

## When to Use

Use this skill when the user needs to:
- Polish language and grammar of a manuscript section
- Restructure paragraphs for better flow and impact
- Translate Chinese academic text to Nature-style English
- Improve readability for non-specialist audience
- Reduce word count to meet journal limits
- Check for Nature-specific style and formatting issues

Trigger phrases: "润色", "polish", "language editing", "English editing", "翻译", "translate", "rewrite", "restructure", "improve readability", "shorten", "condense"

## Core Principles

1. **Preserve scientific meaning** — Never change the factual content, data, or implications during polishing.
2. **Nature style is concise and direct** — Short paragraphs, active voice, minimal jargon, clear topic sentences.
3. **Sentence-level efficiency** — Every word carries weight. Remove redundancy without sacrificing precision.
4. **Respect author voice** — Polish to clarify, not to overwrite. Retain the author's scientific judgment.
5. **Never fabricate** — Do not add data, citations, or claims during polishing.

## Language Rules

### Conciseness
| Wordy | Concise |
|-------|---------|
| It has been demonstrated that | We show that |
| In order to | To |
| Due to the fact that | Because |
| A large number of | Many |
| At the present time | Currently |
| In the event that | If |
| It is possible that | May/might |
| On the basis of | Based on |
| With the exception of | Except |
| In the vicinity of | Near/around |

### Active vs Passive
- Use active voice for author actions: "We measured X" not "X was measured"
- Use passive voice when the actor is unknown or irrelevant: "Samples were prepared"
- Avoid mixing voices within the same paragraph

### Sentence Structure
- Keep sentences under 25–30 words where possible
- One main idea per sentence
- Use clear subject-verb-object order
- Avoid nested clauses

### Academic Tone
| Avoid | Prefer |
|-------|--------|
| Very/really/extremely | Specific quantifiers or remove |
| Importantly/notably | Let the content speak |
| Interestingly | State what is interesting and why |
| Novel/groundbreaking | Describe what is new precisely |
| Obviously/clearly | If it were clear, you would not need to say so |

## Workflow

### Phase 1: Intake
Determine:
- **Task type**: Polish (language), Restructure (organization), Translate (Chinese→English), Condense (word count)
- **Target journal**: Nature/Nature Communications/Science/etc. (affects style requirements)
- **Section**: Abstract, Introduction, Results, Discussion, Methods, cover letter
- **Language**: Current language and target language

### Phase 2: Analysis
Identify:
- Grammatical errors and typos
- Redundant phrases and wordiness
- Jargon that needs definition
- Long sentences that need splitting
- Passive voice that should be active
- Weak or hedge-heavy phrasing
- Structural issues (paragraph order, logical flow)

### Phase 3: Polish/Revise
Apply changes methodologically:
1. **Level 1 (Language)**: Grammar, spelling, punctuation, word choice
2. **Level 2 (Style)**: Conciseness, active voice, academic tone, Nature conventions
3. **Level 3 (Structure)**: Paragraph reorganization, logical flow, section transitions
4. **Level 4 (Translation)**: Chinese→English preserving meaning while adapting to English academic conventions

### Phase 4: Verification
- Changed text does not alter scientific meaning
- Word count meets target (if condensing)
- No fabricated content added
- Technical terms are accurate
- Citations unchanged
- Author's intended meaning preserved

## Translation Guidelines (Chinese → English)

When translating Chinese academic text to Nature-style English:

1. **Subject placement** — Chinese often drops subjects; English needs them. Infer from context.
2. **Long modifiers** — Chinese uses long pre-noun modifiers; English prefers post-position or separate clauses.
3. **"We" vs passive** — Chinese academic text uses passive or topic-comment; English Nature style uses "We" for author actions.
4. **Quantifiers** — Chinese "相关" = "relevant/associated" — be precise; "一定" = "a certain" → often "specific" or a concrete value.
5. **Cohesive devices** — Chinese uses fewer explicit connectors; English may need "however", "therefore", "in contrast" for flow.
6. **Academic hedging** — Chinese 可能/或许 = "may", "could", "potentially". Match the author's epistemic confidence level — do not strengthen or weaken it.

## Anti-Patterns

1. **Over-polishing** — Changing perfectly fine sentences just to change them. If it's clear and concise, leave it.
2. **Meaning drift** — Each editing pass must be checked against the original meaning.
3. **Formatting destruction** — Preserve italics, bold, special characters, equation formatting.
4. **Citation alteration** — Never change, remove, or add citations.
5. **Adding scientific content** — Polishing is about how something is said, not what is said.
6. **Jargon swap** — Replacing field-standard terms with less precise alternatives for "readability".
7. **Americanizing UK English or vice versa** — Respect the manuscript's established dialect unless the target journal specifies otherwise.

## Verification

- [ ] Task type correctly identified
- [ ] Scientific meaning preserved throughout
- [ ] No fabricated content added
- [ ] Word count within target (if condensing)
- [ ] Citations unchanged
- [ ] Author's voice retained
- [ ] Technical terminology accurate
- [ ] Nature-style conventions applied consistently
- [ ] Translation preserves epistemic confidence level
