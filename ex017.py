import math
co = float(input('Digite um valor para o cateto oposto: '))
ca = float(input('Digite um valor para o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A soma entre os catetos é a hipotenusa, que é o valor de: {:.2f}.'.format(hi))
cp = float(input('Digite outro valor para o cateto oposto: '))
cd = float(input('Digite outro valor para o cateto adjacente: '))
hc = (cp**2 + cd**2)**(1/2)
print('A soma entre os catetos é a hipotenusa, que é o valor de: {:.2f}.'.format(hc))
