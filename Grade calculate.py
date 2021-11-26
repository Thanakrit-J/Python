point = float(input("Enter your point : "))
grade = ["A","B","C","D","F"]
if point>=80 and point <=100:
    print(f"Grade : {grade[0]}")
elif point<80 and point>=70 :
    print(f"Grade : {grade[1]}")
elif point<70 and point>=60 :
    print(f"Grade : {grade[2]}")
elif point<60 and point>=50 :
    print(f"Grade : {grade[3]}")
elif point<50 and point>=0 :
    print(f"Grade : {grade[4]}")
else :
    print("Error")
