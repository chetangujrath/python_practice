cloud_env = ["aws","azure","gcp","ibm"]
print("Display a single index provide is as follow : \n",cloud_env[1])
print("Display a single index provide is as follow : \n",cloud_env[-1])
print("Display a multiple range index provide is as follow : \n",cloud_env[1:3])

cloud_env[1] = "alibaba"
print("Updated list is as follow :\n",cloud_env)

num = [41,51,61,71,81,91,101]
print(num[4])

mix = [22,"aws",33,"rose",44,"gcp","azure",3.140]
print(mix[2:7])
print(mix)

data = ["Jatin",45,85.52,True]

name,age,marks,status = data
print("Name :",name)
print("Age : ",age)
print("Marks :",marks)
print("Maritial status :",status)