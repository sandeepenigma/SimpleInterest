print("A program to calculate simple interest")
p = input("Enter the principle amount")
r = input("Enter rate of interest")
t = input("Enter the time frame")
p = float(p)
r = float(r)
t = float(t)
c = (p * r * t) / 100
print("Simple interest is", (p * r * t) / 100)
d = c + p
print("Total value to be paid after", t, "years is", d)
