import conf
import pandas as pd 
connect=conf.conn

def show_employees():
    df = pd.read_sql_query("SELECT * FROM public.Employee", connect)
    print(df)

def show_employee_by_ssn(ssn): 
    df = pd.read_sql_query("SELECT * FROM public.Employee WHERE ssn = %s", connect, params=(ssn,))
    print(df)


def insert_employee():
    cursor=connect.cursor()
    ssn=input("Enter ssn: ")
    fname=input("Enter first name: ")  
    lname=input("Enter last name: ")
    salary=float(input("Enter salary: "))
    cursor.execute("INSERT INTO public.Employee (ssn, fname, lname, salary) VALUES (%s, %s, %s, %s)", (ssn, fname, lname, salary))
    connect.commit()
    print(pd.read_sql_query("SELECT * FROM public.Employee WHERE ssn = %s", connect, params=(ssn,)))


def update_employee_salary(ssn, new_salary):
    cursor=connect.cursor()
    cursor.execute("UPDATE public.Employee SET salary = %s WHERE ssn = %s", (new_salary, ssn))
    connect.commit()
    print(pd.read_sql_query("SELECT * FROM public.Employee WHERE ssn = %s", connect, params=(ssn,)))

def delete_employee_by_ssn(ssn):
    cursor=connect.cursor()
    print(pd.read_sql_query("SELECT fname FROM public.Employee WHERE ssn = %s", connect, params=(ssn,)),"has been deleted from the database.")
    cursor.execute("DELETE FROM public.Employee WHERE ssn = %s", (ssn,))
    connect.commit()

while True:

    print("1. Show all employees")
    print("2. Show employee by SSN")   
    print("3. insert new employee")
    print("4. update employee salary")
    print("5. delete employee by ssn")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        show_employees()
    elif choice == '2':
        ssn = input("Enter SSN: ")
        show_employee_by_ssn(ssn)
    elif choice == '3':
        insert_employee()
    elif choice == '4': 
        ssn = input("Enter SSN of the employee to update: ")
        new_salary = float(input("Enter new salary: "))
        update_employee_salary(ssn, new_salary)
    elif choice == '5':
        ssn = input("Enter SSN of the employee to delete: ")
        delete_employee_by_ssn(ssn)
    elif choice == '6':
        break   