🌶️ Resume Roaster – Funny, Brutal & Actually Useful

A small, honest, Hinglish AI tool that roasts your resume and gives actionable fixes — built because I didn’t have proper guidance to make a strong CV.
Upload a PDF/TXT, tell it the role, and get a sharp (200–300 word) roast + real improvements.

Link : https://op-resume-roaster.streamlit.app/

🚀 Why This Exists

I struggled to make a CV that actually lands interviews. Everyone gives vague advice — so I built something that tells you clearly, brutally, sarcastically, yet constructively what to fix.

It’s funny.
It’s harsh.
But it’s actually useful.
Exactly the kind of guidance I needed myself.


🔥 Features

📤 Upload PDF or TXT resumes
🤖 AI-generated roast in Hinglish
✍️ 200–300 word output
📝 Includes:
Top 5 actionable improvements
2 strengths to keep
One-line rewritten summary
😭 Brutal honesty + comedy + practical insights
🌐 Simple Streamlit UI — runs directly in your browser


🧩 Tech Stack

Python 3.10+
Streamlit
Google Gemini API (google-generativeai)
PyPDF2
python-dotenv


📦 Installation & Setup (with uv)
# Clone the repository
git clone https://github.com/pmaheshwari1903/Resume-Roaster
cd Resume-Roaster


# Run the project
uv run main.py

# Sync virtual environment via uv
uv sync

# OR run directly with Streamlit
streamlit run main.py


🔑 Environment Variables

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here


Get your Gemini API key here:
https://aistudio.google.com/app/api-keys


📁 Project Structure
Resume-Roaster/
│── main.py
│── README.md
│── .python-version
│── requirements.txt / pyproject.toml
│── .env   (create this)
│── .gitignore

🧠 How It Works

You upload a resume (PDF/TXT).
Text is extracted using PyPDF2 or direct decoding.
A custom-crafted prompt roasts the resume in Hinglish.
Gemini generates the roast + actionable feedback + summary rewrite.
Result is displayed in a clean Streamlit UI.


🧭 Future Improvements

Export roast as PDF
DOCX resume support
Better UI design
"Before → After" resume comparison


🤝 Contributing

Pull requests are welcome!
If you find bugs or have ideas, feel free to open an issue — I’ll roast those too 😄


📜 License

MIT License — free to use, modify, and roast responsibly.