import streamlit as st                      # streamlit
from streamlit_folium import st_folium      # streamlitでfoliumを使う
import folium                               # folium
import pandas as pd                         # CSVをデータフレームとして読み込む

#st.write("東北地方のWTW")

# ページ設定
st.set_page_config(
    page_title="東北地方のWTW",
    page_icon="🗾",
    layout="wide"
)

# 地図の中心の緯度/経度、タイル、初期のズームサイズを指定します。
m = folium.Map(
    # 地図の中心位置の指定(今回は宮城gi県の県庁所在地を指定)
    location=[38.26889, 140.87194], 
    # タイル、アトリビュートの指定
    tiles='https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png',
    attr='都道府県庁所在地、名称、リンク',
    # ズームを指定
    zoom_start=8
)

# 表示するデータを読み込み
df = pd.read_excel('pref.xlsx')

# 読み込んだデータ(緯度・経度、ポップアップ用文字、アイコンを表示)
# 修正する時用に残す
#=====
#for i, row in df.iterrows():
    # ポップアップの作成(都道府県名＋都道府県庁所在地＋名称)
    # pop=f"{row['都道府県名']}({row['都道府県庁所在地']})<br>　名称…{row['名称']}<br>　リンク…{row['リンク']}"
    # folium.Marker(
#=====

# マーカーを追加
for idx, row in df.iterrows():
    # ポップアップの作成(国名＋人数)
    pop = f"{row['都道府県名']}<br>　名称…{row['名称']}<br>　<a href='{row['リンク']}' style='text-decoration:underline;'>{row['リンク']}</a>"
    folium.Marker(

        # 緯度と経度を指定
        location=[row['緯度'], row['経度']],
        # ツールチップの指定(都道府県名)
        tooltip=row['名称'],
        # ポップアップの指定
        popup=folium.Popup(pop, max_width=300),
        # アイコンの指定(アイコン、色)
        icon=folium.Icon(icon="home",icon_color="white", color="red")
    ).add_to(m)

st_data = st_folium(m, width=1200, height=800)