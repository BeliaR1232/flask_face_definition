from app import app

app.config.update(
    DEBUG=True,
)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
