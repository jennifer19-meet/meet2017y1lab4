speed= 50
is_birthday = False

if is_birthday == False:
    if speed < 31:
        print('no ticket')
    elif speed > 30 and speed < 51:
        print('small ticket')
    elif speed > 50:
        print('big ticket')
if is_birthday == True:
    if speed < 36:
        print('no ticket')
    elif speed > 35 and speed < 56:
        print('small ticket')
    elif speed > 55:
        print('big ticket')
