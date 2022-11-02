from flask import Flask, escape, request, render_template# Import flask libraries
import pickle  # Importing the python file containing the ML model

vector=pickle.load(open("vectorizer.pkl",'rb'))
model = pickle.load(open("finalized_model.pkl",'rb'))

app = Flask(__name__)# Initialize the flask class

@app.route('/')# Default route set as 'home'
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
       
       
        predict = model.predict(vector.transform([news]))
        
          
        return render_template("prediction.html",prediction_text="News Headline is ->{}".format(predict))
    else:
        return render_template("prediction.html")

if __name__ == '__main__':# Run the Flask server
    app.run()
