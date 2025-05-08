Start server:
```bash
python3 main.py
```

Upload file:
```bash
curl -T <PATH_TO_FILE> http://localhost:8000
```

File should be uploaded to `uploads` directory located next to `main.py` (the directory will be created automatically if it does not exist).
