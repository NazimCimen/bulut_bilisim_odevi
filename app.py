from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bulut Bilişim ve DevOps Teknolojileri Dersi Ödevi-merhaba'

if __name__ == '__main__':
    app.run()