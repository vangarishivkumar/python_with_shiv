print('         *** Welcome to collat\'z hypothesis ***') # welcome messge
count=0                                  # to maintaine count of steps
c0=int(input("Enter a number for collat'z hypothesis: "))       # prompt user to input a number
while c0 > 1:                            # run untill the c0 is > 1
    if ( c0%2 == 0 ) and ( c0 != 1 ):    # if given input c0 is even and not = 1
        c0/=2                            # evaluate new c0 as c0=c0/2
        print(int(c0))                   # print in to console as int becosed / operator gives float o/p
    elif c0%2 != 0:                      # otherwise if c0 is odd then
        c0=(3*c0)+1                      # evaluate new c0 as c0=3*co+1 and print on console
        print(int(c0))                   
    count+=1                             # keep track/count of every step(loop)
print('steps = ' ,count)                 # after all if c0 is < 1 then print count of loop.





print
(""""
1. Enter a number for collat'z hypothesis: 15
output:-
46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17
2. Enter a number for colla'z hypothesis: 16
output :
8
4
2
1
steps = 4
3. Enter a number for colla'z hypothesis: 1023
3070
1535
4606
2303
6910
3455
10366
5183
15550
7775
23326
11663
34990
17495
52486
26243
78730
39365
118096
59048
29524
14762
7381
22144
11072
5536
2768
1384
692
346
173
520
260
130
65
196
98
49
148
74
37
112
56
28
14
7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
steps = 62
""")
