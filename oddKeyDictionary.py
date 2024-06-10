input_dict = eval(input("Enter dictionary = "))
odd_key_dict = {}
for key,value in input_dict.items():
    if key%2 !=0:
        odd_key_dict[key]=value
    
print("Dictionary with odd keys = ",odd_key_dict)