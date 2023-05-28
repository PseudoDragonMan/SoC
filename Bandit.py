import numpy as np
import matplotlib.pyplot as plt


# Function to generate a random number from a normal distribution
def normal():
    return np.random.default_rng().normal(2, 1, 1)[0]


# Function to generate a random number from a Poisson distribution
def poisson():
    return np.random.default_rng().poisson(2, 1)[0]


# Function to simulate a coin toss and return the corresponding reward
def coin_toss():
    a = np.random.randint(0, 2)
    if a == 1:
        return 5
    else:
        return -6


# Function to generate a random number from an exponential distribution
def exponential():
    return np.random.default_rng().exponential(3, 1)[0]


# Function to simulate a crazy button press and return the corresponding reward
def crazy_button():
    a = np.random.randint(0, 4)
    if a == 0:
        return normal()
    elif a == 1:
        return poisson()
    elif a == 2:
        return coin_toss()
    else:
        return exponential()


# Function to run the epsilon-greedy algorithm and calculate the average rewards
def y(e):
    final = [0] * 100
    for x in range(1000):
        r_sum = [0] * 5
        r_avg = [0] * 5
        freq = [0] * 5
        rewards = [0] * 100
        for i in range(100):
            j = np.random.rand()
# Using rand to generate a random number between 0 and 1. If this number is less than the given value of e, or if i = 0, a random button is chosen
            if i == 0 or j < e:
                k = np.random.randint(0, 5)
                if k == 0:
                    rewards[i] = normal()
                elif k == 1:
                    rewards[i] = poisson()
                elif k == 2:
                    rewards[i] = coin_toss()
                elif k == 3:
                    rewards[i] = exponential()
                elif k == 4:
                    rewards[i] = crazy_button()

                r_sum[k] += rewards[i]
                freq[k] += 1
                r_avg[k] = r_sum[k] / freq[k]
                final[i] += rewards[i] / 1000
            else:
# We make the agent choose the button which has the maximum average reward.
                a = max(r_avg)
                if a == r_avg[0]:
                    rewards[i] = normal()
                    c = 0
                elif a == r_avg[1]:
                    rewards[i] = poisson()
                    c = 1
                elif a == r_avg[2]:
                    rewards[i] = coin_toss()
                    c = 2
                elif a == r_avg[3]:
                    rewards[i] = exponential()
                    c = 3
                elif a == r_avg[4]:
                    rewards[i] = crazy_button()
                    c = 4

                r_sum[c] += rewards[i]
                freq[c] += 1
                r_avg[c] = r_sum[c] / freq[c]
                final[i] += rewards[i] / 1000
    return final


x = np.arange(0, 100)

# Plotting the results for different values of epsilon
plt.plot(x, y(0), label="e = 0")
plt.plot(x, y(0.01), label="e = 0.01")
plt.plot(x, y(0.1), label="e=0.1")
plt.legend()
plt.show()
