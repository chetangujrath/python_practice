list_of_env = ["dev", "prod", "staging", "qa", "uat" , "test"]
list_of_num = [ 1,2,3,45,5,3,3,3,2,2,2,1,1,1,4,4,5,65,2,3,4,5,6,7,8,9,10]

key =   "test"
is_key_present = False
for env in list_of_env:
    if env == key:
        is_key_present = True
       
if is_key_present:
    print("Found")
else:
    print("Not Found")       

num = 95
is_num_present = False
for n in list_of_num:
    if n == num:
        is_num_present = True

if is_num_present:
    print("Found")
else:
    print("Not Found")