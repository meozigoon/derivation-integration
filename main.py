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
		elif i + 3 < len(s) and (s[i:i + 4] == 'sin(' or s[i:i + 4] == 'cos('):
		    term = s[i:i + 4]
		    i += 4
		    while i < len(s) and s[i] != ')':
		        term += s[i]
		        i += 1
		    term += ')'
		    i += 1
		    l.append(term)
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
			if i - 1 >= 0 and isDigit(l[i - 1][0]):
				co = int(l[i - 1])
			if l[i] == 'x':
				df += str(co)
			else:
				exp = int(l[i].split('^')[1])
				df += str(exp * co) + 'x'
				if exp > 2:
					df += '^' + str(exp - 1)
				df += ' '
			i += 1
		elif len(l[i]) >= 4 and l[i][0:4] == 'sin(':
		    fin = f(l[i][4:-1]) # list
		    dfin = fp(fin) # str
		    if dfin == 'x':
		        df += 'xcos(' + l[i][4:-1] + ')'
		    elif dfin == '1':
		        df += 'cos(' + l[i][4:-1] + ')'
		    else:
		        df += '(' + dfin + ')' + 'cos(' + l[i][4:-1] + ')'
		    i += 1
		elif len(l[i]) >= 4 and l[i][0:4] == 'cos(':
		    fin = f(l[i][4:-1]) # list
		    dfin = fp(fin) # str
		    print(fin, dfin)
		    if dfin == 'x':
		        df += '-xsin(' + l[i][4:-1] + ')'
		    elif dfin == '1':
		        df += '-cos(' + l[i][4:-1] + ')'
		    else:
		        df += '-(' + dfin + ')' + 'cos(' + l[i][4:-1] + ')'
		    i += 1
		elif isDigit(l[i][0]) or l[i] == '(' or l[i] == ')':
			i += 1
		elif l[i] == '+' or l[i] == '-':
			df += l[i] + ' '
			i += 1
	if len(df) >= 2 and (df[-2] == '+' or df[-2] == '-'):
	    df = df[0:-2]
	return df

def If(l):
    idf = ""
    i = 0
    while i < len(l):
        if l[i][0] == 'x':
            co = 1
            if i - 1 >= 0 and isDigit(l[i - 1][0]):
                co = int(l[i - 1])
            if l[i] == 'x':
                if co / 2 == co // 2:
                    if co // 2 != 1:
                        idf += str(co // 2)
                else:
                    idf += str(co / 2)
                idf += 'x^2 '
            else:
                exp = int(l[i].split('^')[1])
                if co / (exp + 1) == co // (exp + 1):
                    if co // (exp + 1) != 1:
                        idf += str(co // (exp + 1))
                else:
                    idf += str(co / (exp + 1))
                idf += 'x^' + str(exp + 1) + ' '
            i += 1
        elif len(l[i]) >= 4 and l[i][0:4] == 'sin(' or l[i][0:4] == 'cos(':
            return 'err'
        elif isDigit(l[i][0]):
            i += 1
        elif l[i] == '+' or l[i] == '-':
            idf += l[i] + ' '
            i += 1
    if len(idf) >= 2 and (idf[-2] == '+' or idf[-2] == '-'):
        if l[-1] != '1':
            idf += l[-1]
        idf += 'x '
    return idf


fx = input("f(x) = ") #str
ft = f(fx) # list
print(ft)
df = fp(ft) #str
print("f'(x) = ", df)
idf = If(ft)
print("F(x) = ", idf) #str
