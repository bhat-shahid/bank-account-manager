def is_prime(n):
    if n<2:
        return False
    for i in range(2, (int(n**0.5)+1)):
        if n%i==0:
            return False
    return True



rows=3
cols=4
matrix=[[num**0.5 if row%2==0 and num%6==0 else "Even" 
         if row%2==0 and num%2==0 else "Odd" if row%2==0
         else "Prime" if is_prime(num)
         else num**3 if col%2==0 and num%5==0
         else "-"
         for col in range(cols)
         for num in [row*cols+col+1]]
         for row in range(rows)]
print(matrix)