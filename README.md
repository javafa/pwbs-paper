# PWBS: Prompt Work Breakdown Structure — A Structured Planning Framework for LLM Reasoning

A structured prompting framework inspired by Work Breakdown Structure (WBS) principles (PMBOK; PMI, 2021) for LLM prompt engineering. **PWBS targets multi-constraint structured-output tasks** — such as travel planning, code debugging, and data analysis — where multiple conditions must be simultaneously satisfied and outputs require complex structure, rather than single-answer problem solving.

## Abstract

Large Language Models often fail to satisfy multiple constraints simultaneously, lose critical formulas during multi-call architectures, and produce inconsistent outputs across repeated runs. PWBS addresses these challenges by decomposing prompts into six explicit components — **Goal, Assumption, Formula, Constraint, Task, and Validation** — using a 4-step Invalidation Test for systematic classification.

Experiments on 75 custom benchmarks across three domains (travel planning, code debugging, logical reasoning) and 210 public benchmark tasks (GSM8K; Cobbe et al., 2021, BIG-Bench Hard; Suzgun et al., 2023) with GPT-4o and GPT-4o-mini demonstrate that selectively applying structural components improves task success rate and reasoning consistency. Public benchmark validation confirms PWBS's scope: it underperforms baselines on single-answer tasks but achieves the highest score on boolean_expressions (96.7%), where logical structure aligns with PWBS components.

## Key Findings

- **Assumption surfacing is universally effective**: +4.0%p improvement across both models — the most robust single intervention
- **Inverse scaling with model capability**: Constraint specification helps weaker models (+8.0%p on GPT-4o-mini) but slightly hurts stronger ones (−2.7%p on GPT-4o)
- **Component accumulation shows diminishing returns**: Selective application outperforms using all six components together
- **Reasoning consistency**: +32.0%p improvement in code debugging tasks (temperature=0.7)
- **CSR Transparency Paradox**: PWBS's lower Constraint Satisfaction Rate is a measurement artifact — explicit handling reveals violations that implicit methods hide
- **Task-type selectivity**: Public benchmarks confirm PWBS excels at structured-output tasks (boolean_expressions: 96.7%) but shows limited benefit for single-answer problems

## Framework Overview

### 6-Tuple Structure (G-A-F-C-T-V)

| Component | Role | Invalidation Test |
|-----------|------|-------------------|
| **Goal** | Measurable objective + subject data | If changed → different task entirely |
| **Assumption** | Explicit premises for reasoning | If false → reasoning process invalidated |
| **Formula** | Exact calculation rules (preserved verbatim) | If changed → numerical results differ |
| **Constraint** | Verifiable conditions the solution must satisfy | If violated → solution is inadequate |
| **Task** | Step-by-step execution plan | Derived from above components |
| **Validation** | Self-verification checklist | Checks G, A, F, C compliance |

### Key Mechanisms

- **Adaptive Tolerance**: Systematic constraint relaxation (0% → 10% → 20% → 30%) with transparent logging
- **Data/Formula Preserving**: Prevents information loss when AI Planner generates PWBS automatically (2-call architecture)
- **Constraint Coupling**: Classifies constraint interdependencies (coupled/pipeline/independent) to determine optimal task decomposition level

## Experiment Design

### Benchmarks
- **Category A** — Travel Planning (25 tasks): Multi-constraint satisfaction, budget/time limits
- **Category B** — Code Debugging (25 tasks): Bug fix with existing test preservation
- **Category C** — Logical Reasoning (25 tasks): Data analysis with explicit decision criteria

### Methods Compared
| Method | API Calls | Description |
|--------|-----------|-------------|
| Direct | 1 | Task instruction only |
| CoT | 1 | + "Let's think step by step" |
| Plan-and-Solve | 1 | + Planning phase before solving |
| PWBS (manual) | 1 | Human-authored 6-tuple structure |
| PWBS (auto) | 2 | AI Planner generates 6-tuple + LLM executes |

### Public Benchmarks
- **GSM8K** (n=105): Elementary math — Formula preservation, Assumption surfacing
- **BIG-Bench Hard** (n=105): Multi-step reasoning — 4 subtasks (boolean_expressions, causal_judgement, date_understanding, tracking_shuffled_objects)

