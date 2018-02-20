def mayor_digito(n):
    if n<=0:
        return 0;
    else:
        if ((n%10) < mayor_digito(n/10)):
            return (mayor_digito(n/10))
        else:
            return (n%10)
print(mayor_digito(564738232262626))
