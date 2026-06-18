set_of_num = {1,2,3,45,5,3,3,3,2,2,2,1,1,1,4,4,5,65,2,3,4,5,6,7,8,9,10}
print(type(set_of_num))  # This will print <class 'dict'> because {} creates an empty dictionary, not a set
print("set_of_num:", set_of_num)  # This will print the unique elements in the set, duplicates are removed


set_1 = {1, 2, 3, 4, 5,22,3,4,6,7,4,3,5,6,7,8,9,10}
set_2 = {4, 5, 6, 7, 8, 9,10,11,12,13,14,15,22,44,6,3,8,9,10,11,12,13,14,15}
print("Intersection:", set_1.intersection(set_2))  # This will print the intersection of set_1 and set_2, which is a new set containing only the elements that are in both sets
print("Union:", set_1.union(set_2))  # This will print the union of set_1 and set_2, which is a new set containing all unique elements from both sets

list_of_envs = ["dev", "prod", "staging", "qa", "uat", "dev", "prod", "staging", "qa", "uat"]
print("list_of_envs:", list_of_envs)  # This will print the original list with duplicates
list_of_envs = list(set(list_of_envs))  # This will create a set from the list, removing duplicates
print("list_of_envs:", list_of_envs)  # This will print the original