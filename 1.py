import random
max_length = 6
digits = ['0','1','2','3','4','5','6','7','8','9']
character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','x','y','z']
combine_list = digits + character
temp = [random.choice(combine_list) for item in range(max_length)]
emp_code = ""
for element in temp:
    emp_code+=element
emp_id = emp_code
print(emp_id)    


