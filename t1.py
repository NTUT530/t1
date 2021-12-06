import streamlit as st

def hello(i,k):
  st.write((k+"\n")*i)

k=st.text_input("str?")
i=int(st.number_input("number?"))
confirm_input=st.button("OK")
if confirm_input:
  hello(i,k)
