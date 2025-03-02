# Q- ⁠Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word):
    c=0
    vowels=['a','e','i','o','u']
    for a in word:
        if a.lower() in vowels:
            c+=1
    return c

#main
s=input("Enter a word:")
count=count_vowels(s)
print("Number of vowels in the input string: ",count)