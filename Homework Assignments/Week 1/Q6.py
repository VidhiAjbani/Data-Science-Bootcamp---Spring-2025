# Q-⁠Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
n=20
for i in range(1,n+1):
    print(i, end=" : ")
    if i%2==0:
        print("Even")
    else:
        print("Odd")
