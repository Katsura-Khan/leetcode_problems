def halvesAreAlike( s: str) -> bool:
    volwers = ['a','e','i','o','u','A','E','I','O','U']
    i,j = 0, len(s) - 1 
    c1,c2= 0,0
    while i<j:
        c1 += s[i] in volwers
        c2 +=s[j] in volwers
        i += 1
        j-=1
    print(c1,c2)
    return c1==c2

print(halvesAreAlike('book'))