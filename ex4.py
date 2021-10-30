# ex4.py 变量和名字

# '='  表示赋值
# '==' 表示判断左右两边是否相同
# 加空格，阅读体验好


# 汽车数量
cars = 100
# 一辆车的容量（空间，可乘坐人数？）
space_in_a_car = 4.0 # space_in_a_car = 4
# 司机数量
drivers = 30
# 乘客数量
passengers = 90
# 未使用的汽车数量
cars_not_driven = cars - drivers
# 使用的汽车数量
cars_driven = drivers
# 拼车容量
carpool_capacity = cars_driven * space_in_a_car
# 平均每辆车上乘客数量
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")