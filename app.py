#import streamlit as st
#st.title("Olá, eu sou gangster")
#st.sidebar.title("sou fã do matuê")
#st.sidebar.image("matue.png")

import streamlit as st
st.title("Veloz Motors - Aluguel de Carros")
st.sidebar.title("Escolha o seu Modelo ")
st.sidebar.image("logo.png")

carros = ["Nissan Skyline GT-R","Toyota Supra","Dodge Challenger","Chevrolet Impala 70"]

opcao = st.sidebar.selectbox("Escolha o carro que deseja alugar", carros)

st.image(f"{opcao}.png")
st.markdown(f"## Você alugou o modelo: {opcao}")
st.markdown("-----------------------------------")

dias = st.text_input(f"Por quantos dias o {opcao} foi alugado?")
km = st.text_input(f"Quantos km você rodou com o {opcao}?") 

if opcao == "Nissan Skyline GT-R":
    diaria = 8000

elif opcao == "Toyota Supra":
    diaria = 4000

elif opcao == "Dodge Challenger":
    diaria = 2500

elif opcao == "Chevrolet Impala 70": 
    diaria = 5000    

if st.button("Cacular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f"Você alugou o {opcao} por {dias} dias que rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}")
    