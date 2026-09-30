from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Simple HTML page
HTML_PAGE = """
<h2>AI Study Buddy - Vetri Thiran Payirchi Thittam</h2>
<p>Project by savithirimurugan23</p>
<form action="/ask" method="post">
  <input type="text" name="question" placeholder="Un doubt ah ketta?" style="width:300px; padding:8px;">
  <button type="submit">Ask AI</button>
</form>
<p>{{ answer }}</p>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE, answer="")

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question')
    # Demo answer - Gemini API key add panna original answer varum
    answer = f"Ungal kelvi: '{question}' ku answer - AI Study Buddy ready! Gemini API connect panna full answer kudukkum."
    return render_template_string(HTML_PAGE, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
