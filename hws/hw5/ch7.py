""" Dallas Hays
    2/16/15
    Homework 1
    Exercise 7.4
"""

# Exercise 7.4
# Uses raw_input to request input from the user to be evaluated. Prints
# the result. If the user types in 'done' then the function will end
# and return the last value of result. Result defaults to 0.0 in case
# the first input is done.
def eval_loop():
    print "Evaluate an expression, type 'done' to end."
    result = 0.0
    while(True):
        equation = raw_input("What do you want to evaluate? ")
        if equation == 'done':
            return result
        else:
            result = eval(equation)
            print result

def main():
    eval_loop()

if __name__ == "__main__":
    main()
