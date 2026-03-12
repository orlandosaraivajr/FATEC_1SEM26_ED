import time
import random
import pickle


# --- Recuperando a lista do arquivo binário ---
with open("dados_lista.bin", "rb") as f:
    lista = pickle.load(f)

with open("dados_dict_nome.bin", "rb") as f:
    dicionario_nome = pickle.load(f)

with open("dados_dict_cpf.bin", "rb") as f:
    dicionario_cpf = pickle.load(f)

# Escolher um nome aleatório da lista para buscar
alvo_nome, alvo_phone, alvo_cpf = random.choice(lista)

print(f"\nBuscando pelo nome: {alvo_nome}")

# --- Busca na lista (O(n)) ---
inicio = time.time()
resultado_lista = None
for nome, telefone, cpf in lista:
    if nome == alvo_nome:
        resultado_lista = telefone
        break
fim = time.time()
print(f"Busca na lista → Telefone: {resultado_lista}")
print(f"Tempo gasto (lista): {fim - inicio:.6f} segundos")

# --- Busca no dicionário (O(1)) ---
inicio = time.time()
resultado_dict = dicionario_nome.get(alvo_nome)
fim = time.time()
print(f"\nBusca no dicionário → Telefone: {resultado_dict}")
print(f"Tempo gasto (dicionário): {fim - inicio:.6f} segundos")

# --- Busca no dicionário (O(1)) ---
inicio = time.time()
resultado_dict = dicionario_cpf.get(alvo_cpf)
fim = time.time()
print(f"\nBusca no dicionário → Telefone: {resultado_dict}")
print(f"Tempo gasto (dicionário): {fim - inicio:.6f} segundos")
