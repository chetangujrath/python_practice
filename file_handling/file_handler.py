file_obj = open('my_file.txt','r') #open

print(file_obj.readlines()) #process
file_obj.close() #close


try:
    file_obj_new = open('my_file_new.txt','r') #open
except:
    print("error handling")
    file_obj_new = open('my_file_new.txt','w+') #open
    file_obj_new.read() #process
finally:
    file_obj_new.close() #close