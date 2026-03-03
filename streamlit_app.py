import streamlit as st
st.title("Basis Tracker")
f = st.number_input("Future", value=5335.90)
s = st.number_input("Spot", value=5321.94)
m = st.number_input("Manual Diff", value=14.0)
rt = f - s
drift = rt - m
st.metric("Basis RT", f"{rt:.2f}")
st.metric("Drift Gap", f"{drift:.2f}")
st.write("---")
st.write("Zone 5350: เจ้ามือเก็บของ")
st.write("Zone 5400: รายย่อยเล่นเยอะ")
