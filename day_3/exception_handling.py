import builtins
list_of_clodes_env = ["aws", "azure", "gcp", "oracle", "ibm"]
try:
    print(list_of_clodes_env[7])
except:
    print("Index out of range")
finally:
    print("sab kuch chalenga yaha")


print(dir(builtins))