"""
template.py

A generic Python template. A starting place to do awesome things.

Developer  : Joe Graham <joe.w.graham@gmail.com>
Last update: 2018-06-27

It's always a good idea to document your code.
Start each file with some general information,
including your contact information.
"""

def hello(target="world"):
    """This function accepts a target and prints hello to that target.
       It's a good idea to document all functions. Not only does it 
       help other people, but also your future self."""

    output = "Hello " + target + "!"
    print(output)
    return output



if __name__ == "__main__":

    print()
    print("I ran from the command line.")
    hello()
    hello("OCNC 2018")
    hello(target="Okinawa")
    print()
