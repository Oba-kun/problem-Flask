from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')

def hello():
  return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
  amount = int(request.form["amount"])

#ここの計算が反映されない
  if amount <= 1000:
      print("落札できました。")
  else:
      print("不落です。")


  return render_template('index.html',amount = amount)

