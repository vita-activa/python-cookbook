test="this is a strange test"

for i, c in enumerate(test):
    try:
        if i <10 and c=="i":
            print(i, c)
            continue
    except: #when there is an error
        print("what you expect")
    finally:
        print(i)

num=20

for i in range(10):
    try:
        res=num/i
        print(res)
    except ZeroDivisionError:
        print("ERORR")
