import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import os

st.set_page_config(page_title="東北地方のWTW", page_icon="🗾", layout="wide")
st.title("東北地方のWTW")

df = pd.read_excel('pref.xlsx')

# 地図の作成
fig = go.Figure(layout=go.Layout(
    mapbox=go.layout.Mapbox(
        style="open-street-map",
        zoom=6,
        center={"lat": 39.164141, "lon": 140.635296},
    ),
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
))

for i, row in df.iterrows():
    # 写真のパスを設定
    img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{row['画像']}")
    print("画像ファイルのパス:", img_path)
    img = Image.open(img_path)
    img.thumbnail((20, 20))  # 画像を20x20にリサイズ

    # マーカーの作成
    fig.add_trace(go.Scattermapbox(
        lat=[row['緯度']],
        lon=[row['経度']],
        mode='markers',
        marker=dict(
            size=15,
            color='red',
            symbol='circle'
        ),
        text=f"<b>{row['名称']}</b><br>{row['名物']}<br><a href='{row['リンク']}' target='_blank'>リンク</a>",
        hovertemplate=f"<b>{row['名称']}</b><br>名物:{row['名物']}<br><a href='{row['リンク']}' target='_blank'>リンク</a>",
        customdata=[row['リンク']],
        name=row['名称']
    ))

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# 画像を横に並べる
col1, col2 = st.columns(2)
with col1:
    st.image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image1.jpg'), caption='WTW仙台', width=100)
with col2:
    st.image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image2.jpg'), caption='WTW秋田', width=100)