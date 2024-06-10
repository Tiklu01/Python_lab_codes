def count_vowels(input_string):
    count = 0
    vowels = "aeiouAEIOU"
    for char in input_string:
        if char in vowels:
            count+=1
    return count
input_string = input("Enter a string = ")
print(f"the no of voewls in {input_string} is {count_vowels(input_string)}")