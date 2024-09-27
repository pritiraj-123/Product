n=int(input('enter:'))
if n%2==0:
    print("even")
else:
    print("add")


def palindrome(word):
    return word==word[::-1]


def square_n_cube(num):
    return num**2,num==3
