def palindromo(n):
    if len(n)==1 or len(n)==0:
        return " si es palindromo"
    elif(n[0]==n[len(n)-1]):
        n=n[1:-1]
        return palindromo(n)
    else:
        return "no es palindroma"
print (palindromo(3222))
