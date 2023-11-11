import random

'''
This program illustrates the three ways to solve the following problem:

The King of a small country invites 1000 senators to his annual party.
As a tradition, each senator brings the King a bottle of wine. Soon after,
the Queen discovers that one of the senators is trying to assassinate the
King by giving him a bottle of poisoned wine. Unfortunately, they do not
know which senator, nor which bottle of wine is poisoned, and the poison
is completely indiscernible. However, the King has 10 prisoners he plans
to execute. He decides to use them as taste testers to determine which
bottle of wine contains the poison. The poison when taken has no effect
on the prisoner until exactly 24 hours later when the infected prisoner
suddenly dies. The King needs to determine which bottle of wine is poisoned
by tomorrow so that the festivities can continue as planned. Hence, he only
has time for one round of testing. How can the King administer the wine to
the prisoners to ensure that 24 hours from now he is guaranteed to have
found the poisoned wine bottle?
'''

# generate bottles
L = list(range(0, 1000))
poisoned = random.randint(0, 1000)


def get_state_after_drinking(l):
    if (poisoned>=l[0]) and (poisoned<=l[-1]):
        return 'DEAD'
    return 'ALIVE'


def assign_bottles(num_prisoners, bottles):
    groups = []
    p_bottles = int(len(bottles)/(num_prisoners+1))
    if p_bottles == 0:
        for b in bottles:
            if b == poisoned:
                return [b]
    print('bottles per prisoner:', p_bottles)
    for n in range(num_prisoners):
        groups.append(bottles[n*p_bottles:(n+1)*p_bottles])
    invis_bottles = bottles[num_prisoners*p_bottles:]
    groups.append(invis_bottles)
    return groups


def get_poison_group(bottles):
    for group in bottles:
        state = get_state_after_drinking(group)
        if state == 'DEAD':
            print('dead prisoner:', bottles.index(group))
            return bottles.index(group)


def print_update(bot, pri, day):
    print('remainding bottles:', len(bot), bot)
    print('prisoners alive:', pri)
    print('day', day, 'end\n')


def divide_conquer():  # takes 3 days
    daynl = L
    prisoners_alive = 10
    day = 0

    while len(daynl) > 1:
        groups = assign_bottles(prisoners_alive, daynl)
        print_update(daynl, prisoners_alive, day)
        if len(groups) == 1:
            daynl = groups
            break
        poison_group_index = get_poison_group(groups)
        daynl = groups[poison_group_index]
        if poison_group_index < len(groups) - 1:
            # one of the prisoners died
            prisoners_alive -= 1
        day += 1
    print_update(daynl, prisoners_alive, day)  # last remaining bottle. poisonous bottle


def three_digit():  # takes 2 days
    dead = []
    for bottle in L:
        # set up
        bottle_str = str(bottle)
        if bottle < 10:
            b_digits = [0, 0, bottle]
        elif bottle < 100:
            b_digits = [0, int(bottle_str[0]), int(bottle_str[1])]
        else:
            b_digits = [int(bottle_str[0]), int(bottle_str[1]), int(bottle_str[2])]

        # prisoners sip bottles if their digit is contained in the bottle
        for dig in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if dig in b_digits:
                # drink
                if bottle == poisoned:
                    dead.append(dig)

    print('Dead prisoners:', dead)

    # find possible bottles
    if len(dead) == 1:
        possibles = [dead[0]*111]
    elif len(dead) == 2:
        possibles = [dead[0]*100+dead[0]*10+dead[1],
                     dead[0]*100+dead[1]*10+dead[0],
                     dead[1]*100+dead[0]*10+dead[0],
                     dead[1]*100+dead[1]*10+dead[0],
                     dead[1]*100+dead[0]*10+dead[1],
                     dead[0]*100+dead[1]*10+dead[1]]
    else:  # 3 digits
        possibles = [dead[0] * 100 + dead[1] * 10 + dead[2],
                     dead[0] * 100 + dead[2] * 10 + dead[1],
                     dead[1] * 100 + dead[0] * 10 + dead[2],
                     dead[1] * 100 + dead[2] * 10 + dead[0],
                     dead[2] * 100 + dead[0] * 10 + dead[1],
                     dead[2] * 100 + dead[1] * 10 + dead[0]]

    print('Possible poisonous bottles:', possibles)
    print('day 1 end')

    # 7 prisoners alive. maximum 6 bottles remaining
    for b in possibles:
        if b == poisoned:
            print('Found poisoned bottle:',b)

    print('day 2 end')


print('correct poisoned:', poisoned)


def dectobinary(num):
    if num <= 1:
        return num
    else:
        return [dectobinary(num // 2), (num % 2)]


def binary_digit():  # takes 1 day
    dead = []
    for bottle in L:
        # set up
        binstr = (bin(bottle))[2:]
        b_digits = []
        for char in binstr:
            b_digits.append(int(char))
        curlen = len(b_digits)
        zeros = 10 - curlen
        new_bdigits = [0]*zeros + b_digits
        # prisoners sip bottles if their digit is contained in the bottle
        for dig_index in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if new_bdigits[dig_index] == 1:
                # drink
                if bottle == poisoned:
                    dead.append(dig_index)
    print('Dead prisoners:', dead)
    d = {0:'0', 1:'0', 2:'0', 3:'0', 4:'0', 5:'0', 6:'0', 7:'0', 8:'0', 9:'0'}
    for p in dead:
        d[p] = '1'
    binlist = d.values()
    print(binlist)
    pbinstr = ''
    for c in binlist:
        pbinstr += c
    pdec = int(pbinstr, 2)
    print(pdec)


binary_digit()