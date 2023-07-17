import streamlit as st

import controller.cliente as cliente


def deletar():
    st.title('deletar dados')

    with st.form(key= 'insert'):
        input_mat = st.text_input(label='insira a matricula:')

        buttom_submit = st.form_submit_button('enviar')

        if buttom_submit:
            cliente.deletar(input_mat)
            st.success('programador excluido com sucesso')