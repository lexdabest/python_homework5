flag = False
for i in range(1,101): 
    for j in range(2,i):
        if i%j == 0:
            flag = True
            break
        else:
            flag = False
    if flag == False and i!=1:
        print("Prime") 
    else:
        fizz = i%3
        buzz = i%5
        if fizz == 0 and buzz == 0:
            print("FizzBuzz")
        elif fizz == 0:
            print("Fizz")
        elif buzz == 0:
            print("Buzz")
        else:
            print(i)
   
