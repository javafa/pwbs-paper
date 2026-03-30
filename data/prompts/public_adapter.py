"""공개 벤치마크(GSM8K, BBH)용 프롬프트 어댑터.

기존 방법론(Direct, CoT, Plan-and-Solve)은 그대로 적용하되,
PWBS auto는 Planner가 자동 생성하므로 별도 처리 없음.
"""

from __future__ import annotations

from prompts.direct import build_direct_prompt
from prompts.cot import build_cot_prompt
from prompts.plan_and_solve import build_plan_and_solve_prompt


def build_public_prompt(task: dict, method: str) -> str:
    """공개 벤치마크 태스크에 방법론별 프롬프트를 적용.

    Args:
        task: 벤치마크 태스크 dict (loader에서 생성)
        method: "direct", "cot", "plan_and_solve"
            ("pwbs_auto"는 runner에서 Planner를 직접 호출하므로 여기서 처리하지 않음)

    Returns:
        완성된 프롬프트 문자열
    """
    task_input = task["input"]
    category = task.get("category", "")

    # GSM8K: 수학 문제 → "Answer with a number." 지시 추가
    if category == "gsm8k":
        task_input = (
            f"{task_input}\n\n"
            "Solve this math problem. "
            "Show your work and provide the final numerical answer after '####'."
        )

    # BBH: 원본 형식 유지 (이미 지시문 포함)
    elif category == "bbh":
        subtask = task.get("subcategory", "")
        task_input = (
            f"{task_input}\n\n"
            "Provide only the final answer without explanation."
        )

    if method == "direct":
        return build_direct_prompt(task_input)
    elif method == "cot":
        return build_cot_prompt(task_input)
    elif method == "plan_and_solve":
        return build_plan_and_solve_prompt(task_input)
    else:
        raise ValueError(f"Unsupported method for public benchmark: {method}")
