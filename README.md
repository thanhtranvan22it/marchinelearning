1.Mô tả dự án: Hệ thống dự đoán bệnh dựa trên các triệu chứng được cung cấp bởi người dùng. Mô hình học máy sử dụng SVM (Support Vector Machine) để dự đoán một trong số hơn 40 loại bệnh phổ biến, dựa vào 132 triệu chứng được định nghĩa.
2.Công nghệ sử dụng:
a.Python
b.Scikit-learn (SVM - sklearn.svm.SVC)
c.Pickle (lưu và tải mô hình)
d.NumPy
e.Pandas
3.Các chức năng chính:
a.Nhập các triệu chứng người dùng gặp phải
b.Dự đoán bệnh có khả năng cao nhất
c.iển thị tên bệnh và các thông tin liên quan (tùy triển khai)
4.Cấu trúc thư mục
├── model/
│   └── svc.pkl                  # Mô hình SVM đã huấn luyện và lưu
├── data/
│   └── training.csv             # Dữ liệu huấn luyện (triệu chứng - bệnh)
├── app.py                       # File chính chạy dự đoán
├── README.md                    # Tài liệu dự án
├── requirements.txt             # Thư viện cần thiết
5.Cách chạy dự án
a.CLone về máy 
git clone https://github.com/yourusername/disease-prediction-ml.git
cd disease-prediction-ml
b.Cài thư viện
pip install -r requirements.txt
c.Chạy file chính
streamlit run app.py
