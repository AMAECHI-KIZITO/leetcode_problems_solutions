""" Problem 193. Valid Phone Numbers """
with open('phoneno.txt','r') as file:
    content=file.readlines()
    for phone_num in content:
        if phone_num.startswith('(') or '-' in phone_num:
            print(phone_num)
