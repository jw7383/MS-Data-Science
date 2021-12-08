import numpy as np
import matplotlib.pyplot as plt
plt.close("all")
np.random.seed(2017)
import random

def p_longest_streak(n, tries):
    #n is the length of the sequence and tries is the number
    # of sampled sequences used to produce the estimate of the probability
    inv_tries = 1.0/float(tries)
    prob_head_streak = np.zeros(n+1)
    for runs in range(tries):
        longest_head_streak = 0
        current_head_streak = 0
        for i in range(n):
            flip = random.randint(0,1)
            if flip == 0:
                current_head_streak +=1
                if current_head_streak > longest_head_streak:
                    longest_head_streak = current_head_streak
            else:
                current_head_streak = 0
        prob_head_streak[longest_head_streak] += inv_tries
    return prob_head_streak

n_tries = [1e3,5e3,1e4,5e4,1e5]

n_vals = [5,200]

color_array = ['orange','darkorange','tomato','red', 'darkred', 'tomato', 'purple', 'grey', 'deepskyblue', 
               'maroon','darkgray','darkorange', 'steelblue', 'forestgreen', 'silver']
for ind_n in range(len(n_vals)):
    n = n_vals[ind_n]
    plt.figure(figsize=(20,5))
    for ind_tries in range(len(n_tries)):
        tries = n_tries[ind_tries]
        p_longest_tries = p_longest_streak(n, np.intc(tries))
        plt.plot(range(n+1),p_longest_tries, marker='o',markersize=6,linestyle="dashed",lw=2,
                 color=color_array[ind_tries],
                 markeredgecolor= color_array[ind_tries],label=str(tries))
    plt.legend()
    
print("The probability that the longest streak of ones in a Bernoulli iid sequence of length 200 has length 8 or more is ")
print(np.sum(p_longest_streak(200,np.intc(1e5))[8:]))