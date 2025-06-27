

from tbcontrol.symbolic import routh 
import sympy
import matplotlib.pyplot as plt

s= sympy.Symbol('s')

#FT De Malha Aberta
Y_s=1;
P_s=100*(s+4)/(s*((s+1)*(s+2)*(s+5)));
G_s=sympy.expand(Y_s*P_s); #Calcula os termos do polinomio P(s)
print("Malha aberta G(s)={}".format(G_s))


#FT De Malha Fechada
H_s=1;
G1_s=sympy.cancel((G_s)/(1+G_s*H_s))
print("Malha fechada G1(s)={}".format(G1_s))
num_G1_s,den_G1_s= sympy.fraction(G1_s) 


den_G1_s = sympy.poly(den_G1_s)

print("\nTabela de Routh")
tabela=routh(den_G1_s)
print(tabela)


poles = sympy.solve(den_G1_s)
print("Os polos sao: {}".format(poles))



plt.figure() 
for pole in poles: 
    plt.plot(sympy.re(pole), sympy.im(pole),'rx')
    
    
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)

    
    plt.grid(True, which='both', linestyle='--', lw=0.5)

   
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.title('Polos no Plano Complexo')

plt.show()



