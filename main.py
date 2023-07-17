import streamlit as st

import page.insert as insert
import page.select as select
import paga.delete as delete 

#criando a barra lateral do menu
st.sidebar.title('Menu')
selectbox = st.sidebar.selectbox('ação', ['inserir', 'consultar', 'deletar'])

if selectbox == 'inserir':
    insert.inserir()

if selectbox == 'consultar':
    select.consultar()

if selectbox == 'deletar':
    delete.deletar()