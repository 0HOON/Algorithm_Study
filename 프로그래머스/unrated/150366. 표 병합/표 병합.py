# dict
# (r, c): [merge, value]
#   merge: [자기 좌표] / [(r, c)...]
#   value: '' / str

def update(table, args):
    if len(args) == 3:
        r, c, value = args
        r = int(r)
        c = int(c)
        if table.get((r, c)) == None:
            table[(r, c)] = [[(r, c)], value]
        else:
            for cell in table[(r, c)][0]:
                table[cell][1] = value
                
    elif len(args) == 2:
        v1, v2 = args
        for k, v in table.items():
            if v[1] == v1:
                table[k][1] = v2
    else: 
        print("ERROR: wrong # of args for UPDATE")
        
def merge(table, args):
    r1, c1, r2, c2 = list(map(int, args))
    cell1 = table.get((r1, c1), None)
    cell2 = table.get((r2, c2), None)
    if cell1 == None and cell2 == None:
        # 둘 다 없음
        if (r1, c1) == (r2, c2):
            # 같으면 무시
            return
        else:
            new_val = [[(r1, c1), (r2, c2)], 0]

    elif cell1 != None and cell2 != None:
        # 둘 다 존재
        if cell1[0] == cell2[0]:
            # 같은 그룹 / 셀
            return
        else:
            # 다른 그룹 / 셀
            if cell1[1] == 0:
                new_val = [cell1[0] + cell2[0], cell2[1]]
            else:
                new_val = [cell1[0] + cell2[0], cell1[1]]
        
    elif cell1 != None and cell2 == None:
        # cell1만 존재
        new_val = [cell1[0] + [(r2, c2)], cell1[1]]
        
    elif cell1 == None and cell2 != None:
        # cell2만 존재
        new_val = [cell2[0] + [(r1, c1)], cell2[1]]
        
    else:
        print("ERROR: MERGE")
    for cell in new_val[0]:
        table[cell] = new_val
    
    
def unmerge(table, args):
    r, c = list(map(int, args))
    cell = table.get((r, c))
    if cell == None:
        print("ERROR: There's no such cell to UNMERGE")
    else:
        v = cell[1]
        for cc in cell[0]:
            table.pop(cc, None)
        if v != 0:
            table[(r, c)] = [[(r, c)], v]

def print_cell(table, args):
    r, c = list(map(int, args))
    cell = table.get((r, c), None)
    if cell == None:
        return "EMPTY"
    elif cell[1] == 0:
        return "EMPTY"
    else:
        return cell[1]
        
def solution(commands):
    answer = []
    table = {}
    for command in commands:
        c = command.split()
        args = c[1:]
        c = c[0]
        if c == "UPDATE":
            update(table, args)
        elif c == "MERGE":
            merge(table, args)
        elif c == "UNMERGE":
            unmerge(table, args)
        elif c == "PRINT":
            answer.append(print_cell(table, args))
        else:
            print("ERROR: Unkown Command")
    return answer