#Calculadora de Metrologia

# Região de import
from tkinter import *
from tkinter import ttk 
import numpy as np
from vef_k import k
from vef_k import vef
import sys
import os

# pegar os dados iniciais
def enviar_dados():
    global res
    res = float(res_valor.get())
    res_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: %f' %(res), font = 'none 10').grid(row = 1, column = 2, sticky = W)
   
    global td
    td = float(td_valor.get())
    td_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: %f' %(td), font = 'none 10').grid(row = 2, column = 2, sticky = W)
   
    global Ucal
    Ucal = float(Ucal_valor.get())
    Ucal_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: %f' %(Ucal), font = 'none 10').grid(row = 3, column = 2, sticky = W)
    
    global K_Ucal
    K_Ucal = float(K_Ucal_valor.get())
    K_Ucal_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: %f' %(K_Ucal), font = 'none 10').grid(row = 4, column = 2, sticky = W)
    
    global alpha_SM
    alpha_SM = float(alpha_SM_valor.get())
    alpha_SM_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: %f' %(alpha_SM), font = 'none 10').grid(row = 5, column = 2, sticky = W)
    
    global alpha_peca
    alpha_peca = float(alpha_peca_valor.get())
    alpha_peca_lbl_status = ttk.Label(frame_outros_dados, text = 'Valor atual: %f' %(alpha_peca), font = 'none 10').grid(row = 6, column = 2, sticky = W)
   
    global t_amb
    t_amb = float(t_amb_valor.get())
    t_amb_lbl_status = ttk.Label(frame_outros_dados, text = 'Valor atual: %f' %(t_amb), font = 'none 10').grid(row = 7, column = 2, sticky = W)
   
    global erro_t_amb
    erro_t_amb = float(erro_t_amb_valor.get())
    erro_t_amb_lbl_status = ttk.Label(frame_outros_dados, text = 'Valor atual: %f' %(erro_t_amb), font = 'none 10').grid(row = 8, column = 2, sticky = W)
    
    status_dados_lbl.configure(text = 'Dados: Dados enviados!')
    s_status_dados_text.configure('status_dados_text.TLabel', foreground = 'green')
    
    status_resultados_lbl.configure(text = 'Resultado: Aguardando leituras!')
    s_status_resultados_text.configure('status_resultados_text.TLabel', foreground = 'red')

# definir quantidade de leituras
def enviar_qtd_leituras():
    global qtd_leituras
    estado_entradas = ['disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled']
    qtd_leituras = int(qtd_leituras_valor.get())
    for i in range(qtd_leituras):
        estado_entradas[i] = 'enabled'
    valor_leitura_01_entry.config(state = estado_entradas[0])
    valor_leitura_02_entry.config(state = estado_entradas[1])    
    valor_leitura_03_entry.config(state = estado_entradas[2])
    valor_leitura_04_entry.config(state = estado_entradas[3])
    valor_leitura_05_entry.config(state = estado_entradas[4])
    valor_leitura_06_entry.config(state = estado_entradas[5])
    valor_leitura_07_entry.config(state = estado_entradas[6])
    valor_leitura_08_entry.config(state = estado_entradas[7])
    valor_leitura_09_entry.config(state = estado_entradas[8])
    valor_leitura_10_entry.config(state = estado_entradas[9])
    valor_leitura_11_entry.config(state = estado_entradas[10])
    valor_leitura_12_entry.config(state = estado_entradas[11])
    valor_leitura_13_entry.config(state = estado_entradas[12])
    valor_leitura_14_entry.config(state = estado_entradas[13])
    valor_leitura_15_entry.config(state = estado_entradas[14])
    valor_leitura_16_entry.config(state = estado_entradas[15])
    valor_leitura_17_entry.config(state = estado_entradas[16])
    valor_leitura_18_entry.config(state = estado_entradas[17])
    valor_leitura_19_entry.config(state = estado_entradas[18])
    valor_leitura_20_entry.config(state = estado_entradas[19])
    valor_leitura_21_entry.config(state = estado_entradas[20])
    valor_leitura_22_entry.config(state = estado_entradas[21])
    valor_leitura_23_entry.config(state = estado_entradas[22])
    valor_leitura_24_entry.config(state = estado_entradas[23])
    valor_leitura_25_entry.config(state = estado_entradas[24])
    valor_leitura_26_entry.config(state = estado_entradas[25])
    valor_leitura_27_entry.config(state = estado_entradas[26])
    valor_leitura_28_entry.config(state = estado_entradas[27])
    valor_leitura_29_entry.config(state = estado_entradas[28])
    valor_leitura_30_entry.config(state = estado_entradas[29])
               
