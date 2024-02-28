def solution(bandage, health, attacks):
    answer = 0
    time = 0
    hp = health
    t, x, y = bandage
    for at, dmg in attacks:
        hp += ((at-time-1)//t)*y + (at-time-1)*x
        if hp > health:
            hp = health
        hp -= dmg
        if hp <= 0:
            return -1
        time = at
    return hp