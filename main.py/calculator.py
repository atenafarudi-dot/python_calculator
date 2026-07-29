print("======calculator======")

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return 'cant divide by zero'
while True:
    print("\n choose an operation(1-5):")
    print('1. addition (+)')
    print('2. subtraction (-)')
    print('3. multiplication (*)')
    print('4. division (/)')
    print('5. exit')
    choice = input('enter your choice: ')
    if choice == '5':
        print("bye!")
        break
    n1 = int(input('your first number: '))
    n2 = int(input('your second number: '))
    if choice == '1':
        result = add(n1, n2)
    elif choice == '2':
        result = sub(n1, n2)
    elif choice == '3':
        result = mult(n1, n2)
    elif choice == '4':
        result = div(n1, n2)
    else:
        result = "Invalid choice"
    print('result:', result)