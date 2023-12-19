hs = int(input("Harmonic step 1 - "))
x = 1

while x <= hs:
    
    def limit(x):
        if x < 2:
            return 1
        else:
            return 1 / x + (limit(x - 1))
             
    print("Limit = ", x,"Value = ", limit(x))
    x += 1