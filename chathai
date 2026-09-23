import streamlit as st

st.title("🛒 แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%")

# 1. กำหนดรายการเมนูและราคา
menu_prices = {
    "กาแฟอเมริกาโน่": 60.0,
    "ชาไทยเย็น": 55.0,
    "เค้กช็อกโกแลต": 85.0,
    "ครัวซองต์": 65.0,
    "ชาเขียวมัทฉะลาเต้": 75.0
}

# 2. Dropdown สำหรับเลือกเมนู
selected_item = st.selectbox("เลือกรายการเมนู:", list(menu_prices.keys()))

# 3. เลือกจำนวนชิ้น
quantity = st.number_input("จำนวน (ชิ้น):", min_value=1, value=1, step=1)

# 4. คำนวณราคา
base_price = menu_prices[selected_item] * quantity
vat = base_price * 0.07
net_price = base_price + vat  # รวมภาษีเพิ่มเข้าไป

# 5. แสดงผลลัพธ์
st.write(f"**รายการที่เลือก:** {selected_item} ({quantity} ชิ้น)")
st.write(f"• ราคาก่อน VAT: **{base_price:.2f}** บาท")
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิรวม VAT: **{net_price:.2f}** บาท")

st.divider()
