# Q-⁠Display numbers at the odd indices of a list (starting index with 0)
l=eval(input("Enter a list:"))
print("Odd indexed of input list:")
for i in range(len(l)):
    if i%2!=0:
        print(l[i])