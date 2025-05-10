import streamlit as st
import os
from utils import Player, HuntingParty, TAXA_MERCADO, LootResponse

# TODO: Adicionar opção de escolher entre loot com premium acc ou sem
# TODO: adicionar uma coluna para o silver pois não tem taxa
st.title("Calculadora de Loot do Albion")


def limpar_todos(jogadores):
    for i in range(len(jogadores)):
        # st.session_state[f"nome_{i}"] = ""
        st.session_state[f"retorno_{i}"] = 0.0
        st.session_state[f"reparo_{i}"] = 0.0
        st.session_state[f"loot_{i}"] = 0.0
        st.session_state[f"silver_{i}"] = 0.0

    # Botão deve ser renderizado antes dos inputs

# Função para calcular resultados
def calcular_resultados(jogadores: list[Player]) -> list[LootResponse]:
    resultados = []
    hunt = HuntingParty()
    for jogador in jogadores:
        hunt.total_cost += jogador.return_cost + jogador.repair_cost
        hunt.total_loot += jogador.loot
        # hunt.add_player(jogador)
    hunt.loot_with_discount = hunt.total_loot * TAXA_MERCADO

    hunt.profit_per_player = (hunt.loot_with_discount - hunt.total_cost) / len(jogadores) if jogadores else 0

    # Soma ao lucro de cada jogador os custos da hunt
    for jogador in jogadores:
        jogador.proportional_profit = hunt.profit_per_player + jogador.return_cost + jogador.repair_cost

    for jogador in jogadores:
        lucro_liquido = jogador.loot - jogador.return_cost - jogador.repair_cost
        resultados.append(
            LootResponse(
                name=jogador.name,
                liquid_profit=lucro_liquido,
                proportional_profit=jogador.proportional_profit,
                loot_with_discount=jogador.loot_com_desconto
            )
        )
    # breakpoint()
    return resultados


def main():
    # Escolher o número de jogadores
    num_jogadores = st.number_input("Número de jogadores", min_value=1, step=1)

    # Guardar dados dos jogadores
    jogadores = []

    # Criar campos dinamicamente para cada jogador
    for i in range(int(num_jogadores)):
        st.subheader(f"Jogador {i+1}")
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            nome = st.text_input(f"Nome do Jogador", key=f"nome_{i}")
        with col2:
            custo_retorno = st.number_input(f"Custo Retorno", key=f"retorno_{i}", min_value=0.0)
        with col3:
            custo_reparo = st.number_input(f"Custo Reparo", key=f"reparo_{i}", min_value=0.0)
        with col4:
            loot = st.number_input(f"Loot Pessoa", key=f"loot_{i}", min_value=0.0)
        with col5:
            silver = st.number_input(f"Silver", key=f"silver_{i}", min_value=0.0)
        player = Player(
            name = nome,
            return_cost= custo_retorno,
            repair_cost= custo_reparo,
            loot = loot,
            loot_com_desconto = loot * TAXA_MERCADO,
            silver = silver
        )
        jogadores.append(player)

    # Botão para calcular
    st.button("Limpar Todos", on_click=limpar_todos, args=(jogadores,))

    if st.button("Calcular"):
        resultados = calcular_resultados(jogadores)
        st.write("### Resultados")
        for resultado in resultados:
            if resultado.proportional_profit < 0:
                st.write(f"{resultado.name}: Tem que ficar com um total de = {resultado.proportional_profit:.2f} (Perda)")
                st.write(f"Loot com desconto de {resultado.name}: {resultado.loot_with_discount}")
            else:
                st.write(f"{resultado.name}: Tem que ficar com um total de = {resultado.proportional_profit:.2f}")
                st.write(f"Loot com desconto de {resultado.name}: {resultado.loot_with_discount}")
                lucro_positivo = resultado.proportional_profit - resultado.loot_with_discount
                if lucro_positivo >= 0:
                    st.write(f"{resultado.name}: deve receber {lucro_positivo:.2f}")
                    st.write("=====================================================")
                else:
                    st.write(f"{resultado.name}: deve pagar {abs(lucro_positivo):.2f}")
                    st.write("=====================================================")


main()    
    