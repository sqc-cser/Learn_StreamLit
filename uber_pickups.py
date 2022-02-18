import time

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
DATE_COLUMN = 'date/time'
DATA_URL = 'data.csv'

# @st.cache可以把数据存到缓存中，每次刷新都可以读取缓存中的数据，加快速度
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')  # 更改文字
# data_load_state.text("Done! (using st.cache)")
st.subheader('Number of pickups by hour')  # 确定最繁忙的接送时间
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]  # numpy 生成直方图
st.bar_chart(hist_values)

# hour_to_filter = 17  # 查看最繁忙时期的接送地图情况
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
# 动态查看不同时期的地图
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)



