---
name: nature-figure
description: "Create submission-grade scientific figures for Nature/high-impact journals. Supports Python (matplotlib/seaborn) and R (ggplot2) plotting, multi-panel figure assembly, and journal-ready export."
version: 1.0.0
author: Adapted from Yuan1z0825/nature-skills (26.4k stars)
license: Apache-2.0
metadata:
  hermes:
    tags: [academic, figure, plotting, visualization, nature, schematic,科研绘图]
    related_skills: [nature-writing, nature-polishing]
    category: research
---

# Nature Figure Making

Create **submission-grade scientific figures** for Nature-family and other high-impact journals using Python (matplotlib/seaborn) or R (ggplot2).

## When to Use

Use this skill when the user wants to:
- Create scientific figures for manuscript submission
- Multi-panel figure assembly for Nature-style layouts
- Revise or polish existing figures for journal standards
- Generate data visualizations with publication-quality formatting
- Create graphical abstracts or schematic diagrams
- 科研绘图, 科研作图, 论文配图, 画图, 可视化

**Do NOT use** for: dashboards, infographics for general audiences, Illustrator/Figma-first design work.

## Core Principles

1. **Figure-first thinking** — Before generating any code, define the figure's core conclusion. The figure should answer one scientific question.
2. **Archetype-based composition** — Classify the figure by archetype (comparison, trend, distribution, composition, relationship, schematic) and design accordingly.
3. **Hero panel** — Every multi-panel figure has one "hero" panel that makes the central point. All other panels support it.
4. **Restrained palette** — Use Nature-style color schemes. Avoid rainbow colormaps. Use colorblind-friendly palettes.
5. **Journal-ready output** — Export at correct resolution (300+ DPI), format (TIFF/PDF/SVG), dimensions, and font sizes for the target journal.

## Design Guidelines

### Figure Archetypes

| Archetype | Best For | Example |
|-----------|----------|---------|
| Comparison | Control vs treatment, before vs after | Bar plots, box plots, violin plots |
| Trend | Time series, dose-response | Line plots, area plots |
| Distribution | Data spread, statistical populations | Histograms, density plots, ECDF |
| Composition | Proportions, fractions | Stacked bars, pie charts (avoid) |
| Relationship | Correlation, clustering | Scatter plots, heatmaps |
| Schematic | Mechanism, workflow, graphical abstract | Pathway diagrams, illustrations |

### Color Guidelines
- Use Nature's recommended palettes: colorblind-friendly
- 1–4 colors maximum for the hero panel
- For categorical data: Nature Color Palette (colorbrewer2.org safe set)
- For sequential data: single-hue gradient (viridis or turbo alternatives)
- For divergent data: blue-white-red or blue-white-orange
- Label colors directly rather than relying solely on legends where possible

### Typography
- Font: Arial or Helvetica (sans-serif for Nature)
- Axes labels: 8–9 pt
- Figure text (labels, keys): 7–8 pt
- Panel labels (a, b, c): 10–11 pt bold
- Consistent font sizes across panels

### Export Specs (Nature)
- Resolution: 300 DPI minimum (600 for line art)
- Format: TIFF (LZW compression) or PDF (vector)
- Width: single column (89 mm) or double column (183 mm)
- Color mode: CMYK for print, RGB for online
- Font embedding: outline all text

## Python Workflow

### Quick Start (matplotlib)
```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Nature-style rcParams
mpl.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.linewidth': 0.5,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})
```

### Multi-Panel Layout
```python
fig, axes = plt.subplots(2, 3, figsize=(7.2, 4.5))  # double-column
fig, axes = plt.subplots(1, 2, figsize=(3.5, 2.5))   # single-column
```

### Export
```python
plt.savefig('figure1.tiff', dpi=300, format='tiff', pil_kwargs={'compression': 'tiff_lzw'})
plt.savefig('figure1.pdf', dpi=300, format='pdf')  # vector
```

## R Workflow (ggplot2)

```r
library(ggplot2)
library(patchwork)

# Nature-style theme
theme_nature <- function() {
  theme_classic(base_family = "sans") +
  theme(
    text = element_text(size = 8),
    axis.title = element_text(size = 9),
    axis.text = element_text(size = 7),
    axis.line = element_line(linewidth = 0.5),
    legend.position = "right",
    plot.margin = unit(c(2, 2, 2, 2), "mm")
  )
}

# Multi-panel with patchwork
p1 + p2 + p3 + plot_layout(ncol = 3)

# Export
ggsave("figure1.tiff", dpi = 300, compression = "lzw", width = 89, height = 80, units = "mm")
ggsave("figure1.pdf", dpi = 300, width = 183, height = 100, units = "mm")
```

## Workflow

### Phase 1: Define Figure Contract
Before writing any code:
1. **Core conclusion** — What one point does this figure make?
2. **Evidence chain** — What data supports the conclusion?
3. **Archetype** — What visual form best communicates the finding?
4. **Panel plan** — Layout, hero panel, supporting panels
5. **Journal specs** — Nature/Nature Communications/etc. dimensions and formats

### Phase 2: Write and Test Code
Generate plotting code using the identified backend (Python or R):
- Use the quick-start template
- Include all data loading, processing, and visualization steps
- Test that the code runs (verify on sample data if available)

### Phase 3: Review and Polish
- Check: clear labeling, correct statistics, colorblind accessibility
- Verify: resolution, dimensions, font sizes meet journal requirements
- Review: is the conclusion immediately visible?

### Phase 4: Export
Export at correct specifications for the target journal.

## Figure QA Checklist

- [ ] Core conclusion is clear within 3 seconds of viewing
- [ ] Hero panel correctly identified and placed
- [ ] All axes labeled with units
- [ ] Color palette is colorblind-friendly
- [ ] Font sizes meet journal minimums
- [ ] Resolution ≥300 DPI
- [ ] Dimensions match journal specifications
- [ ] File format matches journal requirements
- [ ] No overlapping elements or text
- [ ] Legend is readable and correctly placed
- [ ] Error bars/confidence intervals are defined in caption
- [ ] Statistical annotations are clear
- [ ] Panel labels (a, b, c) are consistent and visible

## Anti-Patterns

1. **Plotting before thinking** — Writing code before defining the figure's conclusion leads to confusing figures that need extensive revision.
2. **Rainbow/viridis for categorical data** — Use qualitative palettes for categories, not sequential colormaps.
3. **Overcrowded panels** — More data in a single figure is not better. Split into multiple figures when the story is unclear.
4. **3D for 2D data** — 3D bar plots and pie charts obscure information. Avoid them.
5. **Inconsistent formatting** — Different panel font sizes, line widths, or color schemes within one figure.
6. **Missing error bars** — Every quantitative measurement must show variability or confidence.
7. **No data behind images** — Do not generate schematic or illustrative figures without scientific grounding.

## Verification

- [ ] Figure conclusion defined before coding
- [ ] Backend (Python/R) confirmed with user
- [ ] Code is runnable and produces the described figure
- [ ] Color palette is accessible and journal-appropriate
- [ ] Export specs match target journal requirements
- [ ] All data/statistics are accurate, not fabricated
- [ ] Figure caption is ready (include statistical details)
