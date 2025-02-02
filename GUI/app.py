from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

app = Flask(__name__)

# Load the saved model and tokenizer
 # Path to your saved model directory
model_path = "D:\Text-Summarization-Project\GUI\Finetuned-model"
tokenizer_path ="D:\Text-Summarization-Project\GUI\Finetuned-model-tokenizer"

model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
# Create the summarization pipeline
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        summary = summarizer(text, max_length=100)[0]["summary_text"]  # Adjust max_length as needed
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)