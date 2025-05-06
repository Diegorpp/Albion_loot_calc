import streamlit as st

st.title("Calculadora de Loot do Albion")

# Função para calcular resultados
def calcular_resultados(jogadores):
    resultados = []
    gasto_total = 0
    loot_total = 0
    for jogador in jogadores:
        gasto_total += jogador["custo_retorno"] + jogador["custo_reparo"]
        loot_total += jogador["loot"]
    # print(f"Gasto total: {gasto_total}")
    # print(f"Loot total: {loot_total}")

    lucro_por_jogador = (loot_total - gasto_total) / len(jogadores) if jogadores else 0
    print(f"Lucro por jogador: {lucro_por_jogador}")

    for jogador in jogadores:
        lucro_proporcional = lucro_por_jogador + jogador['custo_retorno'] + jogador['custo_reparo']
        jogador["lucro_proporcional"] = lucro_proporcional

    for jogador in jogadores:
        lucro_liquido = jogador["loot"] - jogador["custo_retorno"] - jogador["custo_reparo"]
        resultados.append({
            "nome": jogador["nome"],
            "lucro_liquido": lucro_liquido,
            "lucro_proporcional": jogador["lucro_proporcional"]
        })
    return resultados

# Escolher o número de jogadores
num_jogadores = st.number_input("Número de jogadores", min_value=1, step=1)

# Guardar dados dos jogadores
jogadores = []

# Criar campos dinamicamente para cada jogador
for i in range(int(num_jogadores)):
    st.subheader(f"Jogador {i+1}")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        nome = st.text_input(f"Nome do Jogador {i+1}", key=f"nome_{i}")
    with col2:
        custo_retorno = st.number_input(f"Custo Retorno {i+1}", key=f"retorno_{i}", min_value=0.0)
    with col3:
        custo_reparo = st.number_input(f"Custo Reparo {i+1}", key=f"reparo_{i}", min_value=0.0)
    with col4:
        loot = st.number_input(f"Loot Pessoa {i+1}", key=f"loot_{i}", min_value=0.0)

    jogadores.append({
        "nome": nome,
        "custo_retorno": custo_retorno,
        "custo_reparo": custo_reparo,
        "loot": loot,
    })

# Botão para calcular
if st.button("Calcular"):
    resultados = calcular_resultados(jogadores)
    st.write("### Resultados")
    for resultado in resultados:
        if resultado["lucro_proporcional"] < 0:
            st.write(f"{resultado['nome']}: Tem que ficar com um total de = {resultado['lucro_proporcional']:.2f} (Perda)")
        else:
            st.write(f"{resultado['nome']}: Tem que ficar com um total de = {resultado['lucro_proporcional']:.2f}")
