import pdb

def addition(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def dividing(x,y):
    return x/y
def searching(string):
    temp=""
    fnum=""
    for i in string:
        if i.isdigit():
            if fnum==temp:
                fnum=i
            else:
                lnum=i
    return fnum,lnum
    
add_tuple=('add','addition','+','sum','plus','added')
substraction_tuple=('sub','minus','-','substract','difference','substracted')
multiplication_tuple=('multiply','multiplication','product','into','*','multiplied')
divide_tuple=('divide','division','/','divided')
print("HELLO!!!!\nI'M GRAFFITI (THE CALCULATING ROBOT)\nBRING YOUR PROBLEM\nI'M SMART CALCULATOR")
while True:
    user=input("\nEnter the text: ")
    if user=="exit" or user=="Exit" or user=="EXIT":
        print("Thankyou for using...")
        break
    else:
        user1=user.split()
        for use in user1:
            if use in add_tuple:
                first_num,last_num=searching(user1)
                print(f"SUM : {addition(int(first_num),int(last_num))}\nPrint Exit to terminate")
                break
            elif use in substraction_tuple:
                first_num,last_num=searching(user1)
                print(f"SUBSTRACTION : {substraction(int(first_num),int(last_num))}\nPrint Exit to terminate")
                break
            elif use in multiplication_tuple:
                first_num,last_num=searching(user1)
                print(f"MULTIPLICATION : {multiplication(int(first_num),int(last_num))}\nPrint Exit to terminate")
                break
            elif use in divide_tuple:
                first_num,last_num=searching(user1)
                print(f"DIVISION : {dividing(int(first_num),int(last_num))}\nPrint Exit to terminate")
                break
    
