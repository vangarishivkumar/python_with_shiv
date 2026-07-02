rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
####        rooms =20 each floor    | 15 floor each building | total 3 buildings
print(rooms,end='\n')
rooms[1][9][14] = True          # 2nd bulding,10th floor, 15th rooms is occupied/booked.
rooms[0][0][0] = True           # 1st building, 1st floor, 1st room is booeked.
print(rooms)

#############
