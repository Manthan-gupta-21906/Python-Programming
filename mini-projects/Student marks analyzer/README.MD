# 📊 Student Marks Analyzer

> A command-line Python tool that analyzes student academic performance — computing totals, averages, subject highs/lows, and auto-assigning grades using NumPy's vectorized operations.

---

## 🎯 The Goal

Remove the manual effort of processing student marks. Built around NumPy, it handles multiple students with different subject counts and produces a clean, structured report instantly — no spreadsheet needed.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Core Library | NumPy |
| Interface | Command-Line (stdin/stdout) |
| Notebook | Google Colab / Jupyter |

---

## ✨ Key Features

- **Multi-student input** — Add any number of students in one session, each with their own name and subject marks
- **Variable subject support** — Each student can have a different number of subjects, handled gracefully
- **NumPy-powered analytics** — Computes total, average, highest, and lowest marks per student using `axis=1` vectorized operations
- **Auto grade assignment** — Grades assigned automatically based on average: `A` (≥85), `B` (≥70), `C` (≥50), `Fail` (<50)
- **Formatted report** — Prints a clean, labeled report for every student with clear separators

---

## 📋 Grade Scale

| Grade | Average Score |
|---|---|
| 🟢 A | ≥ 85 |
| 🔵 B | ≥ 70 |
| 🟡 C | ≥ 50 |
| 🔴 Fail | < 50 |

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/Manthan-gupta-21906/Python-Programming.git
cd Python-Programming/mini-projects/Student\ marks\ analyzer

# Install dependency
pip install numpy

# Run
python marks_analyzer.py
```

Or open `Student_Marks_Analyzer.ipynb` directly in **Google Colab** or **Jupyter Notebook**.

---

## 💻 Sample Output

```
enter number of students to add : 3

enter name of student 1 : karn
enter number of subjects of karn : 2
  Marks for subject 1: 98
  Marks for subject 2: 78

enter name of student 2 : maahi
enter number of subjects of maahi : 2
  Marks for subject 1: 56
  Marks for subject 2: 34

enter name of student 3 : ronit
enter number of subjects of ronit : 2
  Marks for subject 1: 67
  Marks for subject 2: 87

STUDENT MARKS REPORT :
Student  : karn
Total    : 176.0
Average  : 88.0
Highest  : 98.0
Lowest   : 78.0
Grade    : A
-------------------------------------------------------
Student  : maahi
Total    : 90.0
Average  : 45.0
Highest  : 56.0
Lowest   : 34.0
Grade    : Fail
-------------------------------------------------------
Student  : ronit
Total    : 154.0
Average  : 77.0
Highest  : 87.0
Lowest   : 67.0
Grade    : B
-------------------------------------------------------
```

---

## 🧠 How It Works

| Step | What Happens |
|---|---|
| 1. Input | Collects student names and marks into Python lists via loops |
| 2. Storage | Converts the list of lists into a NumPy 2D array |
| 3. Calculation | Applies `np.sum`, `np.mean`, `np.max`, `np.min` with `axis=1` — one result per student |
| 4. Grading | Passes each student's average into a grade function with if/elif/else logic |
| 5. Display | Loops through all students and prints a formatted report for each |

---

## 🧩 Code Structure

```
marks_analyzer.py
│
├── get_student_details()   # Collects names and marks via input
├── store_numpy()           # Converts Python list → NumPy array
├── calculate()             # Returns total, average, max, min per student
├── grade()                 # Returns letter grade from average score
└── display()               # Prints the final formatted report
```

---

## 🔑 Key Concept — axis=1

```python
total   = np.sum(marks2,  axis=1)   # sum across each row (per student)
average = np.mean(marks2, axis=1)   # mean across each row
max_    = np.max(marks2,  axis=1)   # highest subject score per student
min_    = np.min(marks2,  axis=1)   # lowest subject score per student
```

`axis=1` means "operate across columns within each row" — giving one result per student instead of per subject.

---

## 📌 Future Improvements

- Export report to `.csv` or `.pdf`
- Load student data from a file instead of manual input
- Add subject names alongside marks
- Visualize results with `matplotlib` bar charts

---

*Built as part of a Python fundamentals + NumPy learning journey.*