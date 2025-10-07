print("Enter marks obtained in 4 subjects")
maths = int(input("Maths: "))
english = int(input("English: "))
biology = int(input("Biology: "))
physics = int(input("Physics: "))
sum = maths + english + biology + physics
print("The sum of maths, english, biology and physics is: ")
percentage = (sum / 400) * 100
print(end= "Percentage marks = ")
print(percentage)