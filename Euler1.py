### Grayson Goss
### 01/02/2020
### Euler Problem 1 Solution

s = 0;

for i in range(3, 1001):
    if ( ( i % 3 ) == 0 ):
        s += i;
    elif ( ( ( i % 5 ) == 0 ) and ( ( i % 15 ) != 0 ) ):
        s += i;
    
print(s);


