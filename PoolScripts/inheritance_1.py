class A:
	def __init__(self, a, b):
		self.a = a
		self.b = b


class B(A):
	def __init__(self, a, b, c, d):
		super().__init__( a, b)
		self.c = c
		self.d = d


a = A(2,3)
b = B(2,4,6,8)
print(a.a,a.b,b.a,b.b,b.c,b.d)
