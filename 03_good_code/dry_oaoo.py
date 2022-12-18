# 나쁜 예
def process_students_list(students):
    students_ranking = sorted(students, key=lambda s: s.passed * 11 - s.failed * 5 - s.years * 2)

    # 학생별 순위 출력
    for student in students_ranking:
        print(
            "이름: {0}, 점수: {1}".format(
                student.name,
                (student.passed * 11 - student.failed * 5 - student.years * 2)
            )
        )

# 좋은 예
def score_for_student(student):
    return student.passed * 11 - student.failed * 5 - student.years * 2

def process_students_list2(students):
    students_ranking = sorted(students, key=score_for_student)
    # 학생별 순위 출력
    for student in students_ranking:
        print("이름: {0}, 점수: {1}".format(student.name, score_for_student(student)))

