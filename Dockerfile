# Sử dụng image Python chính thức
FROM python:3.10

# Cập nhật và cài đặt các phụ thuộc hệ thống
RUN apt-get update && apt-get install -y \
    wget \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Thiết lập môi trường
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Cài đặt các gói Python
WORKDIR /app
RUN pip install --no-cache-dir \
        fastapi \
        "uvicorn[standard]" \
        moviepy==2.1.2 \
        ffmpeg-python==0.2.0 \
        pydub==0.25.1 \
        requests \
        curl-cffi==0.13.0 \
        pcloud==1.3 \
        mediafire==0.6.1 \
        pytz==2024.2 \
        aspose-compressor==0.0.4

# Sao chép mã nguồn
COPY ./app.py /app/app.py

# Chuẩn hóa thụt lề (tùy chọn)
RUN find . -type f -name "*.py" -exec sed -i 's/\t/    /g' {} +

# Mở cổng
EXPOSE 7860

# Chạy ứng dụng
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860", "--reload"]
