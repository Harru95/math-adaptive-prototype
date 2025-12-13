# Math Adaptive Learning Prototype

An AI-powered adaptive learning system designed to personalize math practice for children (ages 5–10).  
The system dynamically adjusts difficulty levels using a simple rule-based engine.

---

## 🚀 Features
- Three difficulty levels: Easy, Medium, Hard
- Dynamic math question generation
- Performance tracking (correctness + response time)
- Automatic difficulty adjustment
- End-of-session performance summary
- Streamlit user interface
- Clean modular Python code

---

## 🧠 Adaptive Logic (Rule-Based)

Difficulty increases if:
- Last 3 questions are 100% correct
- AND average response time is under 5 seconds

Difficulty decreases if:
- Accuracy is under 50%
- OR average response time is above 8 seconds

Otherwise: difficulty stays the same.

---

## 📁 Project Structure

\`\`\`
math-adaptive-prototype/
│
├─ README.md
├─ requirements.txt
│
├─ src/
│   ├─ main.py               # Streamlit app
│   ├─ puzzle_generator.py   # Math question generator
│   ├─ adaptive_engine.py    # Difficulty adjustment engine
│   └─ Performance_Tracker.py            # Performance tracker + summary
\`\`\`

---

## 📄 File Descriptions

### main.py
- Handles Streamlit UI  
- Takes user name and question count  
- Runs the question loop  
- Tracks correctness  
- Adjusts difficulty  
- Produces final report  

### puzzle_generator.py
- Generates math puzzles based on difficulty  
- Easy → small integer addition/subtraction  
- Medium → larger numbers  
- Hard → multiplication/division  

### adaptive_engine.py
- Implements rule-based difficulty adjustment  
- Uses last 3 answers (correctness + response time)

### Performance_Tracker.py
- Tracks correctness & response time  
- Computes accuracy + average time  
- Stores difficulty path  
- Produces session summary  

---

## ▶️ Running the App

Install dependencies:  
\`\`\`
pip install -r requirements.txt
\`\`\`

Run the Streamlit app:  
\`\`\`
cd src
streamlit run main.py
\`\`\`

---

## 📊 Example Session Summary

\`\`\`
{
  "name": "Harsh",
  "total_questions": 10,
  "correct": 7,
  "accuracy": 70.0,
  "avg_time": 5.31,
  "path": ["Medium", "Medium", "Hard", "Medium", "Medium"],
  "next_level": "Medium"
}
\`\`\`

---

## 🎯 Learning Outcomes
- Adaptive learning logic  
- Real-time difficulty scaling  
- Rule-based personalization  
- Modular architecture  
- Streamlit app workflow  

---
## 🔮 Future Enhancements
- ML-based difficulty prediction (Logistic Regression / Decision Tree)
- Reinforcement Learning for adaptive difficulty adjustment
- Progress graphs and visual analytics
- More question types (word problems, geometry, multiplication, etc.)
- Long-term student profile + personalized learning trajectories

---

## 🙌 Author
Harsh Soni  
GitHub: https://github.com/Harru95  
