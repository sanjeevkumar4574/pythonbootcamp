from art import logo2




def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

# if operator=='+':
#     print(add(a=get1,b=get2))
# elif operator=='-':
#     print(subtract(a=get1,b=get2))
# elif operator == '*':
#     print(multiplication(a=get1,b=get2))
# else:
#     print(division(a=get1,b=get2))


dict_calcute={
    '+':add,
    '-':subtract,
    '*':multiplication,
    '/':division
}



def calculate():
    print('Welcome to python calulator.')
    print(logo2)


    get1 = int(input('enter first number\n'))
    for i in dict_calcute:
        print(i )
    should_count = True
    while should_count:
        operator = input('choose operator:')
        get2 = int(input('enter next number\n'))
        fun = dict_calcute[operator]
        result1 = fun(get1,get2)
        print(f"{get1} {operator} {get2} = {result1}")

        if input(f"type 'y' to continu with {result1} or 'n' for new calculations .") =='y':
            get1 = result1

        elif input(f"type 'y' to continu with {result1} or 'n' for new calculations .")=='n':
            should_count=False
            calculate()

        else:
            break


calculate()
