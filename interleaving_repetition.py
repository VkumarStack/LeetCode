def Interleaving(x, y, s):
    x = x * (len(s) // len(x) + 1)
    y = y * (len(s) // len(y) + 1)
    opt = [[False for i in range(len(s) + 1)] 
           for j in range(len(s) + 1)]
    opt[0][0] = True
    for i in range(len(s) + 1):
        for j in range(len(s) + 1):
            if i == 0 and j != 0:
                opt[0][j] = (y[j - 1] == s[j - 1]) and opt[0][j - 1]
            elif j == 0 and i != 0:
                opt[i][0] = (x[i - 1] == s[i - 1]) and opt[i - 1][0]
            elif i != 0 and j != 0 and (i + j) <= len(s):
                opt[i][j] = (((x[i - 1] == s[i + j - 1]) and 
                              opt[i - 1][j]) or 
                              ((y[j - 1] == s[i + j - 1]) and 
                                  opt[i][j - 1]))
    
    for i in range(len(s) + 1):
        if opt[i][len(s) - i]:
            return True
    return False

print(Interleaving( "101","00","10001010111"))