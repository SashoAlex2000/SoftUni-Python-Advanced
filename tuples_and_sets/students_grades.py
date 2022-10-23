

number_of_lines = int(input())

students_dict = {}

for turn in range(number_of_lines):
    command = input().split(" ")

    name = command[0]
    grade = float(command[1])

    if name not in students_dict.keys():
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)


for students_name, grade_list in students_dict.items():

    average_grade = sum(grade_list) / len(grade_list)
    new_list = [f"{x:.2f}" for x in grade_list]
    # new_list = [str(x) for x in grade_list]
    print(f"{students_name} -> "+ " ".join(new_list) + f" (avg: {average_grade:.2f})")

#pri generator, iterirame vednuj samo - ?, posle se e izcherpalo
