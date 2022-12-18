typehint:
mypy src/ tests/

test:
pytest tests/

lint:
pylint src/ tests/

# 1.PEP-8 같은 코딩 가이드라인 검사, 2.올바른 타입 사용했는지 검사, 3.최종 테스트 실행 (1개라도 실패 시 실패로 간주)
checklist: lint typehint test

.PHONY: typehint test lint checklist