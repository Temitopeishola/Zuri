import random
choices=['r','p','s']
user=input('Choose an option (r,p,s): ')

if user in choices:
    cpu=random.choice(choices)
    print('CPU input =',cpu)
    if user==cpu:
        print('Draw')
    elif user=='r':
        if cpu=='p':
            print('cpu won!')
        else:
            print('user won!')
    elif user=='p':
        if cpu=='r':
            print('user won!')
        else:
            print('cpu won!')
    elif user=='s':
        if cpu=='p':
            print('user won!')
        else:
            print('cpu won!')
    else:
        print('wrong input')
    

    

    

        
        

