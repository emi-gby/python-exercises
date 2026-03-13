students_dict = {
    "Ana": (8.0, 7.5, 9.0),
    "Carlos": (6.0, 5.0, 7.0)
}

students_set = {'Ana', 'Carlos'}

def register_student():
    '''Adds a student as a key in students_dict with an empty tuple as value'''

    student = input('Enter the name of the student to register: ').capitalize()
    # check for unique students using a set
    if student not in students_set:
        students_dict[student] = ()
        students_set.add(student)
        print('-------------------------------------')
        print('Student registered successfully!')
    else:
        print('-------------------------------------')
        print('Student already enrolled!')

def record_grades():
    '''Checks if student already has grades recorded; if not, adds 3 grades as a tuple for the student key'''

    student = input('Enter the name of the student to record grades: ').capitalize()
    for k, v in students_dict.items():
        if student == k and len(v) != 0:
            print('-------------------------------------')
            print(f'{student} already has grades recorded')
            return

        # if input matches a registered student and their grades tuple is empty
        elif student == k and len(v) == 0:
            grades = []
            try:
                # add 3 grades to a list, then convert list to tuple
                for i in range(1, 4):
                    grade = float(input(f'Enter grade {i}: '))
                    if 0 <= grade <= 10:
                        grades.append(grade)
                    else:
                        print('Invalid grade. Grades must be between 0 and 10! Try again.')
                        return

                students_dict[student] = tuple(grades)
                print('-------------------------------------')
                print('Grades added successfully!')
            except ValueError:
                print('-------------------------------------')
                print('Invalid grade value.')

            return
    print('-------------------------------------')
    print(f'Student {student} is not enrolled.')

def list_students_and_averages():
    '''Lists students in students_dict and calculates their respective averages'''

    print('-------------------------------------')
    for k, v in students_dict.items():
        avg = round(sum(v)/3, 1) if len(v) != 0 else 'Grades not recorded'
        print(f'Student : {k} - Average : {avg}')

def search_student():
    '''Displays student data if found in students_dict'''

    student = input('Enter the name of the student to search: ').capitalize()
    for k, v in students_dict.items():
        if student == k:
            print('-------------------------------------')
            print(f'Student enrolled. \nStudent : {k} - Grades : {v}')
            return
    print('-------------------------------------')
    print(f'Student {student} not enrolled.')

def show_passed_failed():
    '''Calculates average for each student and defines their status'''
    print('-------------------------------------')
    for k, v in students_dict.items():
        if len(v) == 0:
            status = 'Grades not recorded'
        else:
            avg = round(sum(v)/3, 1)
            status = 'Passed' if avg >= 7 else 'Failed'

        print(f'{k} : {status}')

def reports():
    '''Displays desired report according to selected type'''
    print('Report types:\n1- Registered students\n2- Individual averages\n3- Students status')
    report_type = input('Choose report type : ')
    if report_type == '1':
        print('-------------------------------------')
        print('Registered students: ')
        print('-------------------------------------')
        for k in students_dict.keys():
            print(k)

    elif report_type == '2':
        print('-------------------------------------')
        print('Individual averages: ')
        list_students_and_averages()

    elif report_type == '3':
        print('-------------------------------------')
        print('Students status: ')
        show_passed_failed()
    else:
        print("Invalid type! This option is not available in the system!")


while True:
    print('-------------------------------------')
    print("1 - Register student")
    print("2 - Record grades")
    print("3 - List students and averages")
    print("4 - Search student")
    print("5 - Show passed and failed")
    print("6 - Reports")
    print("0 - Exit")
    print('-------------------------------------')
    option = input("Choose an option: ")
    print('-------------------------------------')

    if option == "1":
        register_student()
    elif option == "2":
        record_grades()
    elif option == "3":
        list_students_and_averages()
    elif option == "4":
        search_student()
    elif option == "5":
        show_passed_failed()
    elif option == "6":
        reports()
    elif option == "0":
        print("System terminated!")
        break
    else:
        print("Invalid option! This option is not available in the system!")
