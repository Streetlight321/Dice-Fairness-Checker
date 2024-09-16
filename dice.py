import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt
import seaborn as sns
from math import floor
sns.set()

# The Null Hypothesis assumes that the dice is fair
# The Alternate Hypothesis assumes that the dice isn't fair
# Change the number of sides here
dice_sides = 8

# Roll your dice and put your results here in this format: [1,2,3,4]
observed = [1, 2, 3, 4, 5, 6, 7, 8]

# Observed rolls
observed_rolls = np.array(observed)

# Compute observed frequencies
observed_freq = np.bincount(observed_rolls)[1:]

# Compute expected frequencies (assuming a fair dice)
expected_freq = np.full(dice_sides, len(observed_rolls) / dice_sides)

# Check if sample size is large enough for Chi-square assumption
if len(observed_rolls) != dice_sides*5:
    print("Warning: The sample does not equal the number of sides * 5. The sample size may be too small for reliable conclusions.")
else:
    print("The sample size seems large enough for the Chi-square test.")

# Perform Chi-square test
chi2_stat, p_value = chisquare(observed_freq, expected_freq)

# Luck related calculations
average_roll = np.mean(observed_rolls)
expected_average = dice_sides / 2
luck_percentile = (average_roll - 1) / (dice_sides - 1) * 100

# Print results
print(f"Average Roll: {floor(average_roll)}")
print(f"Luck Percentile: {luck_percentile:.2f}%")  
print(f"Number of rolls: {len(observed)}")

# Chi-square test results
print(f"Observed Frequencies: {observed_freq}")
print(f"Expected Frequencies: {expected_freq}")
print(f"Chi-square Statistic: {chi2_stat:.2f}")
print(f"P-value: {p_value:.2f}")

if p_value < 0.05:
    print("We reject the null hypothesis. The die is likely not fair.")
else:
    print("We fail to reject the null hypothesis. The die is likely fair.")

# Plot histogram of observed rolls
plt.hist(observed, bins=dice_sides)
plt.xlabel('Dice Sides')
plt.ylabel('Frequency')
plt.title('Dice Roll Distribution')
plt.show()