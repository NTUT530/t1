import streamlit as st

page_bg_img="<style>
body{
background-image:url("https://i2.oubafeng.com/c310dd/984e8ba3/98168beb452e5e0fbe69.jpg");


def hello(i,k):
  st.write((k+"\n")*i)

k=st.text_input("str?")
i=int(st.number_input("number?"))
buttom=st.button("OK")
if buttom:
  hello(i,k)
