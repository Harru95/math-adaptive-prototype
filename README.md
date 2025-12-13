Math Adaptive Learning Prototype

An AI-powered adaptive learning prototype designed to personalize math practice for children (ages 5–10).
The system dynamically adjusts difficulty levels based on user performance using a rule-based adaptive engine.

🚀 Features

Three difficulty levels: Easy, Medium, Hard

Dynamic math puzzle generation

Performance tracking:

Correct/Incorrect

Response time

Real-time difficulty adjustment

End-of-session summary and recommended next difficulty

Clean modular code

Streamlit UI (simple, interactive)

🧠 Adaptive Logic (Rule-Based)

Difficulty increases if:

Accuracy in last 3 questions = 100%

AND average response time < 5 seconds

Difficulty decreases if:

Accuracy < 50%

OR response time > 8 seconds

Otherwise difficulty stays the same.

🗂 Folder Structure
math-adaptive-prototype/
│
├─ README.md
├─ requirements.txt
│
├─ src/
│   ├─ main.py
│   ├─ puzzle_generator.py
│   ├─ adaptive_engine.py
│   └─ tracker.py

📄 File Descriptions
main.py

Front-end logic using Streamlit:

User name input

Number of questions input

Puzzle loop

Difficulty transitions

Summary output

puzzle_generator.py

Creates arithmetic problems based on difficulty level.

adaptive_engine.py

Implements rule-based difficulty transitions using:

Past correctness

Time taken

tracker.py

Stores user performance & generates the final session report.

▶️ Running the App
Install dependencies:
pip install -r requirements.txt

Run Streamlit app:
cd src
streamlit run main.py

📊 Example Flow

User enters name

Chooses total number of questions

Receives a math question

System logs performance

Adaptive engine adjusts difficulty

Summary is displayed after final question

🧪 Sample Summary Output
{
  "name": "Aditya",
  "total_questions": 10,
  "correct": 8,
  "accuracy": 80.0,
  "avg_time": 4.3,
  "path": ["Medium", "Medium", "Hard", "Hard", "Hard"],
  "next_level": "Hard"
}
