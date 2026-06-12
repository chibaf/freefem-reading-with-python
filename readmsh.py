with open("yunomi1.msh", "r") as f:
	lines = f.readlines()
lines_rstrip = [line.rstrip("\n") for line in lines]
print(lines_rstrip)
print(len(lines_rstrip))
print(lines_rstrip[0])