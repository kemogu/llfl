age = input("Please enter your age: ")
age = int(age)

has_ticket = False

ticket_input = input("Do you have ticket? (y/n)").strip()

if "y" == ticket_input:
    has_ticket = True

if age >= 18 and has_ticket:
    print("Allowed.")
else:
    print("Denied.")