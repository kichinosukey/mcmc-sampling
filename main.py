from random import random
import numpy as np

y = np.array([4,3,4,5,5,2,3,1,4,0,1,5,5,6,5,4,4,5,3,4])

def lr_cost(y, q, C=70):
    return sum(y*np.log(q) + (8 - y)*np.log(1-q)) + C

def judge():
    return np.random.rand()

def update(q_before, q_after):
    if q_before < q_after and update_prob(q_before, q_after):
        return q_after
    else:
        return q_before

def update_prob_random():
    return 1 if np.random.randn() > 0.5 else 0

def compare_lilkely(q_before, q_after):
    return True if (lr_cost(y, q_after) - lr_cost(y, q_before)) >= 0 else False

def update_prob(q_befor, q_after):
    return True if np.random.randint(1, 100)/100 > np.exp(lr_cost(y, q_after) - lr_cost(y, q_befor)) else False

def select_q_random(q_before, increase=True, step=0.01):
    if increase:
        return q_before + step
    else:
        return q_before - step

if __name__ == '__main__':

    # step1
    q = np.random.randint(1, 100) / 100
    # q = 0.3
    count = 0
    while count < 100:

        # step2
        if update_prob_random():
            increase = True
        else:
            increase = False
        q_after = select_q_random(q, increase=increase)

        # step3
        if compare_lilkely(q, q_after) or update_prob(q, q_after):
            q = q_after
        else:
            pass
        print(count, increase, q, q_after, lr_cost(y, q)) 
        count += 1