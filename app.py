from platform import processor
import streamlit as st
import numpy as np
import joblib

model = joblib.load("rf_model.pkl")

st.title("Dự đoán giá laptop")

st.divider()

st.write("Với ứng dụng này, sau khi bạn ấn nút tính toán và đã nhập đầy đủ các nội dung như bộ xử lý, RAM size, bộ nhớ thì app sẽ đưa ra mức giá dự đoán cho bạn")

st.divider()

processor_speed = st.number_input("Nhập bộ xử lý", value=2.50, step=0.50)
ram_size = st.number_input("Nhập dung lượng RAM", value=16, step=8)
storage_capacity = st.number_input("Nhập dung lượng bộ nhớ", value=512, step=256)

x = processor_speed, ram_size, storage_capacity

st.divider()

prediction = st.button("Dự đoán giá")

st.divider()

if prediction:
    st.balloons()
    x1 = np.array(x)
    prediction = model.predict([x1])[0]
    st.write(f"Giá dự đoán của laptop: {prediction:,.2f} ₫")  # sửa định dạng và từ 'latop' => 'laptop'
else:
    st.write("Vui lòng chọn nút dự đoán giá để tính toán")
    