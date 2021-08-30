
```
FLASK_DEBUG=1 FLASK_APP=app.py python -m flask run
```

```
gunicorn --chdir app app:app -b 0.0.0.0:8000
```
