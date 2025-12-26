# Task 2: Sum of Integers from 1 to 50

# Initialize a variable to store the sum

total_sum = 0

# 1. Uses a for loop to iterate over numbers from 1 to 50 [cite: 61]
# Note: range(1, 51) includes 1 and ends at 50
for i in range(1, 51):
    # 2. Calculates the sum of all integers in this range [cite: 62]
    total_sum += i

# 3. Displays the final sum [cite: 63]
print(f"The sum of numbers from 1 to 50 is: {total_sum}")