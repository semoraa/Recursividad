def palindromo(n):
    if len(n)==0 or len(n)==1:
        return True
    else:
        if n[0]==n[-1]:
            return palindromo(n[1:-2])
        else:
            return False
print (palindromo("axxa"))
    
