def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Get student name
name = input()

# Get 5 grades without loops
g1 = int(input())
g2 = int(input())
g3 = int(input())
g4 = int(input())
g5 = int(input())

# Store grades in a list
grades = [g1, g2, g3, g4, g5]

# Calculate average using the list
avg = sum(grades) / len(grades)

# Determine the letter grade
letter = get_letter_grade(avg)

# Print output
print(name)
print("Average:", avg)
print("Letter Grade:", letter)