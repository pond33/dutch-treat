# 割り勘計算アプリ

import streamlit as st
import math

# 最初にメッセージを表示
st.write("お疲れ様です！今日は何を割り勘しますか？")

# 入力を受け付ける
total_amount = st.number_input("合計金額（円）", min_value=0, step=100)
num_people = st.number_input("人数", min_value=1, step=1)

if st.button("計算する"):
    if num_people > 0:
        # 割り勘の計算（100円単位で四捨五入）
        base_amount = round(total_amount / num_people, -2)  # 100円単位で四捨五入
        remainder = total_amount - (base_amount * num_people)  # 端数を計算

        if remainder == 0:
            # ぴったり割り切れる場合
            result_text = f"全員 {base_amount} 円ずつ支払います。"
        else:
            # 端数がある場合
            extra_amount = base_amount + 100  # 多めに払う金額
            num_extra_people = remainder // 100  # 100円多めに払う人数
            num_base_people = num_people - num_extra_people  # 通常の金額を払う人数

            result_text = f"{num_base_people} 人が {base_amount} 円、{num_extra_people} 人が {extra_amount} 円支払います。"

        # 結果を表示（目立つ色で大きく）
        st.markdown(f"<h2 style='text-align: center; color: cyan;'>{result_text}</h2>", unsafe_allow_html=True)




