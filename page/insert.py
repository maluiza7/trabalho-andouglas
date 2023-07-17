import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('preencha com seus dados e **GANHA O PREMIO**')
    bandeira = ['mastercard', 'visa', 'elo']
    produto = ['tv 72 polegadas', 'iphone 14', 'pc gamer']    
    
    with st.form(key='insert'):
        input_cpf = st.text_input(label='Insira seu cpf')
        input_name = st.text_input(label='insira o numero do cartão:')
        input_cartao = st.text_input(label='insira a bandeira do cartão', options=bandeira)
        input_cvv = st.text_input(label='codigo cvv do cartão')
        input_produto = selectbox(label= 'ESCOLHA O PRODUTO QUE VOCE GANHOU', options=produto)
                 
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir()(input_cpf, input_name, input_job, input_cvv, input_produto)
            st.success('clientes incluido com sucesso')