import streamlit as st
import requests
import pandas as pd
import numpy as np
import json
import time

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

url = "http://182.140.146.130:9999/opening-up/query/latest/weather-data/mqtt?deviceMac="

st.markdown("## 精准气象数据查询")
st.markdown("---")
device_list = [0,1,2,3,4,5]
Station_number = ("K1957+300","K1963+100","K1964+450","K1985+100",
                    "K1992+400","K1996+200", "K2000+000", "K2032+350",
                    "K2086+900", "K2093+550", "K2100+750", "K2105+000",
                    "K2108+750", "K2115+500", "K2118+950", "K2128+000",
                    "K2000+001", "K2100+100")
mac = ("611809f5301e49d7", "613474bc4b2241d7", "5d7132651f1711d7", "614b4791153729d7",
        "611809f5400b49d7", "611809f5313549d7", "5d7132651c4109d7", "611809f5282649d7",
        "613474bc1c1d41d7", "5d713265114209d7", "613474bc312341d7", "5d713265051611d7",
        "5d713265204209d7", "614b4791360f31d7", "5d7132651c1611d7", "5d7132651a1511d7",
        "613474bc151d41d7", "5d713265181611d7")

dict_dev = dict(zip(Station_number, mac))
st.write(dict_dev)

update = 0
df = 0
res_data = 0
selectboxT = st.selectbox("设备桩号", Station_number)
if selectboxT:
    # st.write(dict_dev[selectboxT])
    url = url+dict_dev[selectboxT]
    st.write(url)
    response = requests.get(url)
    res_data = json.loads(response.text)
    st.markdown("---")
    update = 1
    df = pd.DataFrame(res_data["data"])
    df = df.drop(["device_name", "device_type_name","attribute_id"], axis=1)
    # 将 "time" 列中的时间戳转换为格式化的日期时间字符串
    df["time"] = pd.to_datetime(df["time"], unit="ms")  # 假设时间戳是以毫秒为单位的


# selectbox1 = st.selectbox("设备桩号", mac)
# if selectbox1:
#     url = url+selectbox1
#     st.write(url)
#     response = requests.get(url)
#     res_data = json.loads(response.text)
#     st.markdown("---")
#     update = 1
#     df = pd.DataFrame(res_data["data"])
#     df = df.drop(["device_name", "device_type_name","attribute_id"], axis=1)
#     # 将 "time" 列中的时间戳转换为格式化的日期时间字符串
#     df["time"] = pd.to_datetime(df["time"], unit="ms")  # 假设时间戳是以毫秒为单位的    

if st.button("刷新"):
    response = requests.get(url)
    res_data = json.loads(response.text)
    st.markdown("---")

    # 循环处理每个数据点
    df = pd.DataFrame(res_data["data"])
    df = df.drop(["device_name", "device_type_name","attribute_id"], axis=1)
    # 将 "time" 列中的时间戳转换为格式化的日期时间字符串
    df["time"] = pd.to_datetime(df["time"], unit="ms")  # 假设时间戳是以毫秒为单位的

    update = 1
    
if update == 1:
    update = 0
    # 使用 st.dataframe 显示带有样式的 DataFrame
    st.table(df)
    st.json(res_data)


