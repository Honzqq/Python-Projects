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

    potvrzeni = input("If you want to continue say YES if not say END: ")

    if potvrzeni == "END":
        break
    else:
        continue
