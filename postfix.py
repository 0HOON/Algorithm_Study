#1918 후위표기식 골드3

def post():
    temp1 = a.pop()
    temp2 = a.pop()
    a.append(temp2 + temp1 + o.pop())

infix = input()
a = []
o = []

for i in infix:
    if i.isalpha():
        a.append(i)
    if i == '(':
        o.append(i)
    if i == ')':
        while o[-1] != '(':
            post()
        o.pop()
    if i == '+' or i == '-':
        while len(o) > 0 and o[-1] != '(':
            post()
        o.append(i)
    if i == '*' or i == '/':
        if len(o) > 0 and (o[-1] == '*' or o[-1] == '/'):
            post()
        o.append(i)

while len(a) > 1:
    post()

print(a[0])