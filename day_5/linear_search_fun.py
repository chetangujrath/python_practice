
def linear_search(list_of_env,key):
    is_found = False
    for env in list_of_env:
        if env == key:
            is_found = True
    return is_found