# 📰 Rule-Based Fake News Detector

## 📌 Overview

This project is a **rule-based Fake News Detector** that identifies potentially misleading or fake content based on common patterns found in clickbait and suspicious text.

Instead of using machine learning, this system relies on **handcrafted rules and scoring logic** to classify text as **“Fake” or “Real.”**

---

## 🎯 Objective

To understand the fundamentals of:

* Natural Language Processing (NLP)
* Feature engineering
* Rule-based classification systems

---

## 🧠 How It Works

The system analyzes input text and assigns a **score** based on predefined fake news indicators.

### 🚩 Indicators Used

1. **Clickbait Words**

   * Examples:
     `BREAKING`, `SHOCKING`, `SECRET`, `EXPOSED`, `YOU WON`

2. **Excessive Punctuation**

   * Multiple `!!!`, `???`, etc.

3. **All Caps Words**

   * Words written fully in uppercase (e.g., `FREE MONEY`)

4. **Emotional/Exaggerated Language**

   * Phrases like:
     `"This will change your life forever"`

5. **Suspicious Phrases**

   * Examples:
     `"Doctors hate this"`
     `"Government doesn't want you to know"`

---

## ⚙️ Methodology

### Step 1: Input

* User provides a text string (news headline, paragraph, etc.)

### Step 2: Preprocessing

* Convert text to lowercase
* Tokenize into words

### Step 3: Feature Detection

* Check for presence of predefined indicators

### Step 4: Scoring System

Each feature contributes to a total score:

| Feature                | Score |
| ---------------------- | ----- |
| Clickbait word         | +2    |
| Suspicious phrase      | +3    |
| Excess punctuation     | +2    |
| ALL CAPS word          | +1    |
| Emotional exaggeration | +2    |

### Step 5: Classification

```
if score > threshold:
    return "Fake News (High Probability)"
else:
    return "Likely Real"
```

---

## 🧪 Example

### Input:

```
"BREAKING!!! You won $10000!!! Click now!!!"
```

### Output:

```
Fake News (High Probability)
Score: 9
Reasons:
- Clickbait words detected
- Excessive punctuation
- Suspicious phrasing
```

---

## 📂 Project Structure

```
fake-news-detector/
│
├── main.py                # Main script
├── rules.py               # Indicator lists
├── test_cases.txt         # Sample inputs
├── README.md              # Project documentation
```

---

## 🚀 Features

* Rule-based classification (no ML required)
* Explainable output (why it’s fake)
* Lightweight and fast
* Easy to extend with new rules

---

## ⚠️ Limitations

* No real understanding of context
* Can be fooled by cleverly written fake news
* Depends heavily on predefined rules
* Not as accurate as machine learning models

---

## 🔥 Future Improvements

* Add sentiment analysis
* Use TF-IDF or basic ML models
* Build a simple web interface
* Add confidence percentage
* Expand rule database

---

## 🧠 Key Learnings

* How classification systems work
* Importance of feature engineering
* Trade-offs between rule-based vs ML approaches

---

## 💡 Conclusion

This project is a great starting point for understanding how fake news detection works at a fundamental level. While simple, it lays the groundwork for more advanced NLP and machine learning systems.

---

## 🙌 Acknowledgment

Inspired by common patterns observed in clickbait and misleading online content.

---
