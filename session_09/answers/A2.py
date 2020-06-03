# A2 - Create a function that takes the circumferance of a circle and return
# the radius and area.

def circle(c):
    # Create a variable for PI since we will use it multiple times
    PI = 3.141592

    # Work out radius and then area
    r = c / (2 * PI)
    a = PI * (r ** 2)

    # Return both radius and area
    return r, a


radius, area = circle(100)

print(radius, area)
