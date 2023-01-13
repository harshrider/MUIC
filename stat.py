import statistics
f = open("stat.txt", "r")
num = []
for i in f:
    a = f.readline()
    if(a.isdigit):
        num.append(int(a))

print("mean: ",statistics.mean(num),
    "\nstd: ",statistics.stdev(num),
    "\nmin: ",min(num),
    "\nmax: ",max(num))
