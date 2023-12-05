import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('./Label/CICDS_Wednesday.csv')
# print(data)
# print("\n", data.info())

data_attack = data[data[' Label'] != 'BENIGN']
# print("\n", data_attack[' Label'].value_counts())

data_classify = data.groupby([' Timestamp', ' Destination IP', ' Label']).size().reset_index(name=' Count')
# print("\n", data_classify[data_classify[' Label'] != 'BENIGN'])

st.title("Visualize Attack Types with Bar Chart")
st.write("Pilih jenis serangan yang ingin dilihat")
st.write("Analisis data ini berdasarkan dataset CICDS_Wednesday.csv")
page_select = st.selectbox("Pilih menu :", ["All Attack Types", "DoS Hulk", "DoS GoldenEye", "DoS Slowhttptest", "DoS slowloris", "Heartbleed"])

list_label = ['DoS Hulk', 'DoS GoldenEye', 'DoS Slowhttptest', 'DoS slowloris', 'Heartbleed']

if page_select in list_label:
    st.subheader(page_select)
    fig = px.bar(data_classify[data_classify[' Label'] == page_select], x=' Timestamp', y=' Count', color=' Label')
    st.plotly_chart(fig)
    st.subheader(f"Summary {page_select}")
    st.dataframe(data_classify[data_classify[' Label'] == page_select])
    st.subheader("Serangan terbesar pada jenis serangan" + " " + page_select)
    sort = data_classify[data_classify[' Label'] == page_select].sort_values(by=' Count', ascending=False)
    st.write(sort.head(1))

else:
    st.subheader("All Attack Types")
    fig = px.bar(data_classify[data_classify[' Label'] != 'BENIGN'], x=' Timestamp', y=' Count', color=' Label')
    st.plotly_chart(fig)
    st.subheader("Summary All Attack Types")
    st.dataframe(data_classify[data_classify[' Label'] != 'BENIGN'])
    st.subheader("Summary Total Attack Types")
    label_counts = data_attack[' Label'].value_counts()
    st.write(label_counts)

st.subheader("Kelompok 5")
st.markdown('''
        - 2210511044 - Rahman Ilyas Al Kahfi
        - 2210511046 - Hanifah Az Zahra
        - 2210511048 - Moza Rizki Ilahi
        - 2210511056 - Adinda Rizki Sya'bana Diva
        - 2210511079 - Harits Muhammad Ramadhan
        ''')