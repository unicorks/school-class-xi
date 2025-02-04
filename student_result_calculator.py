# write a program to accept name and roll no, marks in 5 subjects, calculate total and percentage and display the result
print("----STUDENT RESULT CALCULATOR----")
name = input("Please enter your name: ")
roll_no = int(input("Please enter your roll no: "))
print("Now, please enter your marks subjectwise out of 80.")
eng = float(input("English: "))
hindi = float(input("Hindi: "))
math = float(input("Math: "))
sci = float(input("Science: "))
sst = float(input("Social Science: "))
total = eng+hindi+math+sci+sst
percentage = total*100/(80*5)

print("----RESULT----")
print("Name of the student: ", name)
print("Roll number: ", roll_no)
print("Total marks: ", total, "/ 400")
print("Percentage: ", percentage)



    