# enviar leituras
def enviar_leituras():
    global leituras_vetor
    leituras_vetor = []
    for i in range(qtd_leituras):
        leituras_vetor.append(float(valor_leitura[i].get()))
    status_leituras_lbl.configure(text = 'Leituras: Leituras enviadas!')
    s_status_leituras_text.configure('status_leituras_text.TLabel', foreground = 'green')
    
    status_resultados_lbl.configure(text = 'Resultado: Disponível!')
    s_status_resultados_text.configure('status_resultados_text.TLabel', foreground = 'blue')
        
# gerar resultados
def gerar_resultado():
    #limpar aba de resultados
    for widget in resultados.winfo_children():
            widget.destroy()
    
    #calculos
    media = np.average(leituras_vetor)
    desv_pad_A = np.std(leituras_vetor, ddof = 1)
    
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
    
    # Display de resultados
    #apresentação de dados
    
    display_RB_frame = LabelFrame(resultados, text = 'Resultado Base')
    display_RB_frame.pack(expand = 1)
    Label(display_RB_frame, text = 'Média das leituras', font = 'none 12').grid(row = 0, column = 0, pady = 5, padx = 10)
    Label(display_RB_frame, text = '%f [mm]' %media, font = 'none 12').grid(row = 0, column = 1, pady = 5, padx = 10, sticky = W)
    
    Label(display_RB_frame, text = 'Tendencia', font = 'none 12').grid(row = 1, column = 0, pady = 5, padx = 10)
    Label(display_RB_frame, text = '%f [mm]' %td, font = 'none 12').grid(row = 1, column = 1, pady = 5, padx = 10, sticky = W)
    
    Label(display_RB_frame, text = 'DeltaLs', font = 'none 12').grid(row = 2, column = 0, pady = 5, padx = 10)
    Label(display_RB_frame, text = '%f [mm]' %Delta_Ls, font = 'none 12').grid(row = 2, column = 1, pady = 5, padx = 10, sticky = W)
    
    Label(display_RB_frame, text = 'Resultado Base', font = 'none 12 bold').grid(row = 3, column = 0, pady = 5, padx = 10)
    Label(display_RB_frame, text = '%f [mm]' %RB, font = 'none 12 bold').grid(row = 3, column = 1, pady = 5, padx = 10, sticky = W)

    display_IM_frame = LabelFrame(resultados, text = 'Incerteza da medição')
    display_IM_frame.pack(expand = 1)
    Label(display_IM_frame, text = 'Estimativa da incerteza padrão do \ntipo A – Avaliação do tipo A', font = 'none 12').grid(row = 0, column = 0, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Ua = %f [mm]' %u_a, font = 'none 12').grid(row = 0, column = 1, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Va = %f' %v_a, font = 'none 12').grid(row = 0, column = 2, pady = 5, padx = 10)
    
    Label(display_IM_frame, text = 'Estimativa do efeito da incerteza da calibração \n(incerteza da tendência) – Avaliação do tipo B', font = 'none 12').grid(row = 1, column = 0, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Ub1 = %f [mm]' %u_b1, font = 'none 12').grid(row = 1, column = 1, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Vb1 = %f' %v_b1, font = 'none 12').grid(row = 1, column = 2, pady = 5, padx = 10)
    
    Label(display_IM_frame, text = 'Estimativa do efeito da resolução limitada (finita) \ndo sistema de medição – Avaliação do tipo B', font = 'none 12').grid(row = 2, column = 0, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Ub2 = %f [mm]' %u_b2, font = 'none 12').grid(row = 2, column = 1, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Vb2 = %f' %v_b2, font = 'none 12').grid(row = 2, column = 2, pady = 5, padx = 10)

    Label(display_IM_frame, text = 'Estimativa do efeito aleatório da temperatura', font = 'none 12').grid(row = 3, column = 0, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Ub3 = %f [mm]' %u_b3, font = 'none 12').grid(row = 3, column = 1, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Vb3 = %f' %v_b3, font = 'none 12').grid(row = 3, column = 2, pady = 5, padx = 10)
    
    Label(display_IM_frame, text = 'Incerteza padrão combinada', font = 'none 12').grid(row = 4, column = 0, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Uc = %f [mm]' %u_c, font = 'none 12').grid(row = 4, column = 1, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'Vef = %f' %v_ef, font = 'none 12').grid(row = 4, column = 2, pady = 5, padx = 10)
    
    Label(display_IM_frame, text = 'Incerteza padrão expandida', font = 'none 12 bold').grid(row = 5, column = 0, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'U = ± %f [mm]' %U, font = 'none 12').grid(row = 5, column = 1, pady = 5, padx = 10)
    Label(display_IM_frame, text = 'k(v_ef) = %f' %k(v_ef)).grid(row = 6, column = 1)


    RM_frame = LabelFrame(resultados, text = 'Resultado de medição')
    RM_frame.pack(expand = 1)

    Label(RM_frame, text = 'O resultado de medição é:', font = 'none 12').grid(row = 0, column = 0, pady = 5)
    Label(RM_frame, text = '(%f ± %f) [mm]' %(RB, U), font = 'none 12 bold').grid(row = 1, column = 0, pady = 5)
    Label(RM_frame, text = 'para U95,45%% e K = %f' %k(v_ef), font = 'none 12').grid(row = 2, column = 0, pady = 5)
    
    status_resultados_lbl.configure(text = 'Resultado: Gerado!')
    s_status_resultados_text.configure('status_resultados_text.TLabel', foreground = 'green')
    
    #botoes
    global botao_resultados
    botao_resultados.destroy()
    
    botoes_resultados_frame = Frame(resultados)
    botoes_resultados_frame.pack(expand = TRUE, side = BOTTOM)
    
    botao_resultados = ttk.Button(botoes_resultados_frame, text = 'Gerar outro resultado', command = gerar_resultado)
    botao_resultados.grid(row = 0, column = 0, padx = 30)
    
    botao_restart = ttk.Button(botoes_resultados_frame, text = 'Sair', command = restart)
    botao_restart.grid(row = 0, column = 1, padx = 30)

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

app = Tk() 
app.title("Calculadora de Metrologia") 
app.geometry('800x700') 

# Abas
s_abas = ttk.Style()
s_abas.configure('TNotebook.Tab', font = 'none 10')
tab_control = ttk.Notebook(app) 
sobre = ttk.Frame(tab_control) 
dados = ttk.Frame(tab_control)
leituras = ttk.Frame(tab_control) 
resultados = ttk.Frame(tab_control) 
tab_control.add(sobre, text='Sobre') 
tab_control.add(dados, text='Dados') 
tab_control.add(leituras, text='Leituras') 
tab_control.add(resultados, text='Resultados') 
tab_control.pack(expand=1, fill='both') 

# # Barra de status
statusbar = LabelFrame(app, relief = SUNKEN, bd = 0)
statusbar.pack(fill = X, side = BOTTOM)

status_dados_frame = LabelFrame(statusbar, relief = SUNKEN, bd = 1)
status_dados_frame.pack(side = LEFT)
s_status_dados_text = ttk.Style()
s_status_dados_text.configure('status_dados_text.TLabel', foreground = 'red')
status_dados_lbl = ttk.Label(status_dados_frame, text = 'Dados: Aguardando envio', font = 'none 9', anchor = W, style = 'status_dados_text.TLabel')
status_dados_lbl.grid(row = 0, column = 0, padx = 10)

status_leituras_frame = LabelFrame(statusbar, relief = SUNKEN, bd = 1)
status_leituras_frame.pack(side = LEFT)
s_status_leituras_text = ttk.Style()
s_status_leituras_text.configure('status_leituras_text.TLabel', foreground = 'red')
status_leituras_lbl = ttk.Label(status_leituras_frame, text = 'Leituras: Aguardando envio', font = 'none 9', anchor = W, style = 'status_leituras_text.TLabel')
status_leituras_lbl.grid(row = 0, column = 0, padx = 10)

status_resultados_frame = LabelFrame(statusbar, relief = SUNKEN, bd = 1)
status_resultados_frame.pack(side = LEFT)
s_status_resultados_text = ttk.Style()
s_status_resultados_text.configure('status_resultados_text.TLabel', foreground = 'red')
status_resultados_lbl = ttk.Label(status_resultados_frame, text = 'Resultado: Aguardando informações', font = 'none 9', anchor = W, style = 'status_resultados_text.TLabel')
status_resultados_lbl.grid(row = 0, column = 0, padx = 10)

status_vazio_frame = LabelFrame(statusbar, relief = SUNKEN, bd = 1)
status_vazio_frame.pack(fill = X)
status_vazio_lbl = ttk.Label(status_vazio_frame)
status_vazio_lbl.grid(row = 0, column = 0, padx = 10)


## SOBRE
ttk.Label(sobre, text = 'Calculadora de Metrologia', font = 'none 16 bold').place(relx = 0.5, rely = 0.2, anchor='center')
ttk.Label(sobre, text = 'Gustavo Cardoso Zotin', font = 'none 14').place(relx = 0.5, rely = 0.8, anchor='center')
ttk.Label(sobre, text = 'https://www.linkedin.com/in/gustavozotin/', font = 'none 14').place(relx = 0.5, rely = 0.85, anchor='center')


# # DADOS
frame_dados_SM = LabelFrame(dados, text = 'Dados Sistema de Medição', padx = 10, pady = 5)
frame_dados_SM.pack(expand = TRUE)
frame_outros_dados = LabelFrame(dados, text = 'Outros Dados', padx = 10, pady = 5)
frame_outros_dados.pack(expand = TRUE)

#resolução
res_valor = StringVar()
res_lbl = ttk.Label(frame_dados_SM, text = 'Resolução [mm]:', font = 'none 12')
res_lbl.grid(row=1, column=0, sticky=W, pady = 3)
res_entry = ttk.Entry(frame_dados_SM, textvariable = res_valor, font = 'none 11', width = 10)
res_entry.grid(row = 1, column = 1, padx = 5)
res_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: 0.000000', font = 'none 10').grid(row = 1, column = 2, sticky = W)

#tendência
td_valor = StringVar()
td_lbl = ttk.Label(frame_dados_SM, text = 'Tendência [mm]:', font = 'none 12')
td_lbl.grid(row=2, column=0, sticky=W, pady = 3)
td_entry = ttk.Entry(frame_dados_SM, textvariable = td_valor, font = 'none 11', width = 10)
td_entry.grid(row = 2, column = 1, padx = 5)
td_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: 0.000000', font = 'none 10').grid(row = 2, column = 2, sticky = W)

#incerteza de calibração
Ucal_valor = StringVar()
Ucal_lbl = ttk.Label(frame_dados_SM, text = 'Incerteza de calibração [mm]:', font = 'none 12')
Ucal_lbl.grid(row=3, column=0, sticky=W, pady = 3)
Ucal_entry = ttk.Entry(frame_dados_SM, textvariable = Ucal_valor, font = 'none 11', width = 10)
Ucal_entry.grid(row = 3, column = 1, padx = 5)
Ucal_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: 0.000000', font = 'none 10').grid(row = 3, column = 2, sticky = W)

#fator de abrangência da incerteza de calibração
K_Ucal_valor = StringVar()
K_Ucal_lbl = ttk.Label(frame_dados_SM, text = 'Fator de abrangência da incerteza de calibração (K):', font = 'none 12')
K_Ucal_lbl.grid(row=4, column=0, sticky=W, pady = 3)
K_Ucal_entry = ttk.Entry(frame_dados_SM, textvariable = K_Ucal_valor, font = 'none 11', width = 10)
K_Ucal_entry.grid(row = 4, column = 1, padx = 5)
K_Ucal_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: 0.000000', font = 'none 10').grid(row = 4, column = 2, sticky = W)

#coef dilatação térmica SM
alpha_SM_valor = StringVar()
alpha_SM_lbl = ttk.Label(frame_dados_SM, text = 'Coeficiente de dilatação térmica [μm/(mºC)]:', font = 'none 12')
alpha_SM_lbl.grid(row=5, column=0, sticky=W, pady = 3)
alpha_SM_entry = ttk.Entry(frame_dados_SM, textvariable = alpha_SM_valor, font = 'none 11', width = 10)
alpha_SM_entry.grid(row = 5, column = 1, padx = 5)
alpha_SM_lbl_status = ttk.Label(frame_dados_SM, text = 'Valor atual: 0.000000', font = 'none 10').grid(row = 5, column = 2, sticky = W)

#coef dilatação térmica peça
alpha_peca_valor = StringVar()
alpha_peca_lbl = ttk.Label(frame_outros_dados, text = 'Coeficiente de dilatação térmica [μm/(mºC)]:', font = 'none 12')
alpha_peca_lbl.grid(row=6, column=0, sticky=W, pady = 3)
alpha_peca_entry = ttk.Entry(frame_outros_dados, textvariable = alpha_peca_valor, font = 'none 11', width = 10)
alpha_peca_entry.grid(row = 6, column = 1, padx = 5)
alpha_peca_lbl_status = ttk.Label(frame_outros_dados, text = 'Valor atual: 0.000000', font = 'none 10').grid(row = 6, column = 2, sticky = W)

#temperatura do ambiente de medição
t_amb_valor = StringVar()
t_amb_lbl = ttk.Label(frame_outros_dados, text = 'Temperatura do ambiente de medição [ºC]:', font = 'none 12')
t_amb_lbl.grid(row=7, column=0, sticky=W, pady = 3)
t_amb_entry = ttk.Entry(frame_outros_dados, textvariable = t_amb_valor, font = 'none 11', width = 10)
t_amb_entry.grid(row = 7, column = 1, padx = 5)
t_amb_lbl_status = ttk.Label(frame_outros_dados, text = 'Valor atual: 0.000000', font = 'none 10').grid(row = 7, column = 2, sticky = W)

#erro da temperatura do ambiente de medição
erro_t_amb_valor = StringVar()
erro_t_amb_lbl = ttk.Label(frame_outros_dados, text = 'Incerteza associada a temperatura:', font = 'none 12')
erro_t_amb_lbl.grid(row=8, column=0, sticky=W, pady = 3)
erro_t_amb_entry = ttk.Entry(frame_outros_dados, textvariable = erro_t_amb_valor, font = 'none 11', width = 10)
erro_t_amb_entry.grid(row = 8, column = 1, padx = 5)
erro_t_amb_lbl_status = ttk.Label(frame_outros_dados, text = 'Valor atual: 0.000000', font = 'none 10').grid(row = 8, column = 2, sticky = W)

#botão de enviar dados
dados.button = ttk.Button(dados, text = 'Enviar dados', command = enviar_dados)
dados.button.pack(expand = TRUE)

# # LEITURAS
qtd_leituras_frame = LabelFrame(leituras, borderwidth = 0, pady = 10)
qtd_leituras_frame.pack(expand = TRUE)
valor_leituras_frame = LabelFrame(leituras, text = 'Leituras em milímetros [mm]', pady = 12)
valor_leituras_frame.pack(expand = TRUE)

#quantidade de leituras
qtd_leituras_valor = StringVar()
qtd_leituras_lbl = Label(qtd_leituras_frame, text = 'Indique a quantidade de leituras (1 - 30): ', font = 'none 12')
qtd_leituras_lbl.grid(row = 0, column = 0, padx = 5)
qtd_leituras_entry = ttk.Entry(qtd_leituras_frame,  textvariable = qtd_leituras_valor, font = 'none 11', width = 10)
qtd_leituras_entry.grid(row = 0, column = 1, padx = 5)
botao_qtd_leituras = ttk.Button(qtd_leituras_frame, text = 'Enviar quantidade de leituras', command = enviar_qtd_leituras)
botao_qtd_leituras.grid(row = 0, column = 2, padx = 5)

estado_entradas = ['disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled', 'disabled']

valor_leitura = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

valor_leitura[0] = StringVar()
valor_leitura_01_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #01')
valor_leitura_01_lbl.grid(row = 0, column = 0)
valor_leitura_01_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[0], font = 'none 11', width = 10, state = estado_entradas[0])
valor_leitura_01_entry.grid(row = 1, column = 0, padx = 10)

