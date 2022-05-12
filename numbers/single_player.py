
def MakeRules():
    global last_losing_number
    global one_step_max
    last_losing_number=int(input("What will be the losing number? "))
    one_step_max=int(input("Maximum numbers allowed at each step? "))

def next_losing_number(n):
    next_losing_number=last_losing_number
    while next_losing_number>n:
        next_losing_number-=(one_step_max+1)
    next_losing_number+=(one_step_max+1)
    return next_losing_number

def Play():
  
    last = 0
    
    while last<last_losing_number:
        
        if(next_losing_number(last)!=1):
            print("Okay. So, my number(s): ")
            for i in range(last+1,next_losing_number(last)):
                print(i)
        
        for x in input("Please, enter some number(s) separated by commas: ").split(','):
            last=int(x)
    
    print("\nSorry! You lose, I win.\n")

MakeRules()
Play()