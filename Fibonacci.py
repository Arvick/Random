def fibonacci(startnum=1,num=20):
    fib=[1,1]
    while len(fib)<num:
        fib.append(fib[-1]+fib[-2])
    fib=list(map(str,fib))
    try:
        fib=fib[fib.index(str(startnum)):]
    except ValueError:
        return('The number is not in the Fibonacci Sequence.')
    return("\n".join(fib))
print(fibonacci())