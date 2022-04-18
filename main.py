# Collect inputs from user and needs to be in certain range by using while function
v = float(input("Please provide Object A current travelling speed [1,10], v\n"))
while v < 1 or v > 10:
    v = float(input("Your v is out of range; Please provide Object A current travelling speed [1,10], v\n"))

d = float(input("Please provide the distance between Object A and B [5,10], d \n"))
while d < 5 or d > 10:
    d = float(input("Your d is out of range; Please provide the distance between Object A and B [5,10], d \n"))

a = float(input("Please provide Object A current accelerating speed [-100,0], a\n"))
while a < -100 or a > 0:
    a = float(input("Your a is out of range; Please provide Object A current accelerating speed [-100,0], a\n"))

t = float(input("Please provide the travelling time for object A (0,10), t\n"))
while t <= 0 or t > 10:
    t = float(input("Your t is out of range, Please provide the travelling time for object A (0,10), t\n"))


# Determine S (the breaking distance for A to collapse B)
s = v*t+0.5*a*t*2

# Req 1: Compare d and d, output if they are going to collapse
if s < d:
    print("They will not collide")
else:
    print("They will collide")

# Req 2: Calculate a; they will be just touching and use proper format for these numbers by using while loop
# s = v*t+0.5*a*t**2

if s > d:
    # if breaking distance(s) is longer than distance d, we increase deceleration speed(a) and test again
    while s > d:
        print("Breaking distance S", format(s, ".2f"), "is longer than d", d, "We will break heavier and test again\n")
        a = a-0.2
        v_current = v
        while v_current > 0:
            t = t + 0.2
            v_current = v + a * t
        s = v * t + 0.5 * a * t ** 2
        print("New t= ", format(t, ".2f"))
        print("New a =", format(a, ".2f"))
        print("New s= ", format(s, ".2f"))
elif s < d:
    # if breaking distance(s) is shorter than distance d, we decrease deceleration speed(a) and test again
    while s < d:
        print("Breaking distance S", format(s, ".2f"), "is shorter than d", d, "We will break lighter and test again\n")
        a = a + 0.2
        v_current = v
        while v_current > 0:
            t = t + 0.2
            v_current = v + a * t
        s = v * t + 0.5 * a * t ** 2
        print("New t= ", format(t, ".2f"))
        print("New a =", format(a, ".2f"))
        print("New s= ", format(s, ".2f"))
print("\nBreaking distance S", format(s, ".2f"), "is very close to the distance between 2 cars", format(d, ".2f"))
print("so The critical value of acceleration a at A just touch B is ", format(a, ".2f"))
