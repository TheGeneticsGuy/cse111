# Teams solution - Week 05
# CSV Files

import csv

# Reads the CSV file and returns a Dictionary
def read_dictionary(filename):

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        students = {}
        for line in reader:
            students[line[0]] = line[1]

    return students

# Checks if input is an integer and returns True
def is_valid_number( text ):

    num = 0
    try:
        num = int(text)
        return True
    except ValueError:
        return False

# Input is confirmed to only be numbers or a dash (hyphen)
def is_correct_format ( number ):

    for i in range (len(number)):

        if ( ord(number[i]) < 48 or ord(number[i]) > 57 ) and ord(number[i]) != 45:     #ASCII Values - Google the table to see
            return False

    return True

def add_student(id,name,students):
    students[id] = name

def main():
    print()
    students = read_dictionary("students.csv")

    while True:
        id = input("Please enter student ID: ")

        if is_correct_format ( id ) and len(id) == 9:

            if id in students:
                print(f"Student Found - Student Name: {students[id]}")
                break
            else:
                print('Student id not found!')

            print()

        else:
            if not is_correct_format ( id ):
                print("Invalid I-Number" )
            elif len(id) < 9:
                print("Invalid I-Number: too few digits" )
            else:
                print( "Invalid I-Number: too many digits" )

    # Adding a new student to the table
    # to_add = input('Do you want to add a new student? (Y/N): ').lower()

    # if to_add == 'y':
    #     new_id = input('Please enter their new ID: ')
    #     new_name = input('Please enter their full name')

    #     add_student(new_id, new_name, students)

    # print(f'{students[new_id]} was added with id {new_id}')
    print()

if __name__ == "__main__":
    main()