employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000]
]

#print number of employees in this company
number_of_employees=len(employees)
print(" number os employees=",number_of_employees)

#print how much salary company has to raise in month end
total_amount=0
for emp in employees:
    total_amount+=emp[3]
print("total amount=",total_amount)

#group by designation of employees

d_count,da_count,ba_count=0,0,0
for emp in employees:
    if(emp[2]=="dataanalyst"):
        da_count+=1
    elif(emp[2]=="developer"):
        d_count+=1
    else:
        ba_count+=1
print("no: of developers=",d_count)
print("no: of dataanalyst=",da_count)
print("no: of ba =",ba_count)

#print highest salaried employee name
salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
high_salary=max(salary_list)
print("highest salary offered by the company is",high_salary)
for emp in employees:
    if(emp[3]==high_salary):
        print("highest salary paid employees are",emp)

#print employee name who receives lowest salary whose designation is developer
salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
low_salary=min(salary_list)
for emp in employees:
    if((emp[3]==low_salary) & (emp[2]=="developer")):
        print("lowest salary paid developer employees are",emp)