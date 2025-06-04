import streamlit as st

st.set_page_config(layout="wide")
st.title("⚽ Painel de Apostas (Versão Offline - Simulada)")

# Dados simulados
jogos = [
    {
        "fixture": {"status": {"long": "Match Finished"}},
        "teams": {
            "home": {"name": "Flamengo", "winner": True},
            "away": {"name": "Corinthians", "winner": False}
        }
    },
    {
        "fixture": {"status": {"long": "Match Finished"}},
        "teams": {
            "home": {"name": "Palmeiras", "winner": False},
            "away": {"name": "Grêmio", "winner": True}
        }
    },
    {
        "fixture": {"status": {"long": "Match Finished"}},
        "teams": {
            "home": {"name": "Atlético-MG", "winner": None},
            "away": {"name": "Bahia", "winner": None}
        }
    }
]

st.markdown("### Jogos simulados")
for jogo in jogos:
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
