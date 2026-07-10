rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
####        rooms =20 each floor    | 15 floor each building | total 3 buildings
print(rooms,end='\n')
rooms[1][9][14] = True          # 2nd bulding,10th floor, 15th rooms is occupied/booked.
rooms[0][0][0] = True           # 1st building, 1st floor, 1st room is booeked.
print(rooms)

#############
########## vacancy check code
vacancy = 0
### check vacancy in 3rd building 15th floor 

rooms[0][0][0] = True
rooms[0][0][2] = True
rooms[0][0][3] = True
rooms[1][1][2] = True
rooms[2][2][2] = True
rooms[2][2][4] = True
print(rooms)
print('Enter below details to check vacancy.')
b=int(input('Enter a buidling Number : '))
f= int(input('Enter floor number: '))
#r=int(input('Enter a room number: '))
for room_number in range (20):
    if not rooms[b-1][f-1][room_number]:
        vacancy += 1
    #print(rooms[b][f][room_number])
print('there are in ',vacancy ,' Vancancies in building no. ',b,' on ',f,' floor...Thank you :)',sep='')

vac=0
vac_list=[]
for bd in range(3):
    for fl in range(15):
        for room_no in range(20):
            if not rooms[bd][fl][room_no]:
                vac += 1
                vac_list = vac_list.append(rooms[bd][fl][room_no])
print('total vacancy in all building is : ',vac)
print('list is:',vac_list)
