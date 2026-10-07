class Node:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add_beginning(self, student_id, name, marks):
        new = Node(student_id, name, marks)

        if self.head is None:
            self.head = new
            return

        new.next = self.head
        self.head = new

    def add_end(self, student_id, name, marks):
        new = Node(student_id, name, marks)

        if self.head is None:
            self.head = new
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new

    def insert_at_pos(self, student_id, name, marks, pos):
        new = Node(student_id, name, marks)

        if pos <= 0:
            print("Invalid Position")
            return

        if pos == 1:
            new.next = self.head
            self.head = new
            return

        temp = self.head
        i = 1

        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1

        if temp is None:
            print("Invalid Position")
            return

        new.next = temp.next
        temp.next = new

    def delete_by_id(self, student_id):
        if self.head is None:
            print("Student list is empty")
            return

        if self.head.student_id == student_id:
            self.head = self.head.next
            print("Student removed")
            return

        temp = self.head
        prev = None

        while temp is not None:
            if temp.student_id == student_id:
                prev.next = temp.next
                print("Student removed")
                return

            prev = temp
            temp = temp.next

        print("Student ID not found")

    def search(self, student_id):
        temp = self.head

        while temp is not None:
            if temp.student_id == student_id:
                print("Student found")
                print("ID:", temp.student_id)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                return

            temp = temp.next

        print("Student ID not found")

    def display(self):
        if self.head is None:
            print("No students registered")
            return

        temp = self.head

        while temp is not None:
            print("ID:", temp.student_id, "Name:", temp.name, "Marks:", temp.marks)
            temp = temp.next

    def count(self):
        temp = self.head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        print("Total students:", count)

    def highest_marks(self):
        if self.head is None:
            print("No students registered")
            return

        temp = self.head
        highest = self.head

        while temp is not None:
            if temp.marks > highest.marks:
                highest = temp

            temp = temp.next

        print("Student with highest marks:")
        print("ID:", highest.student_id)
        print("Name:", highest.name)
        print("Marks:", highest.marks)

    def reverse(self):
        prev = None
        temp = self.head

        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

        print("Registration order reversed")


students = StudentList()

while True:
    print("\n----- STUDENT REGISTRATION MENU -----")
    print("1. Register student at beginning")
    print("2. Register student at end")
    print("3. Register student at specified position")
    print("4. Remove student using Student ID")
    print("5. Search student using Student ID")
    print("6. Display all students")
    print("7. Display total number of students")
    print("8. Find student with highest marks")
    print("9. Reverse registration order")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))
        students.add_beginning(student_id, name, marks)

    elif choice == 2:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))
        students.add_end(student_id, name, marks)

    elif choice == 3:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))
        pos = int(input("Enter Position: "))
        students.insert_at_pos(student_id, name, marks, pos)

    elif choice == 4:
        student_id = int(input("Enter Student ID to remove: "))
        students.delete_by_id(student_id)

    elif choice == 5:
        student_id = int(input("Enter Student ID to search: "))
        students.search(student_id)

    elif choice == 6:
        students.display()

    elif choice == 7:
        students.count()

    elif choice == 8:
        students.highest_marks()

    elif choice == 9:
        students.reverse()

    elif choice == 10:
        print("Exiting application...")
        break

    else:
        print("Invalid choice")
