# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""




def lone_ranger(start, stop, step):
    
    a = range(2)
    for i in range(0,20,2):
        return a

print(lone_ranger(0,0,0))

def loop_ranger(number_number_list):
    yep=[]
    for i in range(4):
       yep.append(i)

    return yep

print(loop_ranger(10))

   
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """


def loop_ranger(number_number_list):
    yep=[]
    for i in range(10):
       yep.append(i)

    return yep[1:5]

print(loop_ranger(5))
   
    """Duplicate the functionality of range.
    Look up the docs for range() and wrap it in a 1:1 way
    """


def two_step_ranger(start, stop):
 
    yep=[]
    for i in range(0,20,2):
       yep.append(i)

    return yep[1:5]

print (two_step_ranger(0,0))
 
 
 
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """


def gene_krupa_range(start, stop, even_step, odd_step):
    odd_numbers = []
    even_numbers = []
    for i in range(0,20,2):
        even_numbers.append(i)
        
    for i in range (0,20,3):
        odd_step.append(i)
        
        return even_numbers
    
print (gene_krupa_range(1,10,2,3))
   
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    pass


    
def stubourn_asker(high = 20, low = 4):
    while True:
        print("Tell me a number")
        number = input()
        if int(number) > 4 and int(number) < 20 :
            print("cool man")
            break
        else:
            print("guess again chump")
            print()
            

stubourn_asker()

    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
  


def not_number_rejector(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("thats a not a INT Number!!!!")
       continue
    else:
       return userInput 
       break 
     
number = inputNumber("give me a number, bru:")

def super_asker(low = 4, high = 20):
    print ("guess me a number")
    while True:
        number = input()
        try :
            num = int(number)
            if num > 4 and num < 20 :
                print ("yeh you did it buddy")
                break  
            else:
                print("try again, thats a number tho")
        except ValueError :
            print ("thats not a number!!")
        

         
        
super_asker()


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
