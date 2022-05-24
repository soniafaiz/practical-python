# bounce.py
#
# Exercise 1.5
height = 100.0      # initial height
bounceBack = 3/5    # proportion of fall that gives height of next bounce
bounceCount = 0     # bounce number

while bounceCount <10:
    bounceCount += 1
    height *= bounceBack
    print(bounceCount,round(height,4))
