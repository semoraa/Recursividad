def producto(n,m):
    if m==0:
        return 0
    if m==1:
        return n
    else:
        return (n + producto(n,m-1))
print(producto(8,5))
