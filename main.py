import streamlit as st

st.write("Percobaan Pertama")

st.write('*Ini contoh huruf miring*')
st.write('**Ini contoh huruf tebal**')
st.write('***Ini contoh huruf tebal dan miring***')

penjualan_oktober = 900
penjualan_november = 850
penjualan_desember = 1000

selisih1 = penjualan_desember - penjualan_november
selisih2 = penjualan_november - penjualan_oktober

st.metric(label='Penjualan Sekarang', value= penjualan_desember, delta = selisih1)
st.metric(label='Penjualan Sebelumnya', value= penjualan_november, delta = selisih2)

#Membaca Dataset
import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv('healthcare-dataset-stroke-data.csv')
st.dataframe(df)

st.write('**2. Visualisasi data - jumlah pasien berdasarkan usia**')
st.line_chart(df['age'].value_counts().sort_index())

st.write('**3. Visualisasi data - Tipe pekerjaan**')
st.bar_chart(df['work_type'].value_counts().sort_index())


st.write('**4. Visualisasi data - jenis kelamin**')

category_df = df['gender'].value_counts(dropna=False).reset_index()
category_df.columns = ['gender','count']

fig = px.pie(category_df, names='gender', values='count')
st.plotly_chart(fig, use_container_width=True)

# 5. Interaktif Komponen
st.write('**5. Button**')
st.button("Reset", type = 'primary')
if st.button('Say Hello'):
    st.write('Why Hello There')
else:
    st.write("Goodbye")

if st.button("Aloha", type = 'tertiary'):
    st.write("Ciao")

# 6. Checkbox
st.write("**6. Checkbox**")
agree = st.checkbox('I Agree')
if agree:
    st.write("Great!")

# 7. Multiselect
st.write("**7. Multiselect**")
options = st.multiselect(
    "What are your favorite colors",
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow','Red'],
)
st.write("You Selected :",options)

#8. Slider
st.write("**8. Slider**")
start_tyres, end_tyres = st.select_slider(
    "Pilih komponen ban untuk race pekan ini",
    options = [
        'Hyper Soft',
        'Ultra Soft',
        'Super Soft',
        'Soft',
        'Medium',
        'Hard',
        'Super Hard',
    ],
    value=['Hyper Soft','Soft']
)
st.write('Anda memilih', start_tyres, 'dan', end_tyres)

#9. Toggle
st.write("**9. Toggle**")
on = st.toggle("Activate feature")
if on:
    st.write("Feature Activated!")

#10. Number Input
st.write('**10. Number Input**')
number = st.number_input(
    "Insert a number", value = None, placeholder = "Type a number...."
)
st.write("The current number is ", number)

#11. Date Input
st.write("**11. Data Input**")
import datetime
d = st.date_input("When's your birthday", datetime.date(1999,9,14))
st.write("Your Birthday Is :", d)

# 12. Image
st.write("*12. Input Image*")
link = "https://infomakassar.id/wp-content/uploads/2025/04/rumah-sakit-di-kota-makassar-800x471.jpg"
st.image(link, caption="Rumah Sakit")

# 13. Membuat Kolom
st.write("**13. Membuat Kolom**")
col1, col2 = st.columns(2)

with col1:
    st.write("**Jumlah Pasien Berdasarkan Usia")
    st.line_chart(df['age'].value_counts().sort_index())

with col2:
    st.write('**3. Visualisasi data - Tipe pekerjaan**')
    st.bar_chart(df['work_type'].value_counts().sort_index())

# 14. Membuat Tab
st.write("**14. Membuat Tab**")
tab1, tab2 = st.tabs(['Line','Bar'])

with tab1:
    st.write("**Jumlah Pasien Berdasarkan Usia**")
    st.line_chart(df['age'].value_counts().sort_index())

with tab2:
    st.write('**Visualisasi data - Tipe pekerjaan**')
    st.bar_chart(df['work_type'].value_counts().sort_index())

# 15. Expander
st.write("**15. Expander**")
with st.expander("See Explanation"):
    st.write('''Quaxwell melatih kaki dan pinggangnya dengan terus berlari di perairan dangkal. Pokémon ini saling mengadu keindahan teknik serangan kaki dengan sesamanya.''')
    st.image("https://id.portal-pokemon.com/play/resources/pokedex/img/pm/dc53be94c2fed43efd89aa83b2c3edaf1a1ecdd1.png")

