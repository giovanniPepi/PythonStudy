number = 0

while number <=100:

    if number % 3 == 0 and number % 5 == 0:
        print ("FizBuzz!")
        number += 1

    elif number % 3 == 0: 
        print("Fizz!")
        number += 1
   
    elif number % 5 == 0:
        print ("Buzz!")
        number += 1
        
    else:
        print (number)
        number += 1
     
for n in range (1,100):

    if n % 3 == 0 and n % 5 == 0:
        print ("1FizBuzz!")
    elif n % 3 == 0: 
        print("1Fizz!")   
    elif n % 5 == 0:
        print ("1Buzz!")
    else:
        print (n)


   
        



    
   

        
        