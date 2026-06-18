dict_of_item_1 = {
    "env": "dev",
    "server": "AWS cloud",
    "ram" :  "16GB" ,
    "cpu" : "8 vCPU",
    "port" : 8080,
    "active" : True
}
dict_of_item_2 = {
    "env": "prod",
    "server": "Azure cloud",
    "ram" :  "32GB" ,
    "cpu" : "16 vCPU",
    "port" : 8080,
    "active" : False
}
dict_of_item_3 = {
    "env": "staging",
    "server": "GCP cloud",
    "ram" :  "64GB" ,
    "cpu" : "32 vCPU",
    "port" : 8080,
    "active" : True
}

env_details = [dict_of_item_1, dict_of_item_2, dict_of_item_3]
print ("active env details +++++++++++++++++++++++++++++++++++++++++\n")
for env in env_details:
    for key,value in env.items():
            if key == "active" and value:
                  print(env.values())
                  print("\n")
                
print ("inactive env details +++++++++++++++++++++++++++++++++++++++++\n")
for env in env_details:
    for key,value in env.items():
            if key == "active" and value == False:
                  print(env.values())                  