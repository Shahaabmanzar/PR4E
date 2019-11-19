largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        num1=int(num)
        if(num1>largest):
            largest=num1
        elif smallest is None or num1<smallest:
             smallest = num1
    except:
        print('Invalid input')
        continue


print("Maximum is", largest)
print("Minimum is",smallest)
