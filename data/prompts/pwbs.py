"""PWBS prompting: 5-tuple 구조 (Goal → Assumption → Constraint → Task → Validation) 유도.

PWBS 방법론의 핵심 프롬프트 템플릿.
실제 실행은 engine/feedback_loop.py의 pwbs_execute()에서 수행.
이 모듈은 단순 single-call PWBS 프롬프트를 제공한다.
"""

PWBS_TEMPLATE = """다음 과제를 PWBS(Prompt Work Breakdown Structure) 프레임워크에 따라 수행하시오.

과제: {task_input}

아래 구조를 순서대로 작성한 후 최종 답변을 제시하시오.

[GOAL]
과제의 최종 목표를 측정 가능한 형태로 기술하시오.

[ASSUMPTIONS]
이 과제를 수행하기 위해 참으로 가정해야 하는 전제 조건을 모두 나열하시오.
특히 입력 데이터의 형식, 실행 환경, 사용자의 의도에 대한 암묵적 가정을 명시하시오.
각 가정에 대해, 그 가정이 거짓일 경우 추론에 미치는 영향을 기술하시오.

- A1: (가정)
  거짓일 경우의 영향: (영향)

[CONSTRAINTS]
과제 수행 시 반드시 준수해야 하는 제약 조건을 나열하시오.
각 제약에 대해, 위반 시 해가 무효화되는 이유를 기술하시오.

- C1: (제약)
  위반 시 영향: (영향)

[TASKS]
목표 달성을 위한 세부 작업을 순서대로 나열하시오.
각 작업에 대해 근거(why), 방법(method), 기대 산출물(output),
의존하는 가정/제약(depends_on)을 명시하시오.

- T1:
    why: (이 작업이 필요한 이유)
    method: (수행 방법)
    output: (기대 산출물)
    depends_on: [A1, C1, ...]

[VALIDATION]
- V1: Goal 달성 여부 검증 기준
- V2: Assumption 충족 여부 검증 기준
- V3: Constraint 준수 여부 검증 기준

[ANSWER]
위 구조에 따라 과제를 수행한 최종 답변을 제시하시오.
"""


def build_pwbs_prompt(task_input: str) -> str:
    return PWBS_TEMPLATE.format(task_input=task_input)