valor_leitura[1] = StringVar()
valor_leitura_02_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #02')
valor_leitura_02_lbl.grid(row = 0, column = 1)
valor_leitura_02_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[1], font = 'none 11', width = 10, state = estado_entradas[1])
valor_leitura_02_entry.grid(row = 1, column = 1, padx = 10)

valor_leitura[2] = StringVar()
valor_leitura_03_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #03')
valor_leitura_03_lbl.grid(row = 0, column = 2)
valor_leitura_03_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[2], font = 'none 11', width = 10, state = estado_entradas[2])
valor_leitura_03_entry.grid(row = 1, column = 2, padx = 10)

valor_leitura[3] = StringVar()
valor_leitura_04_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #04')
valor_leitura_04_lbl.grid(row = 0, column = 3)
valor_leitura_04_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[3], font = 'none 11', width = 10, state = estado_entradas[3])
valor_leitura_04_entry.grid(row = 1, column = 3, padx = 10)

valor_leitura[4] = StringVar()
valor_leitura_05_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #05')
valor_leitura_05_lbl.grid(row = 0, column = 4)
valor_leitura_05_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[4], font = 'none 11', width = 10, state = estado_entradas[4])
valor_leitura_05_entry.grid(row = 1, column = 4, padx = 10)

valor_leitura[5] = StringVar()
valor_leitura_06_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #06')
valor_leitura_06_lbl.grid(row = 0, column = 5)
valor_leitura_06_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[5], font = 'none 11', width = 10, state = estado_entradas[5])
valor_leitura_06_entry.grid(row = 1, column = 5, padx = 10)

