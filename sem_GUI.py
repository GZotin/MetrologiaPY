# Calculadora de metrologia sem GUI
import numpy as np
import time
from vef_k import k
from vef_k import vef
print("Calculadora de metrologia")

# Dados iniciais 
print("Insira os dados inciais...")
res = float(input("Resolução [mm]: "))
td = float(input("Tolerância [mm]: "))
Ucal = float(input("Incerteza de calibração [mm]: "))
K_Ucal = float(input("Fator de abrangência da incerteza de calibração (K): "))
alpha_SM = float(input("Coeficiente de dilatação térmica do sistema de medição [μm/(mºC)]: "))
alpha_peca = float(input("Coeficiente de dilatação térmica da peça [μm/(mºC)]: "))
t_amb = float(input("Temperatura do ambiente de medição: "))
erro_t_amb = float(input("Incerteza associada a temperatura: "))

# Leituras
qtd_leituras = float(input("Insira a quantidade de leituras: "))

for i in range(int(qtd_leituras)):
    if i == 0:
        leituras = np.array(input("Insrira o valor da leitura: ")).astype(np.float)
    else:
        leituras = np.append(leituras, input("Insrira o valor da leitura: ")).astype(np.float)
    
media = np.average(leituras)
desv_pad_A = np.std(leituras, ddof = 1)

# Cálculos
                                                
# Diferença de dilatação térmica
L0 = float(media - td)
Delta_T = float(t_amb - 20)
Delta_Ls = float(L0 * (alpha_peca - alpha_SM) * Delta_T * 10**(-6))

# Média das leituras corrigida
RB = float(media - td - Delta_Ls)

# Determinação dos efeitos das fontes de erro aleatório

# Estimativa da incerteza padrão do tipo A – Avaliação do tipo A
u_a = float(desv_pad_A/np.sqrt(qtd_leituras))
v_a = float(qtd_leituras - 1)

# Estimativa do efeito da incerteza da calibração (incerteza da tendência) – Avaliação do tipo B
u_b1 = float(Ucal / K_Ucal)
v_b1 = vef(K_Ucal)

# Estimativa do efeito da resolução limitada (finita) do sistema de medição – Avaliação do tipo B
u_b2 = float((res/2)/np.sqrt(3))
v_b2 = float("inf")

# Estimativa do efeito aleatório da temperatura
Delta_La = float(RB * (alpha_peca + alpha_SM) * erro_t_amb * 10**(-6))
u_b3 = float(Delta_La/np.sqrt(6))
v_b3 = float("inf")

# Determinação da incerteza padrão combinada
u_c = float(np.sqrt(u_a**2 + u_b1**2 + u_b2**2 + u_b3**2))
v_ef = np.power(u_c, 4)/((np.power(u_a, 4) / v_a)+(np.power(u_b1, 4) / v_b1))

# Determinação da incerteza expandida
U = float(k(v_ef)*u_c)

# Resultado de Medição
print("O resultado de medição é: (%f ± %f) mm para U95,45%% e K = %f" %(RB, U, k(v_ef)))

# Não fechar o terminal
# time.sleep()