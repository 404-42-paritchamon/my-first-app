import streamlit as st

st.title("🛒 แอปคำนวณราคาสินค้ารวม VAT 7%")

menu_prices = {
    "กาแฟอเมริกาโน่": 60.0,
    "ชาไทยเย็น": 55.0,
    "เค้กช็อกโกแลต": 85.0,
    "ครัวซองต์": 65.0,
    "ชาเขียวมัทฉะลาเต้": 75.0
}

# 1. เลือกเมนูที่ต้องการสั่ง
selected_items = st.multiselect(
    "เลือกเมนูที่ต้องการสั่งซื้อ:",
    options=list(menu_prices.keys())
)

total_base_price = 0.0

# 2. ถ้ามีการเลือกเมนู ให้ระบุจำนวน
if selected_items:
    st.write("---")
    st.subheader("ระบุจำนวนสินค้า:")
    
    for item in selected_items:
        price = menu_prices[item]
        qty = st.number_input(f"จำนวน {item} (แก้ว/ชิ้นละ {price:.2f} บาท):", min_value=1, value=1, step=1)
        total_base_price += price * qty

    # 3. คำนวณภาษีและราคาสุทธิ
    vat = total_base_price * 0.07
    net_price = total_base_price + vat

    # 4. แสดงผลลัพธ์
    st.divider()
    st.write(f"• ราคารวมสินค้า: **{total_base_price:.2f}** บาท")
    st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
    st.header(f"• ราคาสุทธิรวม VAT: **{net_price:.2f}** บาท")
else:
    st.info("กรุณาเลือกอย่างน้อย 1 เมนูเพื่อคำนวณราคา")

st.divider()
