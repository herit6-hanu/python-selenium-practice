def test_1():
	a=1
	b=2
	assert a!=b,f'{a} should not be equals to {b}'
def test_2():
	a=1
	b=12
	assert a!=b,f'{a} and {b} should not be same'

def test_3():
	assert 5==5, f'5 and 5 should be equal'