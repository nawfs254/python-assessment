#Problem brief: There are 5 employers there, 1 supervisor and 4 employees. Daily production value is 100 BDT. Supervisors get 60% and employees get 40% of the production rate which will devide into 4 employees. Here, also count the absent employees, where the remaining value will be distribute on the given ratio among the employers. Now, writing the function to get the amount they get on the working day.


#Solution:

totalEmployer = 5 #Number of Employee (including 1 supervisor)
perDayProdValue = 100 #Production value (per day)

def result(supSalary, empSalary):
    print("=== Result ===")
    print("Supervisor will get: ", supSalary)
    print("Per Employee will get: ", empSalary)

def salaryCount(sup, emp):
    salaryPercentageOfSupPerDay = 0.6 * 100
    salaryPercentageOfEmpPerDay = 0.4 * 100

    supSalary = 1 * salaryPercentageOfSupPerDay
    empSalary = salaryPercentageOfEmpPerDay / 4

    absentEmp = totalEmployer - (sup + emp)

    #if any employer is absent
    if absentEmp > 0:
        #if supervisor is present
        if (sup == 1):
            remainingBalance = absentEmp * empSalary
            supGet = 0.6 * remainingBalance
            empGet = (0.4 * remainingBalance) / emp

            supSalary += supGet
            empSalary += empGet

            result(supSalary, empSalary)

        #if supervisor is absent
        if (sup == 0):
            remainingBalance = supSalary + ((absentEmp - 1) * empSalary)
            empGet = remainingBalance / emp
            empSalary += empGet
            supSalary = 0
            result(supSalary, empSalary)

    #if all employers are present
    else:
        result(supSalary, empSalary)
        


def main():
    print("===========Employer Salary Count=========== \n")    
    presentSup = int(input("Enter the number of Supervisor present: "))
    if(presentSup > 1):
        print("Max Supervisor should be 1")
        return "Max Supervisor should be 1"
    
    presentEmp = int(input("Enter the number of Employee present: "))
    if(presentEmp > 4):
        print("Max Employee should be 4")
        return "Max Employee should be 4"
    
    if(presentEmp < 1):
        print("Min Employee should be 1")
        return "Min Employee should be 1"
    
    totalPresent = presentEmp + presentSup

    salaryCount(presentSup , presentEmp)

                

main()