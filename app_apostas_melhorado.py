
import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("⚽ Painel de Apostas com Dados Reais - API-Football")

API_KEY = "a67eaca42fdba245d0bd993fc07d72fd"
HEADERS = {
    "x-apisports-key": API_KEY
}

# Ligas disponíveis
ligas = {
    71: "Brasileirão Série A",
    40: "Premier League",
    135: "Serie A (Itália)",
    78: "Bundesliga",
    61: "Ligue 1 (França)"
}

# Seletor de data
data_opcao = st.selectbox("Escolha a data para análise:", ("Hoje", "Amanhã", "Ontem"))
if data_opcao == "Hoje":
    data_busca = datetime.today()
elif data_opcao == "Amanhã":
    data_busca = datetime.today() + timedelta(days=1)
else:
    data_busca = datetime.today() - timedelta(days=1)

data_formatada = data_busca.strftime("%Y-%m-%d")
st.write(f"🔎 Data selecionada: {data_formatada}")

# Seletor de ligas
ligas_escolhidas = st.multiselect("Escolha as ligas:", options=list(ligas.keys()), format_func=lambda x: ligas[x], default=[71])

def buscar_jogos(league_id):
    url = "https://v3.football.api-sports.io/fixtures"
    params = {
        "date": data_formatada,
        "league": league_id,
        "season": 2024
    }
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json().get("response", [])
    return []

def analisar_jogo(jogo):
    try:
        time_casa = jogo['teams']['home']['name']
        time_fora = jogo['teams']['away']['name']
        status = jogo['fixture']['status']['long']
        st.subheader(f"{time_casa} x {time_fora}")
        st.write(f"Status: {status}")

        stats_home = jogo['teams']['home']['winner']
        stats_away = jogo['teams']['away']['winner']

        if stats_home is True:
            st.write("📌 Sugestão de aposta: ✅ Vitória do time da casa")
        elif stats_away is True:
            st.write("📌 Sugestão de aposta: ✅ Vitória do time visitante")
        else:
            st.write("⚠️ Sugestão: Dupla chance ou empate")
        st.markdown("---")
    except Exception as e:
        st.error(f"Erro ao analisar jogo: {e}")

total_jogos = 0
for liga in ligas_escolhidas:
    jogos = buscar_jogos(liga)
    if jogos:
        st.markdown(f"## 🏆 {ligas[liga]} — {len(jogos)} jogo(s)")
        total_jogos += len(jogos)
        for jogo in jogos:
            analisar_jogo(jogo)

if total_jogos == 0:
    st.info("Nenhum jogo disponível para análise na data e ligas selecionadas.")
