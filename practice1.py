dividend = input("Give me a dividend: ")
divisor = input ("Give me a divisor: ")

dividend = int(dividend)
divisor  = int(divisor)

x = dividend // divisor
y = dividend % divisor

x = str(x)
y = str(y)

print("The answer is " + x + " with a remainder of " + y) 