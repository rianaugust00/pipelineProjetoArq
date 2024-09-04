import tkinter as tk
import time
import threading

# Definir os estágios do pipeline e as cores
estagios = ["FI", "DI", "CO", "FO", "EI", "WO"]
cores = ["lightblue", "lightgreen", "lightyellow", "lightcoral", "lightgray", "lightpink"]
colunas = 14  # Número de colunas no pipeline
instrucoes = 9  # Número máximo de instruções

# Função para apagar elementos específicos
def apagar_elementos_especificos(matriz_labels):
    # C8: Apagar L4, L5, L6, L7
    matriz_labels[3][7].config(text="", bg="white")  # L4, C8
    matriz_labels[4][7].config(text="", bg="white")  # L5, C8
    matriz_labels[5][7].config(text="", bg="white")  # L6, C8
    matriz_labels[6][7].config(text="", bg="white")  # L7, C8

    # C9: Apagar L4, L5, L6, L7
    matriz_labels[3][8].config(text="", bg="white")  # L4, C9
    matriz_labels[4][8].config(text="", bg="white")  # L5, C9
    matriz_labels[5][8].config(text="", bg="white")  # L6, C9
    matriz_labels[6][8].config(text="", bg="white")  # L7, C9

    # C10: Apagar L5, L6, L7
    matriz_labels[4][9].config(text="", bg="white")  # L5, C10
    matriz_labels[5][9].config(text="", bg="white")  # L6, C10
    matriz_labels[6][9].config(text="", bg="white")  # L7, C10

    # C11: Apagar L6, L7
    matriz_labels[5][10].config(text="", bg="white")  # L6, C11
    matriz_labels[6][10].config(text="", bg="white")  # L7, C11

    # C12: Apagar L7
    matriz_labels[6][11].config(text="", bg="white")  # L7, C12

# Função para atualizar o pipeline normalmente
def atualizar_pipeline_normalmente(matriz_labels, intervalo=1):
    ciclo = 0
    while True:
        for i in range(len(matriz_labels)):
            estagio_index = ciclo - i
            if 0 <= estagio_index < len(estagios):
                matriz_labels[i][ciclo].config(text=estagios[estagio_index], bg=cores[estagio_index])
            else:
                matriz_labels[i][ciclo].config(text="", bg="white")

        janela.update()  # Atualiza a interface gráfica
        time.sleep(intervalo)
        ciclo += 1

# Função para atualizar o pipeline com interrupção
def atualizar_pipeline_com_interrupcao(matriz_labels, intervalo=1):
    ciclo = 0
    while True:
        for i in range(len(matriz_labels)):
            estagio_index = ciclo - i
            if 0 <= estagio_index < len(estagios):
                matriz_labels[i][ciclo].config(text=estagios[estagio_index], bg=cores[estagio_index])
            else:
                matriz_labels[i][ciclo].config(text="", bg="white")

        apagar_elementos_especificos(matriz_labels)  # Chama a função para apagar os elementos
        janela.update()  # Atualiza a interface gráfica
        time.sleep(intervalo)
        ciclo += 1

# Função para adicionar uma nova linha de instrução
def adicionar_instrucao(matriz_labels, intervalo=2):
    linha_instrucoes = 0
    while linha_instrucoes < instrucoes:
        time.sleep(intervalo)
        if linha_instrucoes < len(matriz_labels):
            # Adiciona nova linha de instrução
            matriz_labels.append([tk.Label(matriz_frame, text="", width=15, height=3, relief="solid", bg="white") for _ in range(colunas)])
            for j, label in enumerate(matriz_labels[linha_instrucoes]):
                label.grid(row=linha_instrucoes + 1, column=j + 1, padx=5, pady=5)  # Ajuste de posição para linha e coluna numerada
        janela.update()  # Atualiza a interface gráfica
        linha_instrucoes += 1

# Função para iniciar a simulação normal
def iniciar_simulacao_normal():
    # Limpar a área da matriz antes de começar
    for widgets in matriz_frame.winfo_children():
        widgets.destroy()

    # Criar as labels para os números de colunas (no topo)
    for col in range(colunas):
        label_col = tk.Label(matriz_frame, text=f"C{col+1}", width=15, height=2, relief="solid", bg="lightgray")
        label_col.grid(row=0, column=col + 1, padx=5, pady=5)

    # Criar uma matriz de labels
    matriz_labels = []
    for i in range(instrucoes):
        # Criar as labels para os números de linhas (na lateral)
        label_linha = tk.Label(matriz_frame, text=f"L{i+1}", width=5, height=3, relief="solid", bg="lightgray")
        label_linha.grid(row=i + 1, column=0, padx=5, pady=5)

        matriz_labels.append([tk.Label(matriz_frame, text="", width=15, height=3, relief="solid", bg="white") for _ in range(colunas)])
        for j, label in enumerate(matriz_labels[i]):
            label.grid(row=i + 1, column=j + 1, padx=5, pady=5)

    # Iniciar a simulação normalmente
    threading.Thread(target=atualizar_pipeline_normalmente, args=(matriz_labels,)).start()
    threading.Thread(target=adicionar_instrucao, args=(matriz_labels,)).start()

# Função para iniciar a simulação com interrupção
def iniciar_simulacao_com_interrupcao():
    # Limpar a área da matriz antes de começar
    for widgets in matriz_frame.winfo_children():
        widgets.destroy()

    # Criar as labels para os números de colunas (no topo)
    for col in range(colunas):
        label_col = tk.Label(matriz_frame, text=f"C{col+1}", width=15, height=2, relief="solid", bg="lightgray")
        label_col.grid(row=0, column=col + 1, padx=5, pady=5)

    # Criar uma matriz de labels
    matriz_labels = []
    for i in range(instrucoes):
        # Criar as labels para os números de linhas (na lateral)
        label_linha = tk.Label(matriz_frame, text=f"L{i+1}", width=5, height=3, relief="solid", bg="lightgray")
        label_linha.grid(row=i + 1, column=0, padx=5, pady=5)

        matriz_labels.append([tk.Label(matriz_frame, text="", width=15, height=3, relief="solid", bg="white") for _ in range(colunas)])
        for j, label in enumerate(matriz_labels[i]):
            label.grid(row=i + 1, column=j + 1, padx=5, pady=5)

    # Iniciar a simulação com interrupção
    threading.Thread(target=atualizar_pipeline_com_interrupcao, args=(matriz_labels,)).start()
    threading.Thread(target=adicionar_instrucao, args=(matriz_labels,)).start()

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Simulação de Pipeline de Instruções")

# Layout dos inputs
input_frame = tk.Frame(janela)
input_frame.pack(pady=10)

# Botão para iniciar a simulação normal
iniciar_button_normal = tk.Button(input_frame, text="Iniciar Simulação Normal", command=iniciar_simulacao_normal)
iniciar_button_normal.grid(row=0, column=0, padx=10, pady=10)

# Botão para iniciar a simulação com interrupção
iniciar_button_com_interrupcao = tk.Button(input_frame, text="Iniciar Simulação com Interrupção", command=iniciar_simulacao_com_interrupcao)
iniciar_button_com_interrupcao.grid(row=0, column=1, padx=10, pady=10)

# Área da matriz de pipeline
matriz_frame = tk.Frame(janela)
matriz_frame.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
