def longitud(n):
    if n<10:
        return 1
    else:
        return (longitud(n/10))+1
print(longitud(123456))
