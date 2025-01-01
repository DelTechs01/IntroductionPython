import sys
print('Number of Arguments:', len(sys.argv), 'arguments.')
print('Arguments List:', str(sys.argv))
x = int (sys.argv[1])
y = int (sys.argv[2])
z = x + y
print("x = ",x, "y = ", y, "z = ",z)