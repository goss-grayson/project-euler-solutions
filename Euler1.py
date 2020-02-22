### Grayson Goss
### 01/02/2020
### Euler Problem 1 Solution

summation = 0;

for i in range(3, 1000):
    if ( ( i % 3 ) == 0 ):
        summation = summation + i;
        continue;
    if ( ( ( i % 5 ) == 0 ) and ( (i % 15) != 0 ) ):
        summation = summation + i;
        continue;
    
print(summation);


