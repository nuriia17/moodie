def calculate_statistics():
    num_grades = int(input("how many points will you write: "))

    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    for _ in range(num_grades):
        grade = int(input("write your point: "))

        if 90 <= grade <= 100:
            grade_counts['A'] += 1
        elif 75 <= grade < 90:
            grade_counts['B'] += 1
        elif 60 <= grade < 75:
            grade_counts['C'] += 1
        elif 50 <= grade < 60:
            grade_counts['D'] += 1
        elif 0 <= grade < 50:
            grade_counts['F'] += 1
        else:
            print("Don't lie")
            continue

    results = {}
    for grade, count in grade_counts.items():
        percentage = (count / num_grades) * 100 if num_grades > 0 else 0
        results[grade] = (count, percentage)

    for grade, (count, percentage) in results.items():
        if count == 1:print(f"{grade}: {count} grade ({percentage:.2f}%)")

        else:
            print(f"{grade}: {count} grades ({percentage:.2f}%)")

calculate_statistics()
