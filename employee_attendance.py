employees = []

while True:
    print("\n===== Employee Attendance Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Mark Attendance")
    print("5. Update Attendance")
    print("6. Delete Employee")
    print("7. Count Employees")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Add Employee
    if choice == "1":
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")

        employee = {
            "id": employee_id,
            "name": name,
            "department": department,
            "attendance": "Not Marked"
        }

        employees.append(employee)
        print("Employee added successfully!")

    # View Employees
    elif choice == "2":
        if len(employees) == 0:
            print("No employees found.")
        else:
            print("\n--- Employee Details ---")

            for employee in employees:
                print("Employee ID:", employee["id"])
                print("Name:", employee["name"])
                print("Department:", employee["department"])
                print("Attendance:", employee["attendance"])
                print("------------------------")

    # Search Employee
    elif choice == "3":
        employee_id = input("Enter Employee ID to search: ")

        found = False

        for employee in employees:
            if employee["id"] == employee_id:
                print("\nEmployee Found!")
                print("Employee ID:", employee["id"])
                print("Name:", employee["name"])
                print("Department:", employee["department"])
                print("Attendance:", employee["attendance"])
                found = True
                break

        if not found:
            print("Employee not found.")

    # Mark Attendance
    elif choice == "4":
        employee_id = input("Enter Employee ID: ")

        found = False

        for employee in employees:
            if employee["id"] == employee_id:
                status = input("Enter Attendance (Present/Absent): ")

                if status.lower() == "present":
                    employee["attendance"] = "Present"
                    print("Attendance marked as Present.")
                elif status.lower() == "absent":
                    employee["attendance"] = "Absent"
                    print("Attendance marked as Absent.")
                else:
                    print("Invalid attendance status.")

                found = True
                break

        if not found:
            print("Employee not found.")

    # Update Attendance
    elif choice == "5":
        employee_id = input("Enter Employee ID: ")

        found = False

        for employee in employees:
            if employee["id"] == employee_id:
                status = input("Enter New Attendance (Present/Absent): ")

                if status.lower() == "present":
                    employee["attendance"] = "Present"
                    print("Attendance updated successfully.")
                elif status.lower() == "absent":
                    employee["attendance"] = "Absent"
                    print("Attendance updated successfully.")
                else:
                    print("Invalid attendance status.")

                found = True
                break

        if not found:
            print("Employee not found.")

    # Delete Employee
    elif choice == "6":
        employee_id = input("Enter Employee ID to delete: ")

        found = False

        for employee in employees:
            if employee["id"] == employee_id:
                employees.remove(employee)
                print("Employee deleted successfully.")
                found = True
                break

        if not found:
            print("Employee not found.")

    # Count Employees
    elif choice == "7":
        print("Total Employees:", len(employees))

    # Exit
    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
