import streamlit as st
from complements import *
from config import *

def historic(num):
    '''Distribute the values in the dictionary table'''
    if num == 1:
        mon_last = money[-1]
        table['Categoria'].append(category)
        table['Despesas R$'].append('---')
        table['Receita Gerada R$'].append(f'{mon_last:.2f}')
    elif num == 2:
        expen_last = expenses[-1]
        table['Categoria'].append(category)
        table['Despesas R$'].append(f'{expen_last:.2f}')
        table['Receita Gerada R$'].append('---')

def calculate():
    '''Distributes the values received from the input'''
    if category in cat_entr:
        money.append(values)
        total.append(values)
        historic(1)
    else:
        expenses.append(values)
        historic(2)

# Open style.css

with open('style.css', 'r',encoding="utf-8") as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Title 

st.title(":bar_chart: Sistema Financeiro")
st.markdown("""-----""")

# Sidebar

st.sidebar.title("Opição")
st.sidebar.markdown("""-----
Criado Por: ## User Name ##""")

# Row A

col1, col2, col3 = st.columns(3)
col1.metric("Saldo", f'{sum(money):.2f} R$',"+ Entrada")
col2.metric("Despesas", f'{sum(expenses):.2f} R$' ,"- Saída")
col3.metric("Total", f'{sum(total)-sum(expenses):.2f} R$', "Resumo","off")

# Row B

cOl1, cOl2, cOl3 = st.columns(3)
with cOl1:
    check_box_1 = st.checkbox(label = "Entrada", help = "Entrada de valores como Salário e Ganhos",disabled = key_lock_box1 )

    if check_box_1:
        cat_empty = cat_entr
        key_lock = False
        key_lock_box2 = True
        
    check_box_2 = st.checkbox(label = "Saída",  help = "Saida de valores como Despesas e Dividas", disabled = key_lock_box2)

    if check_box_2:
        cat_empty = cat_exit
        key_lock = False

with cOl2:
    category = st.selectbox(label = "Categorias", options = cat_empty, disabled = key_lock)

with cOl3:
    values = st.number_input(label = "Insira Valores", min_value = 0.0, disabled = key_lock, )
    botton_add = st.button(label = "+ Adicionar", on_click = calculate, disabled = key_lock )

# Row C
st.markdown('#### :chart_with_upwards_trend: Histórico dos Valores Aplicados')

st.table(table)
