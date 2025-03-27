from flask import Flask, request, render_template
from qwen import Qwen

app = Flask(__name__)
model = Qwen()

# Load common phishing wordlists
with open('phishing_wordlist.txt', 'r') as file:
    phishing_words = set(file.read().splitlines())

def analyze_email(email_text):
    # Check for common phishing words
    words = set(email_text.split())
    common_words = words.intersection(phishing_words)
    if common_words:
        return f"Phishing Detected! Common words: {', '.join(common_words)}"
    else:
        # Use Qwen for further analysis
        response = model.generate(f"Analyze this email for phishing: {email_text}")
        return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    email_text = request.form['email_text']
    result = analyze_email(email_text)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
