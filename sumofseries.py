''' To calculate the sum of the positive integers of n+(n-2)+(n-4)...(until n-x=<0).
sum_series(6)->12
sum_series(10)->30 '''

def sum_series(n):
    if n<1:
       return n
    else:
       return n+sum_series(n-2)
n=int(input("enter the num to print the series"))
print(sum_series(n))
              
           
           
