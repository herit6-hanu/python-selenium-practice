def gen():
	list=[i for i in range(10000000)]
	yield list
print(next(gen()))
