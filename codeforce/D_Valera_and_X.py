n=int(input())
x=[]
for j in range(n):
        l=list(input())
        x.append(l)
a=x[0][0]
b=x[0][1]

t = 'YES'
n = len(x)  # Get the size of the square matrix

# Loop through each element in the matrix
for i in range(n):
    for j in range(n):
        # Check for diagonal elements
        if i == j or j == n - 1 - i:
            if x[i][j] != a:
                t = 'NO'
                break
        # Check for non-diagonal elements
        else:
            if x[i][j] != b:
                t = 'NO'
                break

# Print the result
print(t)
