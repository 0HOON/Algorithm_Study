# 거짓말 1043 골드4
inputstr = input()
N, M = list(map(lambda x: int(x), inputstr.split()))

inputstr = input()
know = []
input2 = inputstr.split()
if len(input2) > 1:
    know = input2[1:]

member = []
for i in range(M):
    input_party = input()
    input_party = input_party.split()
    member.append(input_party[1:])

know = set(know)
new_know = know
while True:
    for i in list(know):
        for j in range(len(member)-1, -1, -1):
            if i in member[j]:
                new_know = new_know | set(member[j])
                del member[j]
                
    
    if new_know == know:
        break
    know = new_know

print(len(member))