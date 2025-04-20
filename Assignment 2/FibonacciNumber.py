arr = [0,1]
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<len(arr):
        return arr[n]
    else:
        for i in range(2,n+1):
            x = arr[i-1]+arr[i-2]
            arr.append(x)
        print(*arr[:n])

Fibonacci(8)