# There are 60 stairs. A person made a bet of reaching at step 60.
# Game is, roll a dice. 
# if 1 or 2 comes, go one step beyond
# if 3,4,5 comes, go one step up
# if 6 comes, roll dice again and go steps up of the value of dice
# Calculate chances of a person on reaching at step 60

import matplotlib.pyplot as plt
import numpy as np

# Set the seed
np.random.seed(123)

# initialize and populate all_walks
all_walks = []
for i in range(500) : # running our simulation 500 times to get accurate chance of person reaching on step 60
    random_walk = [0] # 0 is 1st step value means ground floor
    # roll a dice 100 times
    for x in range(100) :
        step = random_walk[-1] # pick last step
    
        # Roll the dice
        dice = np.random.randint(1,7) # return integer b/w 1 and 6.
    
        # Determine next step
        if dice <= 2:
            #  go one step beyond
            step = max(0, step - 1) # step must be greater than or equal to 0. it cannot be negative
        elif dice <= 5:
            # go one step up
            step = step + 1
        else:
            # if dice gives 6, roll dice again and add that number to step
            step = step + np.random.randint(1,7)

        # Implement clumsiness - There is 0.1 chance of falling. If fallen, start from 0
        if np.random.rand() <= 0.001 :
            step = 0

        # append next_step to random_walk
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw) # transpost convert columns to rows and rows to columns

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

# Clear the figure
plt.clf()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :] # row where end of each walk exists. We are calculating with 500 walks

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

### # count when a person will reach at 60 steps
endsReached = ends >= 60 # 
np.add((endsReached)/500) # Chance of person on reaching out to end step
