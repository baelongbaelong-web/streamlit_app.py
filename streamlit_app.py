import streamlit as st
import pandas as pd

# ตั้งค่าหน้าแอป
st.set_page_config(page_title="Basis Tracker By Long Chawanit", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FFD700;'>📊 The Basis Tracker</h1>", unsafe_allow_api_html=True)
st.markdown("<p style='text-align: center;'>By LONG CHAWANIT</p>", unsafe_allow_api_html=True)

# ส่วน Sidebar สำหรับกรอกข้อมูล
with st.sidebar:
    st.header("⚙️ ตั้งค่าข้อมูล")
        f_price = st.number_input("Future Price (F)", value=5335.90, format="%.2f")
            s_price = st.number_input("Spot Price (S)", value=5321.94, format="%.2f")
                manual_diff = st.number_input("Manual Diff (ตอกตะปู)", value=14.00, format="%.2f")
                    block_dist = st.number_input("Block Distance", value=25)

                    # คำนวณค่า Basis
                    basis_rt = f_price - s_price
                    drift_gap = basis_rt - manual_diff

                    # ส่วน Dashboard แสดงผล
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Basis RT (Auto)", f"{basis_rt:.2f}")
                        with col2:
                            st.metric("Drift Gap", f"{drift_gap:.2f}", delta=f"{drift_gap:.2f}", delta_color="inverse")

                            st.info(f"Market State: {'CONTANGO' if basis_rt > 0 else 'BACKWARDATION'}")

                            # ตาราง Grid Zone
                            st.subheader("🎯 Buy/Sell Zones (Spot Prices)")
                            base_f = (f_price // block_dist) * block_dist
                            levels = [base_f + (block_dist * i) for i in range(2, -3, -1)]

                            grid_data = []
                            for lvl in levels:
                                grid_data.append({
                                        "Future Level": f"{lvl:.0f}",
                                                "Spot Order": f"{(lvl - manual_diff):.2f}",
                                                        "Action": "🔴 Sell Zone" if lvl > f_price else "🔵 Buy Zone"
                                                            })

                                                            st.table(pd.DataFrame(grid_data))

                                                            # ส่วน Insights
                                                            st.divider()
                                                            st.subheader("💡 Vol2Vol Insights")
                                                            st.write("- **Zone 5350:** OI +9 | Churn 0.75 (สะสมของจริง)")
                                                            st.write("- **Zone 5400:** OI 318 | Churn 0.13 (เล่นสั้นเยอะ)")
                                                            