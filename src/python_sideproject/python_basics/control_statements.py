marks = 72
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

# Logical operators: and, or, not
age = 25
has_id = True
is_member = False

# and -> True only if both conditions are True
if age >= 18 and has_id:
    print("Entry allowed")
elif age >= 18 and not has_id:
    print("Adult, but ID is required")
elif age < 18 and has_id:
    print("Too young to enter")
else:
    print("Entry denied")

# or -> True if at least one condition is True
if is_member and age >= 60:
    print("Member + senior discount")
elif is_member or age >= 60:
    print("Discount applied")
else:
    print("No discount")

# not -> reverses the condition
if not is_member and age >= 18:
    print("Please sign up for membership")
elif not is_member:
    print("Membership requires a guardian")
else:
    print("Welcome back, member")

# Combining operators (use parentheses for clarity)
if (age >= 18 and has_id) and (is_member or age < 30):
    print("Special offer available")
elif age >= 18 and has_id:
    print("Standard offer available")
else:
    print("No offer")

# Logical operators with membership checks
day = "Sat"
if day == "Sat" or day == "Sun":
    print("Weekend")
elif day == "Fri":
    print("Almost weekend")
else:
    print("Weekday")

if day in ("Sat", "Sun"):  # shorter equivalent
    print("Weekend")
else:
    print("Not a weekend")

# Chained comparison (same as marks >= 60 and marks < 75)
if 60 <= marks < 75:
    print("Grade C range")
elif 75 <= marks < 90:
    print("Grade B range")
elif marks >= 90:
    print("Grade A range")
else:
    print("Below passing marks")
