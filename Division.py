def division(n,m):
    if n<m:
        return 0;
    else:
        return 1 + division(n-m,m);    
print(division(64,2));
