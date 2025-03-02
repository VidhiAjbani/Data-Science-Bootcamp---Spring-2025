# Q- ⁠Display Fibonacci Series upto 10 terms (starting with 0)

def fibonacci(n):
    n1=0
    print(n1, end=" ")
    if n>1:
        n2=1
        print(n2, end=" ")
        if n>2:
            for i in range(2,n):
                n3=n1+n2
                print(n3, end=" ")
                n1=n2
                n2=n3

# main
num=int(input("Enter number of terms in fibonacci series:"))
while num<=0:
    print("invalid input")
    num=int(input("Enter number of terms in fibonacci series:"))
fibonacci(num)
