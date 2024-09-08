import tkinter as tk  #interfaces gráficas
import time  #temporização
import threading  #executar várias tarefas ao mesmo tempo

estagios = ["FI", "DI", "CO", "FO", "EI", "WO"] 
cores = ["lightblue", "lightgreen", "lightyellow", "lightcoral", "lightgray", "lightpink"] 
colunas = 14
instrucoes = 9

# Função para apagar elementos específicos da matriz
def apagar_elementos_especificos(matriz_labels):
    apagar_lista = [(3, 7), (4, 7), (5, 7), (6, 7), (3, 8), (4, 8), (5, 8), (6, 8),
                    (4, 9), (5, 9), (6, 9), (5, 10), (6, 10), (6, 11)]
    #Apaga o conteúdo das células especificadas
    for i, j in apagar_lista:
        matriz_labels[i][j].config(text="", bg="white") 

# Função que atualiza o pipeline em cada ciclo
# Se "com_interrupcao" for True, elementos específicos são apagados
def atualizar_pipeline(matriz_labels, intervalo=1, com_interrupcao=False):
    ciclo = 0 
    while True:
        for i in range(len(matriz_labels)):
            estagio_index = ciclo - i 
            if 0 <= estagio_index < len(estagios):  # Verifica se o estágio está dentro dos limit=es
                # Atualiza a célula com o nome do estágio e a cor correspondente
                matriz_labels[i][ciclo].config(text=estagios[estagio_index], bg=cores[estagio_index])
            else:
                
                matriz_labels[i][ciclo].config(text="", bg="white")

        # Se a simulação tiver interrupção, apaga elementos específicos
        if com_interrupcao:
            apagar_elementos_especificos(matriz_labels)

        janela.update()  # Atualiza
        time.sleep(intervalo)
        ciclo += 1 



#Inicia uma nova thread para atualizar o pipeline usando a função fornecida (atualizacao_func).
# Função para iniciar a simulação (normal ou com interrupção)
def iniciar_simulacao(atualizacao_func):
    matriz_frame.winfo_children().clear()

    # Cria as labels das colunas no topo da matriz
    for col in range(colunas):
        tk.Label(matriz_frame, text=f"C{col+1}", width=15, height=2, relief="solid", bg="lightgray").grid(row=0, column=col+1, padx=5, pady=5)

    # Cria as linhas da matriz e adiciona labels para cada célula
    matriz_labels = []
    for i in range(instrucoes):
        # Cria labels para as linhas na lateral
        tk.Label(matriz_frame, text=f"L{i+1}", width=5, height=3, relief="solid", bg="lightgray").grid(row=i+1, column=0, padx=5, pady=5)
        # Cria as células da matriz e as insere na grid
        linha = [tk.Label(matriz_frame, text="", width=15, height=3, relief="solid", bg="white") for _ in range(colunas)]
        matriz_labels.append(linha)
        for j, label in enumerate(linha):
            label.grid(row=i + 1, column=j + 1, padx=5, pady=5)

    # Inicia a atualização do pipeline em uma nova thread
    threading.Thread(target=atualizacao_func, args=(matriz_labels,)).start()




#f  unções para Iniciar Simulações

def iniciar_simulacao_normal():
    iniciar_simulacao(lambda matriz: atualizar_pipeline(matriz, intervalo=1))

def iniciar_simulacao_com_interrupcao():
    iniciar_simulacao(lambda matriz: atualizar_pipeline(matriz, intervalo=1, com_interrupcao=True))

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Simulação de Pipeline de Instruções")

# Layout para os botões de controle
input_frame = tk.Frame(janela)
input_frame.pack(pady=10)

tk.Button(input_frame, text="Iniciar Simulação Normal", command=iniciar_simulacao_normal).grid(row=0, column=0, padx=10, pady=10)
tk.Button(input_frame, text="Iniciar Simulação com Interrupção", command=iniciar_simulacao_com_interrupcao).grid(row=0, column=1, padx=10, pady=10)

# Frame que vai conter a matriz de pipeline
matriz_frame = tk.Frame(janela)
matriz_frame.pack(padx=10, pady=10)

# Inicia o loop principal da interface gráfica (aguardando interações do usuário)
janela.mainloop()