def getEvenSet(num):
    even_set = set()
    for n in num:
        if n%2 == 0:
            even_set.add(n)
    return even_set
og_set = eval(input("Enter a set of integers = "))
print(getEvenSet(og_set))