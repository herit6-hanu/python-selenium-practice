k = 0


def gen():
	lists = [i for i in range(1000)]
	while True:
		global k
		yield lists[k]
		k += 1


res = gen()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
