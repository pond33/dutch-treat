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
        # 100円単位で四捨五入した基本の金額
        base_amount = round(total_amount / num_people, -2)
        
        # 100円単位で丸めた後の合計金額との差を計算
        adjusted_total = base_amount * num_people
        remainder = total_amount - adjusted_total

        if remainder == 0:
            # ぴったり割り切れる場合
            result_text = f"全員 {base_amount} 円ずつ支払います。"
        else:
            # 余りがある場合
            num_extra_people = abs(remainder) // 100  # 100円多く払う人数
            if remainder > 0:
                extra_amount = base_amount + 100  # 追加分を足した金額
            else:
                extra_amount = base_amount - 100  # 少なく払う場合

            num_base_people = num_people - num_extra_people  # 基本額を払う人数

            result_text = f"{num_base_people} 人が {base_amount} 円、{num_extra_people} 人が {extra_amount} 円支払います。"

        # 結果を表示（見やすく）
        st.markdown(f"<h2 style='text-align: center; color: yellow;'>{result_text}</h2>", unsafe_allow_html=True)




