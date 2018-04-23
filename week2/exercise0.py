
def add_5(a_number):
   a_number= 5
    return a_number + 10

print (add_5(0))



def adder(a_number, another_number):
    a_number = 10
    another_number = 10
    return a_number + another_number

print (adder(0,0))


    
def shout(a_string):
    a_string = 'HELLO'
    return a_string

    
print (shout(0))

def really_shout(a_string,exc_point):
   
    a_string = 'HELLO'
    exc_point = '!'
    return a_string + exc_point



    
print (really_shout(0,0))



def shout_with_a_number(a_string, a_number):
    """Return a string in uppercase with a space and a_number concatentated.
    E.g.
    >>> shout_with_a_number('hello', 42)
    'HELLO 42'

    HINT: Lookup how to cast a_number to a string or lookup how to use f-strings in python
    """
    a_string = 'please work, i want to get this '
    a_string.upper()
    a_number = '123'
    
    return a_string + a_number

print (shout_with_a_number(0,0))
    


def minitest(f, args, expected):
    """Run a function with a list of args and print a response.

    This is a helper. Don't edit it.
    """
    result = f(*args)
    template = "expect {name}({args}) == {expected} => {result}"
    print(template.format(name=f.__name__,
                          args=str(args)[1:-1],
                          result=result == expected,
                          expected=expected))
    return result == expected


if __name__ == "__main__":
    minitest(add_5, [1], 6)
    minitest(add_5, [6], 11)
    minitest(add_5, [-3], 2)
    minitest(add_5, [0.5], 5.5)
    minitest(adder, [-0.5, -0.5], -1)
    minitest(adder, [2, 2], 4)
    minitest(adder, [2, -2], 0)
    minitest(shout, ["hello"], "HELLO")
    minitest(really_shout, ["hello"], "HELLO!")
    minitest(really_shout, [""], "!")
    minitest(really_shout, ["!"], "!!")
    minitest(shout_with_a_number, ('hello', 42), "HELLO 42")
    print("""
          This section does a quick test on your results and prints them nicely
          It's NOT the official tests, they are in tests.py as usual.
          Add to these tests, give them arguments etc. to make sure that your
          code is robust to the situations that you'll see in action.

          REMEMBER: these aren't the tests that you submit, these are just
          there to keep you sane.""")
