# try and except

# if an error is encounterd, a try block code execution is stopped and...
# transferred down to the except block

# use try and except for runtime errors

# example - divide by zero

def meanUser(num, denominator):
    try:
        answer = num/denominator
        print(answer)
    except:
        print('bad user') # if you put bad code in your except statement...ERROR
    finally:
        print('hi there')

