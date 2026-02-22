fruits = ["mango", "apple", "banana", "oranges"]
print(fruits[0])

# x = int(input())

# if x < 0:
#     print("-ve")
# elif x > 0 and x < 10:
#     print("single digit")
# elif x >= 10 and x < 100:
#     print("double digit")
# elif x >= 100:
#     print("triple digit")

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end=" ")
        a, b = b, a + b

fib(2000)