### Ablation Study (CoT + PWBS Components)
Tested on GPT-4o: CoT base, CoT+A, CoT+C, CoT+F, CoT+V, CoT+AC, CoT+ACFV

## Results Summary

### Task Success Rate (GPT-4o)
| Method | Travel | Code | Logic | Overall |
|--------|--------|------|-------|---------|
| Direct | 72% | 80% | 96% | 82.7% |
| CoT | 84% | 88% | 100% | 90.7% |
| Plan-and-Solve | 80% | 84% | 96% | 86.7% |
| PWBS (manual) | 88% | 92% | 100% | 93.3% |
| PWBS (auto) | 80% | 88% | 100% | 89.3% |

### Reasoning Consistency (3 runs, temp=0.7)
| Method | Avg RC | Perfect (3/3) |
|--------|--------|---------------|
| CoT | 32.9% | 23/75 |
| PWBS | 43.1% | 28/75 |

### Public Benchmark Results (GPT-4o)
| Benchmark | Direct | CoT | P&S | PWBS auto |
|-----------|--------|-----|-----|-----------|
| GSM8K (n=105) | **94.3%** | 93.3% | 93.3% | 64.8% |
| BBH (n=105) | 64.8% | **65.7%** | 64.8% | 40.0% |
| Overall (n=210) | **79.5%** | **79.5%** | 79.0% | 52.4% |

| BBH Subtask | Direct | CoT | P&S | PWBS auto |
|-------------|--------|-----|-----|-----------|
| boolean_expressions (n=30) | 86.7% | 86.7% | 83.3% | **96.7%** |
| causal_judgement (n=25) | **72.0%** | 68.0% | 72.0% | 8.0% |
| date_understanding (n=25) | 60.0% | **68.0%** | 64.0% | 28.0% |
| tracking_shuffled (n=25) | 36.0% | 36.0% | 36.0% | 16.0% |

PWBS achieves the highest score (96.7%) on boolean_expressions where logical structure aligns with PWBS components, confirming its value as a **selective** tool for structure-amenable tasks. Note: PWBS targets multi-constraint structured-output tasks; these single-answer benchmarks test generalization boundaries rather than the intended use case.

> **Statistical note:** Main experiment pairwise comparisons show no statistically significant differences ($p > 0.05$). Ablation differences (e.g., +4.0%p, +8.0%p) are directional observations on per-category subsets ($n=25$), not formally significance-tested.

## Compilation

```bash
pdflatex main.tex
pdflatex main.tex  # run twice for TOC and references
```

Requires standard LaTeX packages: `booktabs`, `multirow`, `hyperref`, `geometry`, `natbib`.

## Repository Structure

```
├── main.tex                          # Full paper LaTeX source
├── README.md
├── .gitignore
├── LICENSE
└── data/
    ├── README.md                     # Data documentation
    ├── benchmarks/
    │   ├── travel_planning.json      # Category A: 25 tasks
    │   ├── code_debugging.json       # Category B: 25 tasks
    │   └── logical_reasoning.json    # Category C: 25 tasks
    └── prompts/
        ├── direct.py                 # Direct prompting template
        ├── cot.py                    # Chain-of-Thought template
        ├── plan_and_solve.py         # Plan-and-Solve template
        ├── pwbs.py                   # PWBS 6-tuple template
        ├── cot_pwbs.py               # Ablation combinations (CoT+A, CoT+C, etc.)
        └── public_adapter.py         # GSM8K/BBH prompt wrapper
```

## Key References

- Wei et al. (2022) — Chain-of-Thought Prompting
- Wang et al. (2023a) — Plan-and-Solve Prompting
- Wang et al. (2023b) — Self-Consistency
- Zhou et al. (2023) — Least-to-Most Prompting
- Khot et al. (2023) — Decomposed Prompting
- Chen et al. (2023) — Program of Thoughts
- Cobbe et al. (2021) — GSM8K
- Suzgun et al. (2023) — BIG-Bench Hard
- PMI (2021) — PMBOK Guide (WBS)

Full reference list (16 papers) in `main.tex`.

## Authors

**Donho Ko**, **Eunyoung Shin** — DIFAI Inc.

## License

CC BY 4.0
