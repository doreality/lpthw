# ex30.py Else 和 if

cars = 1
people = 3
trucks = 2

max_num = 0
mid_num = 0
min_num = 0

if cars >= people and trucks >= people:
    min_num = people
    if cars >= trucks:
        max_num = cars
        mid_num = trucks
    else:
        max_num = trucks
        mid_num = cars
elif cars <= people and trucks <= people:
    max_num = people
    if cars >= trucks:
        mid_num = cars
        min_num = trucks
    else:
        mid_num = trucks
        min_num = cars
else:
    mid_num = people
    if cars >= trucks:
        max_num = cars
        min_num = trucks
    else:
        max_num = trucks
        min_num = cars

print(f"{max_num} > {mid_num} > {min_num}")
