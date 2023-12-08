import streamlit as st
import requests
import pandas as pd
import numpy as np
import json
import time

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("## 精准气象数据查询")
st.markdown("---")
device_list = [0,1,2,3,4,5]
Station_number = ("K1957","K1992","K1993","K1994","K1995","K1996")
mac = ['K1957','K1992','K1993','K1994','K1995','K1996']

r12c1,r12c2 = st.columns(2)
with r12c1:
    selectbox1 = st.selectbox("设备MAC地址", device_list)
with r12c2:
    selectbox2 = st.selectbox("设备桩号", Station_number)
    if selectbox2:
        selectbox2
        

if st.button("刷新"):
    response = requests.get("http://182.140.146.130:9999/opening-up/query/latest/weather-data/mqtt?deviceMac=611809f5313549d7")

    st.json(response.text)
    data = json.loads(response.text)
    st.markdown("---")

    # 循环处理每个数据点
    df = pd.DataFrame(data["data"])
    df = df.drop(["device_name", "device_type_name", "device_id","attribute_id"], axis=1)
    # 将 "time" 列中的时间戳转换为格式化的日期时间字符串
    df["time"] = pd.to_datetime(df["time"], unit="ms")  # 假设时间戳是以毫秒为单位的

    # 使用 st.dataframe 显示带有样式的 DataFrame
    st.table(df)
    

