# this is a problem statement no 1
a = int(input("Enter your age or the Year you were born in : "))
current_year = int(input("In which year are you running this program in? : "))
X_years = int(input("Enter the age you want and find out in which year you're going to turn that age in : "))

if a>1000:
    print(f"You were born in the year {a}")
    age = current_year - a
    print(f"You are {age} years old")
    print(f"You will turn {X_years} years old in the year {a + X_years}")

elif a>=1 and a<=102:
    print(f"You are {a} years old")
    birth_year = current_year - a
    print(f"you were born in the year {birth_year}")
    print(f"You will turn {X_years} years old in the year {birth_year + X_years}")



