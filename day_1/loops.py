import time

print("*******1 . for loops********")
for i in range(0,21,2):
    print(i)

print("*******2 . while loops********")

i = 0
while i < 5 :
    i +=1 
    if i == 4:
        continue
    print(i) 

while True:
    time.sleep(2)
    print("hello")