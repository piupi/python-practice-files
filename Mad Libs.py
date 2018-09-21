n1 = input("Enter a noun:")
v = input("Enter a verb:")
adj = input("Enter an adjective:")
n2 = input("Enter another noun:")

r = """The {} {} the {} {}
    """.format(n1,
               v,
               adj,
               n2)

print(r)

