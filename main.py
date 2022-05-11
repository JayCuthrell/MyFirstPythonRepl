from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_flask():
  return render_template("index.html", content="Hello Flask")

app.run(host='0.0.0.0', port=8080)
