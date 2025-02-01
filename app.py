import streamlit as st

# タイトルを表示
st.title("割り勘計算機")

# 入力フォーム
amount = st.number_input("合計金額を入力", min_value=0)
people = st.number_input("人数を入力", min_value=1)

# 割り勘計算
if amount > 0 and people > 0:
    share = amount / people
    st.write(f"1人あたりの金額は {share:.2f} 円です。")
else:
    st.write("金額と人数を入力してください。")
import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app!")

