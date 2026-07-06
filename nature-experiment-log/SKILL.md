---
name: nature-experiment-log
description: "Standardized lab notebook with structured YAML-frontmatter experiment logs. Supports Obsidian vault integration, image/voice/text input, and batch/tracking systems."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, lab-notebook, experiment, obsidian, tracking]
    related_skills: [nature-data, nature-literature-pipeline]
    category: research
---

# Experiment Log

Standardized laboratory notebook system with structured YAML-frontmatter experiment logs. Supports Obsidian vault integration, image/voice/text input, batch tracking, and experiment ID systems.

## When to Use

Use this skill to:
- Create structured experiment logs
- Track experiments with consistent metadata
- Integrate with Obsidian for lab notebook management
- Process raw materials (images, voice notes, text) into structured logs
- Manage experiment batches and sample tracking

Trigger phrases: "实验记录", "lab notebook", "experiment log", "实验日志", "batch tracking", "实验追踪"

## Core Structure

### Experiment Log Format (YAML frontmatter + Markdown)

```yaml
---
experiment_id: "EXP-2026-001"
date: 2026-07-06
title: "Effect of succinate concentration on scaffold porosity"
project: "BAM scaffolds for bone tissue engineering"
researcher: "[Name]"

batch_id: "BATCH-2026-07-A"
samples:
  - id: "S001"
    condition: "5% succinate"
    replicates: 3
  - id: "S002"
    condition: "10% succinate"
    replicates: 3

materials:
  - "Polycaprolactone (PCL, MW 80,000)"
  - "Succinic acid (Sigma, ≥99%)"
  - "Chloroform (anhydrous)"

equipment:
  - "Scanning electron microscope (SEM, JEOL JSM-IT800)"
  - "Universal testing machine (Instron 5944)"

status: completed
tags: [scaffold, porosity, succinate, bam]
---
```

### Body sections
```
## Objective
Brief statement of the experimental goal.

## Protocol
Step-by-step procedure with enough detail for reproducibility.

## Results
Key observations, measurements, and initial findings.

## Analysis
Data analysis performed, statistical tests, figures.

## Conclusions
What was learned, decisions for next steps.

## Next Steps
Follow-up experiments or adjustments.
```

## Batch Tracking

When experiments involve multiple samples or conditions, track with a batch system:

### Batch Record
```yaml
---
batch_id: "BATCH-2026-07-A"
date: 2026-07-06
project: "BAM scaffold optimization"
total_samples: 18
conditions:
  - name: "Control (PCL only)"
    n: 3
  - name: "5% succinate"
    n: 3
  - name: "10% succinate"
    n: 3
  - name: "15% succinate"
    n: 3
  - name: "20% succinate"
    n: 3
  - name: "25% succinate"
    n: 3
status: completed
---
```

## Obsidian Integration

When using Obsidian for lab notebook:
- Place logs in `{vault}/Experiments/` folder
- Use Dataview plugin for querying
- Create index files by project or month
- Link experiments to literature notes
- Tag by technique, material, status

### Index File Example
```markdown
# Experiment Index: BAM Scaffolds
```dataview
TABLE date, status, batch_id
FROM "Experiments"
WHERE contains(tags, "bam")
SORT date DESC
```

## Workflow

### Input Types
1. **Text** — Describe the experiment; the skill structures it into the standard format
2. **Voice notes** — Transcribe and structure
3. **Images** — Extract contextual information and structure around them

### Steps
1. Identify experiment type and scope
2. Generate experiment ID following convention
3. Build YAML frontmatter from provided information
4. Draft body sections
5. Assign batch/sample IDs for multi-sample experiments
6. Create index entries if using Obsidian

## Anti-Patterns

1. **Inconsistent IDs** — Use a consistent experiment ID convention throughout the project.
2. **Missing metadata** — Always include date, materials, equipment, and conditions.
3. **Results without analysis** — Log raw observations AND initial interpretation.
4. **No next steps** — Every log should conclude with what comes next.
5. **Overwriting** — Never delete old logs. Version or append.

## Verification

- [ ] Experiment ID follows convention
- [ ] YAML frontmatter complete (date, title, project, status, tags)
- [ ] Protocol detailed enough for reproducibility
- [ ] Materials and equipment listed
- [ ] Results separated from interpretation
- [ ] Next steps documented
- [ ] Batch/sample tracking applied when relevant
