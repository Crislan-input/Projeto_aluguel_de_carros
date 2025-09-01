# import streamlit as st

# st.title("Xana Bet's💵") #TITLE e titulo em inglês

# # python -m streamlit run app.py

# st.write("Ou você arrisca na Xana, ou perca a suas tchecas")


import streamlit as st
import pandas as pd

 # python -m streamlit run app.py

 #---------------------------------------------------------------------------------------- Sidebar

st.sidebar.image("logo.png")
st.sidebar.title("CarLans")

carros = ['BMW','Mustang', 'Porsche', 'Fusca', 'Toro']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

#-------------------------------------------------------------------------------------------- Principal
st.title('Car Future - Alugues de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == "BMW":
    diaria = 700

elif opcao == "Mustang":
    diaria = 500

elif opcao == "Porsche":
    diaria = 450

elif opcao == "Fusca":
    diaria = 300

elif opcao == "Toro":
    diaria = 600

    

if st.button('Calcular'): #BUTTON e para criar um botão pra clicar
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km . O valor total a pagar é R${aluguel_total:.2f}')