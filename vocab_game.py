import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน Session State
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "game_active" not in st.session_state:
    st.session_state.game_active = False


def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False
    st.session_state.game_active = True  # เริ่มเปิดระบบนับเวลา


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    if u_ans3 == "coconut":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "key":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    # แก้ไขเกณฑ์การชนะให้เป็น 4 คะแนนเต็ม
    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. การจัดการส่วนเวลานับถอยหลัง
if st.session_state.get("game_active", False) and not st.session_state.get(
    "is_ended", False
):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.session_state.game_active = False
        st.subheader("⏰ หมดเวลาแล้ว!")
        st.rerun()

st.divider()

# 3. ช่องกรอกข้อมูล (แก้ไข value ของข้อ 4 ให้ถูกต้อง)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: This drink is very refreshing ` c _ _ o n _ t `. 🥥",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: Unlock the door ` k _ _ `. 🔑",
    value=st.session_state.ans4_val,  # แก้เป็น ans4_val แล้ว
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# 4. ปุ่มส่งคำตอบ
if st.session_state.get("game_active", False) and not st.session_state.get(
    "is_ended", False
):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.session_state.game_active = False
        st.rerun()

    # ย้ายมาทำ rerun ตรงนี้เฉพาะตอนที่กำลังเล่นเกม เพื่อใช้อัปเดตตัวเลขเวลาบนหน้าจอ
    time.sleep(1)
    st.rerun()

# แสดงหน้าต่างสรุปผลเมื่อจบเกม
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.write("นางสาวปริชมน จันทาเทพ เลขที่ 42 ม.4/4")
