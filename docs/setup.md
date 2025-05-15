
---

# ⚙️ Setup & Usage

## 🖥️ Local Development

1. **Create a virtual environment**

   ```bash
   python -m venv venv ----------
   source venv/bin/activate -------
   pip install -r requirements.txt
   ```

2. **Configure environment variables**

   Create a `.env` file in the project root and add the following (update values as needed):

   ```bash
DATABASE_HOST= # IP address of the database host,
DATABASE_PORT=___________,
DATABASE_USER=___________,
DATABASE_PASSWORD=********,
DATABASE_NAME=____________
```


3. **Start the application**

   ```bash
   fastapi dev app/main.py
   ```

---

## 🐳 Docker

1. **Build the Docker image**

   ```bash
   docker build -t expense-tracker .
   ```

2. **Run the Docker container**

   Pass the `.env` file if needed:

   ```bash
   docker run --env-file .env -p 8000:8000 expense-tracker
   ```

