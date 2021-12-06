import streamlit as st

def hello(i,k):
  st.write((k+"\n")*i)

k=st.text_input("str?")
i=int(st.number_input("number?"))
buttom=st.button("OK")
if buttom:
  hello(i,k)
