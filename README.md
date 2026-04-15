<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

<h1>🎓 Career Advisor Chatbot (Gemini API + Streamlit)</h1>

<p>
An AI-powered <b>Career Advisor Chatbot</b> built using <b>Google Gemini API</b> and <b>Streamlit</b>, designed to provide 
<b>precise, short, and practical career guidance</b>.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
    <li>💬 Real-time chat interface using Streamlit</li>
    <li>🎯 Career-focused responses only</li>
    <li>⚡ Fast responses using <b>Gemini 2.5 Flash</b></li>
    <li>⌨️ Typing animation effect</li>
    <li>📥 Download chat history</li>
    <li>🧹 Clear chat functionality</li>
    <li>🎨 Custom avatars for user & bot</li>
</ul>

<hr>

<h2>🧠 How It Works</h2>
<ul>
    <li>Uses a structured system prompt to control AI behavior</li>
    <li>Maintains conversation using session state</li>
    <li>Sends queries to Gemini API via a client class</li>
    <li>Displays responses with streaming typing effect</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>Google Gemini API</li>
    <li>dotenv</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
career-advisor-chatbot/
│── app.py
│── client.py
│── config.py
│── prompts.py
│── ui.py
│── assets/
│    ├── user.png
│    └── bot.png
│── requirements.txt
│── README.md
</pre>

<hr>

<h2>⚙️ Setup & Installation</h2>

<h3>1. Clone Repository</h3>
<pre>
git clone https://github.com/your-username/career-advisor-chatbot.git
cd career-advisor-chatbot
</pre>

<h3>2. Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Add API Key</h3>
<pre>
GEMINI_API_KEY=your_api_key_here
</pre>

<p><b>⚠️ Do NOT upload .env file to GitHub</b></p>

<h3>4. Run the App</h3>
<pre>
streamlit run app.py
</pre>

<hr>

<h2>🌐 Deployment (Streamlit Cloud)</h2>
<ol>
    <li>Push code to GitHub</li>
    <li>Go to Streamlit Cloud</li>
    <li>Add secrets:</li>
</ol>

<pre>
GEMINI_API_KEY = "your_api_key_here"
</pre>

<p>Deploy 🚀</p>

<hr>

<h2>💡 Example Interaction</h2>

<p><b>User:</b><br>
How can I switch to Data Science?</p>

<p><b>Bot:</b><br>
Learn Python, statistics, and ML basics. Build projects and apply for entry-level roles.</p>

<hr>

<h2>🎯 System Behavior</h2>
<pre>
- Answer precisely
- Answer shortly
- Answer only from career perspective
- Give practical advice
</pre>

<hr>

<h2>🔒 Security Best Practices</h2>
<ul>
    <li>API keys stored using .env (local) and Streamlit secrets (deployment)</li>
    <li>.env excluded using .gitignore</li>
    <li>Prevents accidental key leaks</li>
</ul>

<hr>

<h2>🔮 Future Improvements</h2>
<ul>
    <li>🔍 Add conversation memory</li>
    <li>📊 Resume analyzer feature</li>
    <li>🌐 Enhanced UI</li>
    <li>🧠 Vector database integration</li>
</ul>

<hr>

<h2>📈 Learning Outcomes</h2>
<ul>
    <li>Prompt Engineering</li>
    <li>LLM Integration (Gemini API)</li>
    <li>Streamlit Development</li>
    <li>Secure API Handling</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>Feel free to fork and improve the project!</p>

<hr>

<h2>⭐ Support</h2>
<p>If you like this project, give it a ⭐ on GitHub!</p>

👨‍💻 Author

Vaibhav M

GitHub: https://github.com/Vaibhav-9-9-9

</body>
</html>
