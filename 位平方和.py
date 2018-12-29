# 把一个整数的每个数位都平方后求和，又得到一个整数，我们称这个整数为：位平方和。
# 对新得到的整数仍然可以继续这一运算过程
# 已知一个整数x，求第n步的运算结果。


# 判断整数的位数 方法一
def f1(m):
	if 999999999>=m>=100000000:
		return 9
	elif m>=10000000:
		return 8
	elif m>=1000000:
		return 7
	elif m>=100000:
		return 6
	elif m>=10000:
		return 5
	elif m>=1000:
		return 4
	elif m>=100:
		return 3
	elif m>=10:
		return 2
	elif m>=0:
		return 1
# 判断整数的位数 方法二
# 参数m为待测整数,n为估计位数
def f3(m,n):
	if m>10**(n-1):
		for i in range(n-1,100):
			if m/(10**i)<10:
				return i+1
	else:
		for i in range(n-1,-100,-1):
			if m/(10**i)>1:
				return i+1
# 取整数的每一位数
def f2(m,n):
	a = []
	for i in range(1,n+1):
		b = 10**(n-i)
		c = m//b
		m = m%b
		a.append(c)
	return a
# 按规则进行平方，m为初始数值，n为第几次
def f(m,n):
	a = []
	for i in range(n):
		s1 = f1(m)
		l1 = f2(m,s1)
		s2 = len(l1)
		c = 0
		for j in range(s2):
			c = l1[j]**2+c
		print(c)
		a.append(c)
		m = c
	return a
m = 1314
a = f1(m)
print(f(m,10))
print(f3(44355,5))
