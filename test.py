# 使用streamlit run your_script.py [-- script args] 运行网页代码
# test.py 试用streamlit包
import streamlit as st
import pandas as pd
import numpy as np
import time

dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)
# st.table(dataframe)  # 静态数据
data = pd.read_excel('data.xlsx',header=None)
data.drop(index=[0,1,2],inplace=True)
data = data[3]

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df  # 这里的magic相当于st.wirte(df)

st.write("# My first app Hello *world*")  # st.write 采用Markdown类似写法
st.text("# hello") # st.text 写入的是原始文本
st.line_chart(data)

'''添加小组件进行互动'''
number = st.slider("选择一个数字", 0, 50) # 选择数字
# file = st.file_uploader("选择文件上传") # 添加文件
color = st.color_picker(label='选择一种颜色') # 选择颜色
# st.altair_chart(mychart)  # 柱状图
genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))  # 选择题
date = st.date_input("Pick a date") # 选择日期

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.map(map_data) # 绘制地图

# txt = st.text_input("Your name", key="name") # 输入文本
# print(txt)

# if st.checkbox('Show dataframe'): # checkbox是一个是否选中的状态,在此处取值为True、False
#     # do something
#     st.write('I am OK')

# option = st.selectbox(  # 多选题
#     'Which number do you like best?',
#      df['first column'])
# 'You selected: ', option

add_selectbox = st.sidebar.selectbox(  # 侧边栏sidebar
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# left_column, right_column = st.columns(2) # columns 可以并排堆放小组件
# left_column.button('Press me!')
#
# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

# 'Starting a long computation...'
# latest_iteration = st.empty()
# bar = st.progress(0)  # 使用st.progress来绘制进度条
#
# for i in range(100):
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)
#
# '...and now we are done!'

