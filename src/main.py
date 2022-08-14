print("Enter X: ")
X = int(input())
print("Enter K: ")
K = int(input())

num = pow(10, K-1)
for digit in range(num, pow(10, K)):
    if (digit%X == 0):
        print("Output: ", digit)
        break