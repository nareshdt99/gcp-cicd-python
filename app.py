from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello GKE</title>
        <style>
            body, html {
                height: 100%;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #f06, #48f);
                font-family: 'Arial', sans-serif;
            }

            h1 {
                font-size: 3em;
                color: #fff;
                text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
                animation: glow 1.5s ease-in-out infinite alternate;
            }

            @keyframes glow {
                from {
                    text-shadow: 0 0 10px #fff, 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff;
                }
                to {
                    text-shadow: 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #00ffff, 0 0 50px #00ffff;
                }
            }
        </style>
    </head>
    <body>
        <h1>Hello, GKE! Pipeline Completed! congrats</h1>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