Label(valor_leituras_frame, text = ' ').grid(row = 2)

valor_leitura[6] = StringVar()
valor_leitura_07_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #07')
valor_leitura_07_lbl.grid(row = 3, column = 0)
valor_leitura_07_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[6], font = 'none 11', width = 10, state = estado_entradas[6])
valor_leitura_07_entry.grid(row = 4, column = 0, padx = 10)

valor_leitura[7] = StringVar()
valor_leitura_08_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #08')
valor_leitura_08_lbl.grid(row = 3, column = 1)
valor_leitura_08_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[7], font = 'none 11', width = 10, state = estado_entradas[7])
valor_leitura_08_entry.grid(row = 4, column = 1, padx = 10)

valor_leitura[8] = StringVar()
valor_leitura_09_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #09')
valor_leitura_09_lbl.grid(row = 3, column = 2)
valor_leitura_09_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[8], font = 'none 11', width = 10, state = estado_entradas[8])
valor_leitura_09_entry.grid(row = 4, column = 2, padx = 10)

valor_leitura[9] = StringVar()
valor_leitura_10_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #10')
valor_leitura_10_lbl.grid(row = 3, column = 3)
valor_leitura_10_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[9], font = 'none 11', width = 10, state = estado_entradas[9])
valor_leitura_10_entry.grid(row = 4, column = 3, padx = 10)

