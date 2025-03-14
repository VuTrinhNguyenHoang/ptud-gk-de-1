@echo off

REM Khởi tạo môi trường ảo để tránh xung đột khi chạy ứng dụng
echo Create Venv...
python -m venv venv

REM Kích hoạt môi trường ảo
call venv\Scripts\activate.bat

REM Nâng cấp pip trong môi trường ảo
python -m pip install --upgrade pip

REM Cài đặt các thư viện cần thiết
pip install -r requirements.txt

REM Chạy ứng dụng Flask từ file main.py
python main.py

REM Tạm dừng cửa sổ để bạn xem thông báo hoặc lỗi
pause