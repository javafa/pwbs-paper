"""Plan-and-Solve prompting: 계획 수립 후 단계별 실행."""


def build_plan_and_solve_prompt(task_input: str) -> str:
    return (
        f"{task_input}\n\n"
        "Let's first understand the problem and devise a plan to solve it. "
        "Then, let's carry out the plan and solve the problem step by step."
    )
