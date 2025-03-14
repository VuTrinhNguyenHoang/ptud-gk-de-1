# Thông tin cá nhân sinh viên

- **Trịnh Nguyễn Hoàng Vũ**
- **MSSV: 22642231**
- **STT: 75**

# Mô tả Dự án

Dự án này xây dựng một hệ thống blog đơn giản, cho phép người dùng:
- **Đăng ký & Đăng nhập:** Tạo tài khoản và đăng nhập để sử dụng hệ thống.
- **Đăng tải & Quản lý blog:** Viết blog, hỗ trợ hình ảnh.
- **Dashboard:** Xem các blog của bản thân tại Dashboard.

# Hướng dẫn cài dặt và chạy chương trình

### Tải hệ thống

Clone dự án từ Github:
```bash
git clone https://github.com/VuTrinhNguyenHoang/ptud-gk-de-1.git
```

Vào thư mục hệ thống:
```bash
cd ptud-gk-de-1
```

### Cài đặt mô trường ảo

Trước tiên, đảm bảo bạn đã cài đặt Python (phiên bản ≥ 3.10).

Tạo môi trường ảo:
```bash
python -m venv venv
```

Kích hoạt môi trường ảo:
- Windows: 
    ```bash
    venv\Scripts\activate
    ```

- Ubuntu/Linux:
    ```bash
    source venv/bin/activate
    ```

### Cài đặt thư viện

Cập nhật phiên bản mới nhất của pip trong môi trường ảo:
```bash
python -m pip install --upgrade pip
```

Sau đó, cài đặt các thư viện cần thiết từ `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Chạy chương trình

Khởi chạy chương trình:
```bash
python main.py
```

### Nếu muốn chạy tự động

Chạy file `run.bat`:
```bash
.\run.bat
```

# Link project đã triển khai

- [http://127.0.0.1:5000](http://127.0.0.1:5000)