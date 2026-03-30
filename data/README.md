# PWBS Benchmark Data & Prompt Templates

## Benchmarks (`benchmarks/`)

75 self-designed benchmark tasks across 3 categories (25 each):

| File | Category | Description |
|------|----------|-------------|
| `travel_planning.json` | Category A | N-day trip planning with budget, time, and dietary constraints |
| `code_debugging.json` | Category B | Buggy Python code + "fix without breaking existing tests" |
| `logical_reasoning.json` | Category C | Data analysis with explicit numerical criteria |

Each task includes: task description, ground truth, evaluation criteria, constraint definitions, and PWBS manual input (`pwbs_input`).

## Prompt Templates (`prompts/`)

| File | Method | Description |
|------|--------|-------------|
| `direct.py` | Direct | Task instruction only |
| `cot.py` | CoT | "Let's think step by step" |
| `plan_and_solve.py` | Plan-and-Solve | "Understand, plan, then solve" |
| `pwbs.py` | PWBS (manual) | 6-tuple G-A-F-C-T-V template |
| `cot_pwbs.py` | Ablation | CoT + PWBS component combinations (CoT+A, CoT+C, CoT+F, CoT+V, CoT+AC, CoT+ACFV) |
| `public_adapter.py` | Public benchmark | Prompt wrapper for GSM8K/BBH tasks |

## Reproducing Experiments

See the main [README.md](../README.md) for full experiment setup and execution instructions.
