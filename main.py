row = int(input())
list_sits = [list(input()) for _ in range(row)]
people_group = int(input())
list_req = [input().split() for _ in range(people_group)]
trans = {0: 'A', 1: 'B', 2: "C", 4: 'D', 5: 'E', 6: 'F'}
for i in range(people_group):
    amt = int(list_req[i][0])
    side = list_req[i][1]
    req = list_req[i][2]
    if side == 'left':
        if req == 'window':
            l, r = 0, amt
        else:
            l, r = 3 - amt, 3
    else:
        if req == 'window':
            l, r = 7 - amt, 7
        else:
            l, r = 4, 4 + amt
    ticet_list = ''
    for j in range(row):
        for s in range(l, r):
            if list_sits[j][s] != '.':
                break
        else:
            for s in range(l, r):
                list_sits[j][s] = 'X'
                ticet_list += f'{j + 1}{trans[s]} '
            print(f'Passengers can take seats: {ticet_list.strip()}')
            for j_row in list_sits:
                print(''.join(j_row))
            for s in range(l, r):
                list_sits[j][s] = '#'
            break
    else:
        print('Cannot fulfill passengers requirements')
