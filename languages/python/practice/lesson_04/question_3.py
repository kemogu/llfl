score = input("Please enter a score between 0-100: ")
score = int(score)

if score > 100 or score < 0:
    print("Invalid score.")
else:
    print("Valid Score")