valor_leitura[10] = StringVar()
valor_leitura_11_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #11')
valor_leitura_11_lbl.grid(row = 3, column = 4)
valor_leitura_11_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[10], font = 'none 11', width = 10, state = estado_entradas[10])
valor_leitura_11_entry.grid(row = 4, column = 4, padx = 10)

valor_leitura[11] = StringVar()
valor_leitura_12_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #12')
valor_leitura_12_lbl.grid(row = 3, column = 5)
valor_leitura_12_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[11], font = 'none 11', width = 10, state = estado_entradas[11])
valor_leitura_12_entry.grid(row = 4, column = 5, padx = 10)

Label(valor_leituras_frame, text = ' ').grid(row = 5)

valor_leitura[12] = StringVar()
valor_leitura_13_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #13')
valor_leitura_13_lbl.grid(row = 6, column = 0)
valor_leitura_13_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[12], font = 'none 11', width = 10, state = estado_entradas[12])
valor_leitura_13_entry.grid(row = 7, column = 0, padx = 10)

valor_leitura[13] = StringVar()
valor_leitura_14_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #14')
valor_leitura_14_lbl.grid(row = 6, column = 1)
valor_leitura_14_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[13], font = 'none 11', width = 10, state = estado_entradas[13])
valor_leitura_14_entry.grid(row = 7, column = 1, padx = 10)

