 # factorial (5) -> 5 * 4 * 3 * 2 * 1 = 120 
 
#number = 70
#result = 1
#for i in range(number):
   #result = result * (i + 1)
   #print("Iteration..")
   #print(i +1)
   #print(result)
   #if result > 10 ** 82:
    #print("Woah that's big!")
#print("And the grand final tally is:")
#print(result)


height = 4
width = 6
top = "+"
for i in range(width - 2):
 top = top + "-"
top = top + "+"
print(top)
for j in range(height - 2):
 side = "|"
 for i in range(width - 2):
   side = side + " "
 side = side + "|"
 print(side)
bottom = "+"
for i in range(width - 2):
 bottom = bottom + "-"
bottom = bottom + "+"
print(bottom) 