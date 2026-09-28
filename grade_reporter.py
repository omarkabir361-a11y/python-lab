# Scores list provided by assignment specification
scores = [72, 45, 90, 61, 38]

# Initialize tracking variables
pass_count = 0
fail_count = 0
total_score = 0

print("Individual Grades:")
# Loop through each score to assign grades and calculate metrics
for score in scores:
    total_score += score
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1
        
    print(f"Score: {score} -> Grade: {grade}")

# Calculate average score
average_score = round(total_score / len(scores), 1)

print("\nSummary Statistics:")
print(f"Learners Passed: {pass_count}")
print(f"Learners Failed: {fail_count}")
print(f"Average Score: {average_score}")