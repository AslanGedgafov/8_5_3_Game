a={"cap_a":8}
b={"cap_b":5}
c={"cap_c":3}
for key, value in a.items():
    def_a = value
for key, value in b.items():
    def_b = value    
for key, value in c.items():
    def_c = value    

print(f"You have an {def_a} litre jug full of water and two smaller jugs are empty,\nOne that contains {def_b} litres and the other {def_c} litres. \nNone of the jugs have markings on them, nor do you have any additional measuring device.\nYou have to divide the 8 litres of water equally between your two best friends, \nso that each gets 4 litres of water. How can you do this?")

#----------User input treatment section -----------------------

def func():  # Check if input is there integer 
    choice = "Wrong"
    while choice.isdigit()==False :
        choice = input("Enter a single number: ")

        if choice.isdigit()==False:
            print("Wrongly entered: ")
        else:
            return int(choice)

def user():
    user_in = []
    while len(user_in) < 3: 
        user_in.append(func()) 

    return user_in

#print(user())

# ------ Winning Combinations & Ded End Combinations 
win = [[8,0,0],[3,5,0],[3,2,3],[6,2,0],[6,0,2],[1,5,2],[1,4,3],[4,4,0]]
ded_end = [[5,0,3],[0,5,3],[],[],[],[],[],[],[]]
print(win[0])

# need to find out how check the tipe of an input()

#iterate throue the nested list and compare it with the input

"""user_in_storage = []
user_lst = user()"""

# comparing input and win list
def in_nested_list(my_list, item):
    
    if item in my_list:
        return True
    else:
        return any(in_nested_list(sublist, item) for sublist in my_list if isinstance(sublist, list))
"""
print(in_nested_list(win, user_lst))
print(user_in_storage)
"""


# MISTAKE call 2 times function USER()
def engin(user_in, win_lst):
    user_in_storage = []
    while user != win_lst:  
        user_lst = user_in
    
        print(in_nested_list(win, user_lst))
        user_in_storage.append(user_lst)
        print(user_in_storage)
    
        if user_in == user_lst:
            break

    print("You Win!")


print(engin(user(), win[-1]))