valor_leitura[14] = StringVar()
valor_leitura_15_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #15')
valor_leitura_15_lbl.grid(row = 6, column = 2)
valor_leitura_15_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[14], font = 'none 11', width = 10, state = estado_entradas[14])
valor_leitura_15_entry.grid(row = 7, column = 2, padx = 10)

valor_leitura[15] = StringVar()
valor_leitura_16_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #16')
valor_leitura_16_lbl.grid(row = 6, column = 3)
valor_leitura_16_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[15], font = 'none 11', width = 10, state = estado_entradas[15])
valor_leitura_16_entry.grid(row = 7, column = 3, padx = 10)

valor_leitura[16] = StringVar()
valor_leitura_17_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #17')
valor_leitura_17_lbl.grid(row = 6, column = 4)
valor_leitura_17_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[16], font = 'none 11', width = 10, state = estado_entradas[16])
valor_leitura_17_entry.grid(row = 7, column = 4, padx = 10)

valor_leitura[17] = StringVar()
valor_leitura_18_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #18')
valor_leitura_18_lbl.grid(row = 6, column = 5)
valor_leitura_18_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[17], font = 'none 11', width = 10, state = estado_entradas[17])
valor_leitura_18_entry.grid(row = 7, column = 5, padx = 10)

Label(valor_leituras_frame, text = ' ').grid(row = 8)
            
