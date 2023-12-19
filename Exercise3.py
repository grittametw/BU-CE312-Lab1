max = int(input("Enter max value: "))
oeb = (input("Enter O/E/B (Odd or Even or Both): "))
pm = (input("Enter Y/N (onlyPrime?): "))

while max > 0:
    
    def check(max):
        if (max < 2):
            return (max % 2 == 0)
        return (check(max - 2))
        
    def Prime(max,Count):
        Status = True
        if Count == max:
                return True
        else:
                if max % Count == 0:
                        return False
                elif 1 % max == 0:
                        return Status
                else:
                        Count += 1
                        Status = (Prime (max,Count) and Status)
                        return Status
                    
    def Recursive(max):
            if Prime(max,2) == True:
                    return "is prime number"
            else:
                    return "is not prime number"        
    
    if oeb == 'O':
        if(check(max)==False):
            print("num", max, Recursive(max))
    if oeb == 'E':
        if(check(max)==True):
            print("num", max, Recursive(max))
    if oeb == 'B':
        if pm == 'Y':
            if Prime(max,2) == True:
                print("num", max, Recursive(max))
        else:
            if(check(max)==True):
                print("num", max, Recursive(max))
            else:
                print("num", max, Recursive(max))
    
    max -= 1