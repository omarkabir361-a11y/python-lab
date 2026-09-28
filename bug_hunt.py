count = 1
total = 0

# BUG: Fixed SyntaxError by adding a missing colon (:) at the end of the while loop statement.
# BUG: Fixed logic bug where condition 'count < 5' excluded 5; changed to 'count <= 5' to sum 1 through 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Fixed TypeError by converting integer 'total' to string using str(total) for concatenation.
print("Sum of 1 to 5 is: " + str(total))