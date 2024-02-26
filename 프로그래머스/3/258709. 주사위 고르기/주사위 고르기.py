from itertools import combinations, accumulate
from collections import deque

class Dice():
    def __init__(self, dice=None, nums=None, counts=None):
        self.dice = dice
        
        if counts is None:
            counts = {}
            for d in dice:
                counts[d] = counts.get(d, 0) + 1

            self.nums = list(set(dice))
            self.counts = counts
            #[counts[n] for n in self.nums]
        else:
            self.nums = sorted(nums)
            self.counts = counts


def dice_sum(a, b):
    new_nums = set([])
    new_counts = {}
    for aa in a.nums:
        for bb in b.nums:
            new_nums.add(aa+bb)
            new_counts[aa+bb] = new_counts.get(aa+bb, 0) + (a.counts[aa] * b.counts[bb])
    return Dice(nums=list(new_nums), counts=new_counts)
        

def get_sum(dice_list):
    tmp = dice_list[0]
    for d in dice_list[1:]:
        tmp = dice_sum(tmp, d)
    #print('###')
    #print(tmp.nums)
    #print([tmp.counts[n] for n in tmp.nums])
    return tmp

def get_win_count(sum_a, sum_b):
    i = 0
    j = 0
    win_count = 0
    cum_a = list(accumulate([sum_a.counts[n] for n in sum_a.nums])) + [0]
    cum_b = list(accumulate([sum_b.counts[n] for n in sum_b.nums])) + [0]
    #print(cum_a, cum_b)
    for i, a in enumerate(sum_a.nums):
        for j, b in enumerate(sum_b.nums):
            if a <= b:
                win_count += cum_b[j-1] * sum_a.counts[a]
                break
            elif j == len(sum_b.nums)-1:
                win_count += cum_b[j] * sum_a.counts[a]
    
    return win_count

def solution(dice):
    answer = []
    dice = [Dice(dice=sorted(d)) for d in dice]
    best_win_count = 0
    
    for comb in combinations(range(len(dice)), len(dice)//2):
        #print('---------', comb)
        
        sum_a = get_sum([dice[i] for i in comb])
        sum_b = get_sum([dice[i] for i in range(len(dice)) if i not in comb])
        
        win_count = get_win_count(sum_a, sum_b)
        if best_win_count < win_count:
            best_win_count = win_count
            answer = comb
            
        #print(win_count)
            
    return [i+1 for i in answer]