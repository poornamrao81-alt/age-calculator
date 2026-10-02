from datetime import date

name = input("Enter your name: ")
dob = input("Enter your date of birth (DD-MM-YYYY): ")

# Convert DOB into date
day, month, year = map(int, dob.split("-"))

dob = date(year, month, day)
today = date.today()

# Basic age calculation
age = today.year - dob.year

# Check if birthday has happened this year
if (today.month, today.day) < (dob.month, dob.day):
    age = age - 1

print("Hello", name)
print("Your age is:", age)

# Calculate days until next birthday

next_birthday = date(today.year, dob.month, dob.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, dob.month, dob.day)

days_left = (next_birthday - today).days

print("Days until your next birthday:", days_left)