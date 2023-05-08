#必要なライブラリをインポート
import streamlit as st
import numpy as np
import pandas as pd


#タイトルとテキストを入力

st.title('Sreamlot 基礎')
st.write('Hellow world')

#データフレームの準備

df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

st.dataframe(df)

#引数を使用した動的テーブル
st.dataframe(df.style.highlight_max(axis = 0), width = 100, height = 400)

#10行3列のデータフレームを準備

df =- pd.DataFrame(
    np.random.rand(10,3),
    columns = ['a','b','c']
)
df

#折れ線グラフ
st.line_chart(df)

#面グラフ
st.area_chart(df)

#棒グラフ
st.bar_chart(df)

#マップをプロット

df_map = pd.DataFrame(
    np.random.rand(100,2) / [50, 50]+[35.69, 139.70],
    columns = ['lat', 'lon']
)

st.map(df_map)

#Pillow
from PIL import Image
img = Image.open('iris.jpg')
st.image(img,caption = 'Iris', use_column_width = True)

#チェックボックス

if st.checkbox('Show Image'):
    img = Image.open('iris.jpg')
    st.image(img, caption = 'Iris', use_column_width = True)

#セレクトボックス

option = st.selectbox(
    '好きな数字を入力してください',
    list(range(1,11))
)

'あなたの好きな数字は',option,'です。'

#テキスト入力による動的なデータの入力

text = st.text_input('あなたの好きなスポーツを教えてください')

'あなたの好きなスポーツ:',text

#スタイダーによる動的な値の変更

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション:', condition

#プルダウン表示

expander1 = st.expander('質問1')
expander1.write('質問1の答え')
expander2 = st.expander('質問2')
expander2.write('質問2の答え')
expander3 = st.expander('質問3')
expander3.write('質問3の答え')

#プログレスバーの表示

import time

latest_iteration = st.empty()
bar = st.progress(0)

#プログレスバーを0,1秒ごとに進める

for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'


