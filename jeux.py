import random


# [00,01 pour le 0,01 pour le 1, 11]

gains = [random.randint(50,250),random.randint(-50,100),random.randint(100,250),random.randint(-100,50)]

res_1 = 0
res_2 = 0


def choose(strat):
    if strat == "random":
        # pick a random choice
        return random.choice([0,1])
    elif strat == "always_0":
        return 0
    elif strat == "always_1":
        return 1
    elif strat == "greedy":
        # pick the choice with the max possible gain
        if gains.index(max(gains)) >1:
            return 1
        else:
            return 0
    elif strat == "average_win":
        # pick the choice with the max average gain
        if gains[0]+gains[1] > gains[2]+gains[3]:
            return 0
        else:
            return 1
    elif strat == "sympa":
        # pick the choice with the max possible total win for both player
        if gains[0]*2 > gains[3]*2:
            return 0
        else:
            return 1
    elif strat == "generous":
        # pick the max possible gain for adv
        if gains.index(max(gains)) == 0:
            return 0
        elif gains.index(max(gains)) == 3:
            return 1
        elif gains.index(max(gains)) == 1:
            return 1
        else:
            return 0
    elif strat == "evil":
        # pick the choice with the least average gain for adv
        if gains[0]+gains[2] <= gains[1]+gains[3]:
            return 0
        else:
            return 1
    return None




strats = {
    "random":0,
    "always_0":0,
    "always_1":0,
    "greedy":0,
    "average_win":0,
    "sympa":0,
    "generous":0,
    "evil":0

    }

choices = {
"random":0,
    "always_0":0,
    "always_1":0,
    "greedy":0,
    "average_win":0,
    "sympa":0,
    "generous":0,
    "evil":0
}
def game():
    global res_1,res_2,strats,gains
    for strat_1 in strats.keys():
        for strat_2 in strats.keys():

            res_1 = choose(strat_1)
            res_2 = choose(strat_2)

            choices[strat_1]+=res_1/100
            choices[strat_2] += res_2 / 100

            #print(strat_1, strat_2)
            #print(res_1, res_2)

            if res_1 ==0 and res_2==0:
                #print(f"{strat_1} : +{gains[0]} ; {strat_2} : +{gains[0]}")

                strats[strat_1] += gains[0]
                strats[strat_2] += gains[0]
            elif res_1 ==1 and res_2==0:
                #print(f"{strat_1} : +{gains[2]} ; {strat_2} : +{gains[1]}")
                strats[strat_1] += gains[2]
                strats[strat_2] += gains[1]
            elif res_1 == 0 and res_2 == 1:
                #print(f"{strat_1} : +{gains[1]} ; {strat_2} : +{gains[2]}")
                strats[strat_1] += gains[1]
                strats[strat_2] += gains[2]
            else:
                #print(f"{strat_1} : +{gains[3]} ; {strat_2} : +{gains[3]}")
                strats[strat_1] += gains[3]
                strats[strat_2] += gains[3]
        """for i,n in enumerate(gains):
            gains[i]+= random.randint(-20,20)"""

        #print(strats)

for i in range(0,10000):
    gains = [random.randint(50,250),random.randint(-50,100),random.randint(100,250),random.randint(-100,50)]
    game()

sorted_by_values = dict(sorted(strats.items(), key=lambda item: item[1]))

print(sorted_by_values)
for name, score in sorted_by_values.items():
    print(f"{name} : {score} | {choices[name]}% de 1")