valor_leitura[18] = StringVar()
valor_leitura_19_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #19')
valor_leitura_19_lbl.grid(row = 9, column = 0)
valor_leitura_19_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[18], font = 'none 11', width = 10, state = estado_entradas[18])
valor_leitura_19_entry.grid(row = 10, column = 0, padx = 10)

valor_leitura[19] = StringVar()
valor_leitura_20_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #20')
valor_leitura_20_lbl.grid(row = 9, column = 1)
valor_leitura_20_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[19], font = 'none 11', width = 10, state = estado_entradas[19])
valor_leitura_20_entry.grid(row = 10, column = 1, padx = 10)

valor_leitura[20] = StringVar()
valor_leitura_21_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #21')
valor_leitura_21_lbl.grid(row = 9, column = 2)
valor_leitura_21_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[20], font = 'none 11', width = 10, state = estado_entradas[20])
valor_leitura_21_entry.grid(row = 10, column = 2, padx = 10)

valor_leitura[21] = StringVar()
valor_leitura_22_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #22')
valor_leitura_22_lbl.grid(row = 9, column = 3)
valor_leitura_22_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[21], font = 'none 11', width = 10, state = estado_entradas[21])
valor_leitura_22_entry.grid(row = 10, column = 3, padx = 10)

valor_leitura[22] = StringVar()
valor_leitura_23_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #23')
valor_leitura_23_lbl.grid(row = 9, column = 4)
valor_leitura_23_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[22], font = 'none 11', width = 10, state = estado_entradas[22])
valor_leitura_23_entry.grid(row = 10, column = 4, padx = 10)

