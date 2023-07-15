

def num_plus():
    try:
        until = int(input('''Choose a variant:
    (1) - How much calculations
    (2) - Until a number (info)-the string of numbers will do one more calculation above the maximum number, because it does one more calculation by default
    >>:'''))
    except ValueError:
        print(" You can't add a string, it have to be an integer!")
    if until == 1:
        unt0 = int(input('How much calculations:'))
        
        num1 = 1
        num2 = 2

        list = []
        list.append(num1)
        list.append(num2)
        i = 0
        
        
        for x in range(0, int(unt0)):
            i += 1
            num = int(list[-1]) + int(list[-2])
            list.append(num)
            print(num)
            if num == until:
                break
    if until == 2 :
        unt = int(input('Until what number: '))
        num1 = 1
        num2 = 2

        list = []
        list.append(num1)
        list.append(num2)
        i = 0
        stat = True
        
        
        while stat == True:
            i += 1
            num = int(list[-1]) + int(list[-2])
            list.append(num)
            print(num)
            if num >= unt:
                stat = False
        

num_plus()
        
