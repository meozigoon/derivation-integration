def isDigit(c):
	return (ord('0') <= ord(c) and ord(c) <= ord('9'))

def f(s):
	i = 0
	l = []
	while i < len(s):
		if isDigit(s[i]):
			num = ""
			while i < len(s) and isDigit(s[i]):
				num += s[i]
				i += 1
			l.append(num)
		elif s[i] == ' ':
			i += 1
		elif s[i] == '+' or s[i] == '-':
			l.append(s[i])
			i += 1
		else:
			term = ""
			while i < len(s) and s[i] != '+' and s[i] != '-' and s[i] != ' ':
				term += s[i]
				i += 1
			l.append(term)
	return l

def fp(l):
	df = ""
	i = 0
	while i < len(l):
		if l[i][0] == 'x':
			co = 1
			if isDigit(l[i - 1][0]):
				co = int(l[i - 1])
			if l[i] == 'x':
				df += str(co)
			else:
				exp = int(l[i].split('^')[1])
				df += str(exp * co) + 'x'
				if exp > 2:
					df += '^' + str(exp - 1)
			i += 1
		elif isDigit(l[i][0]):
			i += 1
		elif l[i] == '+' or l[i] == '-':
			df += l[i]
			i += 1
	if df[-1] == '+' or df[-1] == '-':
	    df = df[0:-1]
	return df


fx = input() #str
ft = f(fx) # list
print(ft)
df = fp(ft) #str
print(df)
