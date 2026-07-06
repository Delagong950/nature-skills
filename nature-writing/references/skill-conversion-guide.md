# Converting Third-Party Skills to Hermes Format

A pattern for adapting Claude Code / Codex skills (from GitHub repos) into Hermes Agent SKILL.md files.

## Source Repo Pattern

Many popular skill repos (e.g., Yuan1z0825/nature-skills, Imbad0202/academic-research-skills) use a **multi-file architecture** designed for Claude Code:

```
skill-name/
  SKILL.md           # Router — YAML frontmatter + routing protocol
  manifest.yaml      # Declares always_load files and on_demand references
  static/
    core/            # stance.md, workflow.md, principles.md (always loaded)
    fragments/       # Backend-specific fragments (loaded conditionally)
  references/        # Deep reference material (loaded on demand)
  templates/         # Boilerplate templates
  scripts/           # Runnable scripts
```

## Hermes Flattening Pattern

Hermes loads a single SKILL.md. The conversion process:

### Step 1: Identify the Router SKILL.md
This is the entry point. It contains YAML frontmatter and the routing protocol.

### Step 2: Extract Always-Loaded Content
From `manifest.yaml`, find everything under `always_load`. Flatten `static/core/*.md` content into the Hermes SKILL.md body.

### Step 3: Inline On-Demand References
From `manifest.yaml`, find `on_demand` references. For each reference file that covers essential functionality (not edge-case deep dives), evaluate:

- **Core workflow** → inline directly in the SKILL.md workflow section
- **Taxonomy / reference tables** → inline as tables
- **Templates** → add as code blocks or note that they're available
- **QA checklists** → inline at the end

### Step 4: Adapt the YAML Frontmatter

Claude Code SKILL.md frontmatter:
```yaml
name: skill-name
description: "..."
version: 1.0.0
```

Hermes SKILL.md frontmatter (add metadata.hermes):
```yaml
---
name: skill-name
description: "..."
version: 1.0.0
author: Adapted from [original repo]
license: Apache-2.0
metadata:
  hermes:
    tags: [keyword1, keyword2]
    related_skills: [existing-umbrella-skill]
    category: research
---
```

### Step 5: Adapt Claude Code-Specific Instructions
Replace or remove:
- `open [file]` → inline the file content or reference that it's available
- `run script [path]` → describe what the script does; use terminal() if needed
- Claude Code-specific tool references → Hermes tool equivalents (web_search, terminal, execute_code, read_file, write_file, etc.)
- Multi-agent patterns → Hermes delegate_task patterns

### Step 6: Add Anti-Patterns and Verification
Always include:
- Anti-patterns section (common failure modes from the original skill + session experience)
- Verification checklist at the end

## Common Adaptations

| Claude Code Pattern | Hermes Equivalent |
|--------------------|--------------------|
| Read file from disk | embed content inline; use `read_file` for dynamic reads |
| Run script.py | describe intent; use `terminal()` to run |
| Multi-agent dispatch | flatten into sequential workflow; use `delegate_task` for parallelism |
| `clarify` / ask user | use Hermes `clarify` tool (same API) |
| Write output files | use Hermes `write_file` |
| Reference `static/` fragments | inline the content directly in SKILL.md |
| manifest.yaml `always_load` | all go into the Hermes SKILL.md body |
