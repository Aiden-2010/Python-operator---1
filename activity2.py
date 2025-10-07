#count the note
#write a program to calculate the number of notes in the given amount
amount = int(input("Please enter an amount for withdraw: "))
note_1 = amount // 100
note_2 = (amount % 100) // 50
note_3 = ((amount % 100) % 50) // 10
print("Note of 100 rupee",note_1)
print("Note of 50 rupee",note_2)
print("Note of 10 rupee",note_3)