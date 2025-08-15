def is_prime(n):
    if n<2:
        return False
    for i in range(2, (int(n**0.5)+1)):
        if n%i==0:
            return False
    return True

rows=3
cols=4
new_matrix=[]
for row in range(rows):
    new_list=[]
    for col in range(cols):
        num=row*cols+col+1
        if col%2==0 and num%4==0:
            num=num**2
        elif row%2==0 and num%5==0:
            num=num**3
            
        elif is_prime(num):
            num="Prime"
        else:
            num="X"
        new_list.append(num)
    print(new_list)
        

        