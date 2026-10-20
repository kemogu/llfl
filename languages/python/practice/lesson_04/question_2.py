import sys

score = input("Please enter a score between 0-100: ")
score = int(score)

if score > 100:
    print("score bigger than limit.")
    sys.exit(0)
elif score < 0:
    print("score lower than limit.")
    sys.exit(0)

if score >= 90:
    print("excellent")
elif score >= 60:
    print("passed")
else:
    print("keep practicing")