def producto(n,m):
    if m==0:
        return 0
    if m==1:
        return n
    else:
        return (n + producto(n,m-1))
print(producto(1,5))

def division(n,m):
    if n<m:
        return 0;
    else:
        return 1 + division(n-m,m);    
print(division(64,2));


def fibonacii(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacii(n-1) + fibonacii(n-2)
print fibonacii(13)


def potencia(n,m):
    if m==0:
        return 1
    else:
        return n * potencia(n,m -1);
print(potencia(5,8))


def suma_digitos(n):
    if n<10:
        return n;
    else:
        return (n%10) + suma_digitos(n//10) 
print(suma_digitos(223))


def mayor_digito(n):
    if n<=0:
        return 0;
    else:
        if ((n%10) < mayor_digito(n/10)):
            return (mayor_digito(n/10))
        else:
            return (n%10)
print(mayor_digito(564738232262626))

def invertir_numero(n):
    if n<10:
        return n;
    else:
        return str(n%10)+ str(invertir_numero(n//10) )
print(invertir_numero(223))


def longitud(n):
    if n<10:
        return 1
    else:
        return (longitud(n/10))+1
print(longitud(123456))


def palindromo(n):
    if len(n)==1 or len(n)==0:
        return " si es palindromo"
    elif(n[0]==n[len(n)-1]):
        n=n[1:-1]
        return palindromo(n)
    else:
        return "no es palindroma"
print (palindromo(3222))









