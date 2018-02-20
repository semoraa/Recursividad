def invertir_numero(n):
    if n<10:
        return n;
    else:
        return str(n%10)+ str(invertir_numero(n//10) )
print(invertir_numero(12345))
