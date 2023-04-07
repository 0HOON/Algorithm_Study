from math import floor 

class Node():
    def __init__(self, name, children, parent):
        self.name = name
        self.children = children
        self.parent = parent
        self.profit = 0
        
    def add_child(self, child):
        self.children.append(child)
    
    def give_profit_to_parent(self, profit):
        if self.name == 'minho':
            return
        profit_to_parent = floor(profit * 0.1)
        self.profit += profit - profit_to_parent
        if profit_to_parent > 0:
            self.parent.give_profit_to_parent(profit_to_parent)
    
def solution(enroll, referral, seller, amount):
    member_dict = {en: Node(en, [], None) for en in enroll}
    center = Node('minho', [], None)
    for en, re in zip(enroll, referral):
        if re == '-':
            center.add_child(member_dict[en])
            member_dict[en].parent = center
        else:
            member_dict[re].add_child(member_dict[en])
            member_dict[en].parent = member_dict[re]

    for s, a in zip(seller, amount):
        member_dict[s].give_profit_to_parent(a*100)
    
    answer = [member_dict[en].profit for en in enroll]
    
    return answer