valor_leitura[23] = StringVar()
valor_leitura_24_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #24')
valor_leitura_24_lbl.grid(row = 9, column = 5)
valor_leitura_24_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[23], font = 'none 11', width = 10, state = estado_entradas[23])
valor_leitura_24_entry.grid(row = 10, column = 5, padx = 10)

Label(valor_leituras_frame, text = ' ').grid(row = 11)

valor_leitura[24] = StringVar()
valor_leitura_25_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #25')
valor_leitura_25_lbl.grid(row = 12, column = 0)
valor_leitura_25_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[24], font = 'none 11', width = 10, state = estado_entradas[24])
valor_leitura_25_entry.grid(row = 13, column = 0, padx = 10)

valor_leitura[25] = StringVar()
valor_leitura_26_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #26')
valor_leitura_26_lbl.grid(row = 12, column = 1)
valor_leitura_26_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[25], font = 'none 11', width = 10, state = estado_entradas[25])
valor_leitura_26_entry.grid(row = 13, column = 1, padx = 10)

valor_leitura[26] = StringVar()
valor_leitura_27_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #27')
valor_leitura_27_lbl.grid(row = 12, column = 2)
valor_leitura_27_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[26], font = 'none 11', width = 10, state = estado_entradas[26])
valor_leitura_27_entry.grid(row = 13, column = 2, padx = 10)

valor_leitura[27] = StringVar()
valor_leitura_28_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #28')
valor_leitura_28_lbl.grid(row = 12, column = 3)
valor_leitura_28_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[27], font = 'none 11', width = 10, state = estado_entradas[27])
valor_leitura_28_entry.grid(row = 13, column = 3, padx = 10)

valor_leitura[28] = StringVar()
valor_leitura_29_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #29')
valor_leitura_29_lbl.grid(row = 12, column = 4)
valor_leitura_29_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[28], font = 'none 11', width = 10, state = estado_entradas[28])
valor_leitura_29_entry.grid(row = 13, column = 4, padx = 10)

valor_leitura[29] = StringVar()
valor_leitura_30_lbl = ttk.Label(valor_leituras_frame, text = 'Leitura #30')
valor_leitura_30_lbl.grid(row = 12, column = 5)
valor_leitura_30_entry = ttk.Entry(valor_leituras_frame, textvariable = valor_leitura[29], font = 'none 11', width = 10, state = estado_entradas[29])
valor_leitura_30_entry.grid(row = 13, column = 5, padx = 10)

#botão de enviar leituras
botao_enviar_leituras = ttk.Button(leituras, text = 'Enviar leituras', command = enviar_leituras)
botao_enviar_leituras.pack(expand = TRUE)

# # RESULTADOS
botao_resultados = ttk.Button(resultados, text = 'Gerar resultado', command = gerar_resultado)
botao_resultados.pack(expand = TRUE)

# Inicia o app
app.mainloop()