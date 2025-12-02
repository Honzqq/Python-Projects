def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

while True:
    number = int(input("Enter a number: "))

    if even(number):
        print("Result: Even")
    else:
        print("Result: Odd")

    confirmation = input("If you want to continue say YES if not say END: ")

    if confirmation == "END":
        break
    else:
        continue
