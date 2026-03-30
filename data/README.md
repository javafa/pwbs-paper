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

The experiment code (runner, evaluator, LLM client) is available in the companion repository `pwbs_experiment/`. This `data/` directory contains the benchmark inputs and prompt templates used in the paper. To reproduce:

1. Set up OpenAI API key in `config/settings.py`
2. Run: `python3 run_experiment.py --step main` (main experiment, 75 tasks × 5 methods × 2 models)
3. Run: `python3 run_experiment.py --step ablation` (ablation study)
4. Run: `python3 run_experiment.py --step consistency` (reasoning consistency)
5. Run: `python3 run_experiment.py --step public --primary-only` (GSM8K + BBH, GPT-4o only)

See the paper (Section 5) for full experimental setup details.
