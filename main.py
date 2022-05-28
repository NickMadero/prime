#checking if a number is prime

user = int(input("enter a number: "))
if user > 1 :

    for x in range(2,user):
     if ( user % x ) == 0:
         print(user,"is not a prime number sorry ")
         break
    else:
        print(user," is a prime number")
