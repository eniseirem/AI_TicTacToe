import random
places = {
        0: ['1', '5', '9'],
        1: ['7','8','9'],
        2: ['4','5','6'],
        3: ['1','2','3'],
        4: ['4','7','1'],
        5: ['8','5','2'],
        6: ['9','6','3'],
        7: ['7','5','3'],
    }

def ai(vals):
    v= vals
    a = []
    a.append(int(v['1']+v['5']+v['9']))     # 0 dia
    a.append(int(v['7']+v['8']+v['9']))     # 1
    a.append(int(v['4']+v['5']+v['6']))     # 2
    a.append(int(v['1']+v['2']+v['3']))     # 3
    a.append(int(v['4']+v['7']+v['1']))     # 4
    a.append(int(v['8']+v['5']+v['2']))     # 5
    a.append(int(v['9']+v['6']+v['3']))     # 6
    a.append (int(v['7']+v['5']+v['3']))    # 7 dia


    for id, el in enumerate(a):
        if el == 6 or el == 10:
            search = places[id]
            for i in search:
                if v[str(i)] == 0:
                    return i
        elif v['5']==0:
            return 5

    if 11 in a and 13 in a:
        m = range(1,9)
        return random.choice(m)

    elif v['5']==3 or v['5']== 5:
        corners=[1,3,7,9]
        return random.choice(corners)


