qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?",
      "What did you eat today?"]
n = 0
while True:
    print("Type q to quit")

    a = input(qs[n])
    if a == "q":
        break
    n = (n+1) % 4

n is an index variable. Each time around the loop, you assign n to the evaluation of the expression (n + 1) % 3, which enables you to cycle indefinitely through every question in your qs list. The first time around the loop, n starts at 0. Next, n is assigned the value of the expression (0 + 1) % 3, which evaluates to 1. Then, n is assigned to the value of (1 + 1) % 3, which evaluates to 2, because whenever the first number in an expression using modulo is smaller than the second, the answer is the first number. Finally, n is assigned the value of (2 + 1) % 3, which evaluates back to 0.

Althoff, Cory. The Self-Taught Programmer: The Definitive Guide to Programming Professionally (pp. 110-111). Triangle Connect


