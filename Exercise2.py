while(1):
    y = input("Input Y to continue (N,Exit): ").upper().strip()
    if (y == "Y"):
            try:
                n = int(input("Input diamond size (odd number): "))

                def diamond(n):
                    star = 1
                    main = ''
                    try:
                        while (n%2 == 1) :
                            print("Diamond size = " + str(n))
                            for i in range(1,n+1):
                                string = ''
                                space = abs(i - int((n+1)/2))
                                star = n - 2 * space
                                string = space * ' ' + star * '*' + '\n'
                                main += string
                            return(main)
                    except:
                        print("error")

                print(diamond(n))

            except:
                print("error")

    elif (y == "N"):
        break