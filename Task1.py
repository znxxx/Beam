parenInput =input()
paren = {"(":")", "[":"]", "{":"}"}
#check length
if len(parenInput)%2==1:
    print ("false")
else:
    #push open bracket into stack list
    stack = []
    for x in parenInput:
        #Open bracket
        if x == "(" or x =="{" or x == "[":
            stack.append(x)
        else:
            #x is the close bracket
            #if the stack is empty, that mean there is no way there are pair for x
            if stack == []:
                print("false")
                break
            #pop latest open bracket appended(suppost to be it's pair) and check if they're matched
            openbracket = stack.pop()
            if x != paren[openbracket]:
                print("false")
                break
        #the stack must be empty from popping, and the x must be the last one(stack can be empty whether
        # or not the string is completely iterated.)
        if stack == [] and x == parenInput[-1]:
            print("true")


    