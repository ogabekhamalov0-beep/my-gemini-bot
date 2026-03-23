# Python'ning barqaror versiyasini tanlaymiz
FROM python:3.10-slim

# Ishchi katalogni belgilaymiz
WORKDIR /app

# Kerakli tizim paketlarini o'rnatamiz
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt ni nusxalaymiz va kutubxonalarni o'rnatamiz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Qolgan barcha fayllarni nusxalaymiz
COPY . .

# Botni ishga tushiramiz
CMD ["python", "main.py"]
