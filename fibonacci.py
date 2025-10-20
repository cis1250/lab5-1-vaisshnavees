#!/usr/bin/env python3
# Fibonacci Sequence Exercise
def get_fibonacci_input(): #changing  def main
    # making sure the input is a positive integer
    while True:
        user_input = input("How many terms of the Fibonacci sequence do you want? ")
        if user_input.isdigit():
            n = int(user_input)  # converting string to integer
            if n > 0:
                return n # channig break to return for valid input
            else:
                print("Please enter a positive integer.")
        else:
            print("Please enter a positive integer.")
    
    # print Fibonacci sequence using a for loop
  def generate_fibonacci_sequencce(n): #sequence to n terms thats why its added
    if n == 1:
        # if user wants 1 term print 1
        return[0] #taking print out and putting return to give user 1 term
    elif n == 2:
        #if user want 2 terms
        return[0,1]
    else:
        # for more terms useing the for loop
        fib_sequence = [0, 1] #showing the first fibnacci numbera
        
        # showing the remaining terms 
        for i in range(2, n):
            next_term = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_term)  # adding a new term

        return fib_sequence # adding return to give value

        def print_fibonacci_sequence(fib_sequence):#for a readable format
        # making sure all numbers are turned to strings to get an output
        print(" ".join(str(term) for term in fib_sequence))

def main(): #adding new main
    n= get_fibonacci_input()#input from user
fib_sequence = generate_fibonacci_sequence(n)#generating fib sequnece
print_fibonacci_sequence(fib_sequence)#print result
# to run the progam
if __name__ == "__main__":
    main()
