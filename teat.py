import random as rd
import streamlit as st

st.write("今晚我想來點？？")

colse_full_rice=["銀記","今華"]
colse_full_noodle=["查無結果"]
colse_rice=["咖食堂","蔣老爹","永和豆漿"]
colse_noodle=["葛瑪莉","小四川"]
colse_other=["永和豆漿","煎餅果子","小四川"]


far_full_rice=["九龍燒臘","新莊燒臘"]
far_full_noodle=["查無結果"]
far_full_other=["查無結果"]
far_rice=["查無結果"]
far_noodle=["查無結果"]
far_other=["塞門甜不辣","永春蚵仔煎","大稻埕肉包","廟街餅店","廟街夜市","饒河夜市","寧夏夜市麻糬冰","新莊漢堡"]



far=st.text_input("1.近(北科) 2.遠 : ")
full=st.text_input("1. 吃飽 2.吃好 : ")
riceORnoodle=st.text_input("1. 飯 2.麵 3.都可 : ")

button=st.button("OK")
if button:
  if far=="1":
    if full=="1":
      if riceORnoodle=="1":
        food=colse_full_rice
      elif riceORnoodle=="2":
        food=colse_full_noodle
      elif riceORnoodle=="3":
        food=colse_full_rice+colse_full_noodle
    elif full=="2":
      if riceORnoodle=="1":
        food=colse_rice
      elif riceORnoodle=="2":
        food=colse_noodle
      elif riceORnoodle=="3":
        food=colse_rice+colse_noodle+colse_other
  elif far=="2":
    if full=="1":
      if riceORnoodle=="1":
        food=far_full_rice
      elif riceORnoodle=="2":
        food=far_full_noodle
      elif riceORnoodle=="3":
        food=far_full_rice+far_full_noodle+far_full_other
    elif full=="2":
      if riceORnoodle=="1":
        food=far_rice
      elif riceORnoodle=="2":
        food=far_noodle
      elif riceORnoodle=="3":
        food=far_rice+far_noodle+far_other
  st.write(rd.choice(food))
