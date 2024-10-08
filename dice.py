import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# The Null Hypothesis assumes that the dice is fair
# The Alternate Hypothesis assumes that the dice isn't fair

dice_sides = 8  # Change the number of sides here

# Roll your dice and put your results here
observed = [1, 2, 3, 4, 5, 6, 7, 8]

# Convert observed rolls to a NumPy array
observed_rolls = np.array(observed)

# Compute observed frequencies
observed_freq = np.bincount(observed_rolls, minlength=dice_sides + 1)[1:]

# Compute expected frequencies (assuming a fair dice)
expected_freq = np.full(dice_sides, len(observed_rolls) / dice_sides)

# Check if sample size is large enough for Chi-square assumption
if np.any(expected_freq < 5):
    print(f"Warning: Expected frequencies are less than 5. Consider collecting more data.")
else:
    print("The sample size is adequate for the Chi-square test.")

# Perform Chi-square test
chi2_stat, p_value = chisquare(observed_freq, expected_freq)

# Luck related calculations
average_roll = np.mean(observed_rolls)
expected_average = (dice_sides + 1) / 2  # Correct expected average
luck_percentile = (average_roll - 1) / (dice_sides - 1) * 100

# Print results
print(f"Average Roll: {average_roll:.2f}")
print(f"Expected Average Roll: {expected_average:.2f}")
print(f"Luck Percentile: {luck_percentile:.2f}%")  
print(f"Number of Rolls: {len(observed)}")

# Chi-square test results
print(f"Observed Frequencies: {observed_freq}")
print(f"Expected Frequencies: {expected_freq}")
print(f"Chi-square Statistic: {chi2_stat:.2f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("We reject the null hypothesis. The die is likely not fair.")
else:
    print("We fail to reject the null hypothesis. The die is likely fair.")

# Plot histogram of observed rolls
plt.hist(observed_rolls, bins=np.arange(0.5, dice_sides + 1.5, 1), edgecolor='black')
plt.xticks(range(1, dice_sides + 1))
plt.xlabel('Dice Sides')
plt.ylabel('Frequency')
plt.title('Dice Roll Distribution')
plt.show()
