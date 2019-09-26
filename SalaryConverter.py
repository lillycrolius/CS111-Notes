def askUserSalary():
    annualSalary = int(input("Please enter your annual salary."))
    return annualSalary

def convertAnnualSalary(annualSalary):
    weeklyRate = annualSalary / 50
    hourlyRate = weeklyRate / 40
    return hourlyRate

salary = askUserSalary()

usersHourlyRate = convertAnnualSalary(salary)

print("Your hourly rate is " + str(usersHourlyRate))
