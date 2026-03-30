"""Chain-of-Thought prompting: 단계별 추론 유도."""


def build_cot_prompt(task_input: str) -> str:
    return f"{task_input}\n\nLet's think step by step."
