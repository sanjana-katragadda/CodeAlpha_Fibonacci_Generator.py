def fib(n):
    if n<=0:
        return []
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    series = [0,1]
    for i in range(2,n):
        next_term = series[-1]+series[-2]
        series.append(next_term)
    return series 
num_terms = int(input("Enter the no.of terms :"))
results=fib(num_terms)
print(f"fibonacci series with {num_terms} terms:{results}")