import streamlit as st
import pandas as pd

st.set_page_config(page_title="Basis Tracker By Long Chawanit")

st.title("📊 The Basis Tracker")
st.write("By LONG CHAWANIT")

# ส่วนรับข้อมูล
f_price = st.number_input("Future Price (F)", value=5335.90)
s_price = st.number_input("Spot Price (S)", value=5321.94)
manual_diff = st.number_input("Manual Diff", value=14.00)
block_dist = st.number_input("Block Distance", value=25)

# คำนวณ
basis_rt = f_price - s_price
drift_gap = basis_rt - manual_diff

# แสดงผล
st.divider()
c1, c2 = st.columns(2)
c1.metric("Basis RT", f"{basis_rt:.2f}")
c2.metric("Drift Gap", f"{drift_gap:.2f}")

# ตาราง Grid
st.subheader("🎯 Grid Zones")
base_f = (f_price // block_dist) * block_dist
levels = [base_f + (block_dist * i) for i in range(2, -3, -1)]

grid_data = []
for lvl in levels:
    grid_data.append({
            "Future": f"{lvl:.0f}",
                    "Spot Order": f"{(lvl - manual_diff):.2f}"
                        })

                        st.table(pd.DataFrame(grid_data))
                        