"""CoT + PWBS 구성요소 조합 프롬프트.

Ablation Study용: CoT를 베이스로 PWBS 구성요소를 하나씩 추가하여
각 구성요소의 기여도를 측정한다.

조합:
  cot              : Let's think step by step. (베이스라인)
  cot+A            : CoT + Assumption 표면화
  cot+C            : CoT + Constraint 명시
  cot+F            : CoT + Formula 보존
  cot+V            : CoT + Validation 체크
  cot+AC           : CoT + Assumption + Constraint
  cot+ACFV (=PWBS) : CoT + 전체 PWBS 구조
"""


def build_cot_a_prompt(task_input: str) -> str:
    """CoT + Assumption: 암묵적 가정을 먼저 표면화한 후 단계별 추론."""
    return f"""{task_input}

이 과제를 수행하기 전에, 먼저 이 과제를 풀기 위해 참이라고 가정해야 하는 전제 조건을 나열하시오.
각 가정에 대해 거짓일 경우 추론에 미치는 영향을 기술하시오.

그 다음, Let's think step by step. 단계별로 풀어 최종 답변을 제시하시오."""


def build_cot_c_prompt(task_input: str) -> str:
    """CoT + Constraint: 제약 조건을 먼저 명시한 후 단계별 추론."""
    return f"""{task_input}

이 과제를 수행하기 전에, 먼저 반드시 준수해야 하는 제약 조건을 모두 나열하시오.
각 제약에 대해 위반 시 답이 무효화되는 이유를 기술하시오.

그 다음, Let's think step by step. 모든 제약을 만족하면서 단계별로 풀어 최종 답변을 제시하시오."""


def build_cot_f_prompt(task_input: str) -> str:
    """CoT + Formula: 수식/공식을 먼저 정리한 후 단계별 추론."""
    return f"""{task_input}

이 과제에 계산 공식이 포함되어 있다면, 먼저 해당 공식을 원문 그대로 정리하시오.
공식의 각 변수가 무엇을 의미하는지 명시하시오.

그 다음, Let's think step by step. 공식을 정확히 적용하면서 단계별로 풀어 최종 답변을 제시하시오."""


def build_cot_v_prompt(task_input: str) -> str:
    """CoT + Validation: 단계별 추론 후 검증 단계 추가."""
    return f"""{task_input}

Let's think step by step.

단계별로 풀어 답변을 도출한 후, 반드시 다음을 검증하시오:
1. 과제의 최종 목표가 달성되었는가?
2. 모든 제약 조건이 충족되었는가?
3. 계산이 있다면 수치가 정확한가?

검증 결과를 명시한 후 최종 답변을 제시하시오."""


def build_cot_ac_prompt(task_input: str) -> str:
    """CoT + Assumption + Constraint: 가정과 제약을 모두 명시한 후 추론."""
    return f"""{task_input}

이 과제를 수행하기 전에:

[ASSUMPTIONS] 이 과제를 풀기 위해 참이라고 가정하는 전제 조건을 나열하시오.
각 가정에 대해 거짓일 경우의 영향을 기술하시오.

[CONSTRAINTS] 반드시 준수해야 하는 제약 조건을 나열하시오.
각 제약에 대해 위반 시 영향을 기술하시오.

그 다음, Let's think step by step. 위 가정과 제약을 고려하면서 단계별로 풀어 최종 답변을 제시하시오."""


def build_cot_acfv_prompt(task_input: str) -> str:
    """CoT + ACFV (전체 PWBS): 모든 PWBS 구성요소를 CoT 위에 적용."""
    return f"""{task_input}

이 과제를 수행하기 전에 아래 구조를 먼저 작성하시오:

[ASSUMPTIONS] 이 과제를 풀기 위해 참이라고 가정하는 전제 조건을 나열하시오.
각 가정에 대해 거짓일 경우의 영향을 기술하시오.

[FORMULA] 과제에 계산 공식이 있다면 원문 그대로 정리하시오. 없으면 생략.

[CONSTRAINTS] 반드시 준수해야 하는 제약 조건을 나열하시오.
각 제약에 대해 위반 시 영향을 기술하시오.

그 다음, Let's think step by step. 위 가정, 공식, 제약을 고려하면서 단계별로 풀어 답변을 도출하시오.

마지막으로 [VALIDATION]을 수행하시오:
1. 모든 가정이 유지되었는가?
2. 공식이 정확히 적용되었는가?
3. 모든 제약이 충족되었는가?

검증 결과를 명시한 후 최종 답변을 제시하시오."""


# Ablation 설정 매핑
ABLATION_BUILDERS = {
    "cot_a": build_cot_a_prompt,
    "cot_c": build_cot_c_prompt,
    "cot_f": build_cot_f_prompt,
    "cot_v": build_cot_v_prompt,
    "cot_ac": build_cot_ac_prompt,
    "cot_acfv": build_cot_acfv_prompt,
}
