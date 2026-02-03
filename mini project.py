subjects = []

while True:
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects > 0:
            break
        print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

for i in range(1, num_subjects + 1):
    
    while True:
        name = input(f"Enter name for subject {i}: ").strip()
        if name:
            break
        print("Subject name cannot be empty. Please enter a name.")

    
    while True:
        try:
            mark = float(input(f"Enter mark for '{name}': "))
            if 0 <= mark <= 100:
                break
            print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    subjects.append((name, mark))


if len(subjects) == num_subjects:
    passing_marks = 40
    marks = [m for _, m in subjects]

    total_marks = sum(marks)
    average = total_marks / len(marks)
    max_mark = max(marks)
    min_mark = min(marks)

    
    max_subject = next(n for n, m in subjects if m == max_mark)
    min_subject = next(n for n, m in subjects if m == min_mark)

    print(f"\nTotal Marks: {total_marks}")
    print(f"Average Mark: {average:.2f}")
    print(f"Highest: {max_mark} ({max_subject})")
    print(f"Lowest: {min_mark} ({min_subject})")
    print(f"Number of Subjects: {len(subjects)}\n")

    print("Subject-wise results:")
    for idx, (name, mark) in enumerate(subjects, start=1):
        status = "Pass" if mark >= passing_marks else "Fail"
        print(f"{idx}. {name}: {mark} — {status}")

    passed = [(n, m) for n, m in subjects if m >= passing_marks]
    print(f"\nPassed subjects ({len(passed)}): {passed}")

    sorted_asc = sorted(subjects, key=lambda x: x[1])
    sorted_desc = list(reversed(sorted_asc))
    print("\nSorted (low → high):")
    for n, m in sorted_asc:
        print(f"  {n}: {m}")

    abs_difference = abs(max_mark - min_mark)
    print(f"\nAbsolute Difference between Highest and Lowest Marks: {abs_difference}")
else:
    print("Error: unexpected input count.")

