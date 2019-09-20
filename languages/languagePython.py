

if __name__ == "__main__":
    #take input while End of File
    while True:
        try:
            n = input()
        except EOFError:
            break

    # take space separated int inputs

    while True:
        try:
            inputs = input()
        except EOFError:
            break
        n,m = list(map(int, inputs.split()))

        if n == 0 and m == 0:
            break

    # file I/O
    import sys 
    # For getting input from input.txt file 
    sys.stdin = open('input.txt', 'r')  
      
    # Printing the Output to output.txt file 
    sys.stdout = open('output.txt', 'w')

    pass


## copy a list into another
list_b = list_a.copy();

## logical AND/OR/NOT

#- a and b
#- a or b
#- not a

## check if all passes a condition
maxi = max(nums);
        
if all(maxi >= 2 * x for x in nums if x != maxi):
    return nums.index(maxi)