#Giles Ali Gepulane
name = input("Enter your username: ")
section = input("Enter your section: ")


prelim = float(input("Prelim Grade: "))

if not prelim <= 100 or not prelim >=40:
    print("Error")
    quit()
else:
    print(f"Your Prelim Grade is {prelim:.2f}")
    
 
midterm = float(input("Midterm Grade: "))

if not midterm <= 100 or not midterm >=40:
    print("Error")
    quit()
else:
    print(f"Your Midterm Grade is {midterm:.2f}")


finals = float(input("Finals Grade: "))

if not finals <= 100 or not finals >=40:
    print("Error")
    quit()
else:
    print(f"Your finals Grade is {finals:.2f}")


finalGrade = round((prelim * 0.33332) + (midterm * 0.33332) + (finals * 0.33332))

if finalGrade == 99 or finalGrade == 100:
    gpa = 1.00
    desc = "Excellent"
elif finalGrade >= 96 and finalGrade <= 98:
    gpa = 1.25
    desc = "Outstanding"
elif finalGrade >= 93 and finalGrade <= 95:
    gpa = 1.50
    desc = "Superior"
elif finalGrade >= 90 and finalGrade <= 92:
    gpa = 1.75
    desc = "Very Good"
elif finalGrade >= 87 and finalGrade <= 89:
    gpa = 2.00
    desc = "Good"
elif finalGrade >= 84 and finalGrade <= 86:
    gpa = 2.25
    desc = "Satisfactory"
elif finalGrade >= 81 and finalGrade <= 83:
    gpa = 2.50
    desc = "Fairly Satisfactory"
elif finalGrade >= 78 and finalGrade <= 80:
    gpa = 2.75
    desc = "Fair"
elif finalGrade >= 75 and finalGrade <= 77:
    gpa = 3.00
    desc = "Passed"
elif finalGrade <75:
    gpa = 5.0
    desc = "Failed"

print(f"Final Grade: {finalGrade}%")
print("GPA:", gpa)
print(desc)
