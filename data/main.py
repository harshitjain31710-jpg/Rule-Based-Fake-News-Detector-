from rules import CLICKBAIT_WORDS, SUSPICIOUS_PHRASES, EMOTIONAL_PHRASES
import re
import string


def preprocess(text):
    original_text = text
    lowered_text = text.lower()
    tokens = lowered_text.split()
    return original_text, lowered_text, tokens


def check_clickbait(lowered_text):
    found = []
    for word in CLICKBAIT_WORDS:
        if word in lowered_text:
            found.append(word)
    return found


def check_suspicious_phrases(lowered_text):
    found = []
    for phrase in SUSPICIOUS_PHRASES:
        if phrase in lowered_text:
            found.append(phrase)
    return found


def check_emotional_language(lowered_text):
    found = []
    for phrase in EMOTIONAL_PHRASES:
        if phrase in lowered_text:
            found.append(phrase)
    return found


def check_excessive_punctuation(text):
    matches = re.findall(r'[!?]{2,}', text)
    return matches


def check_all_caps(original_text):
    words = original_text.split()
    caps_words = []
    for word in words:
        clean_word = word.strip(string.punctuation)
        if clean_word.isupper() and len(clean_word) >= 3:
            caps_words.append(clean_word)
    return caps_words


def calculate_score(clickbait, suspicious, emotional, punctuation, caps):
    score = 0
    reasons = []

    if clickbait:
        score += len(clickbait) * 2
        reasons.append(f"Clickbait words detected: {clickbait}")

    if suspicious:
        score += len(suspicious) * 3
        reasons.append(f"Suspicious phrases detected: {suspicious}")

    if emotional:
        score += len(emotional) * 2
        reasons.append(f"Emotional/exaggerated language detected: {emotional}")

    if punctuation:
        score += 2
        reasons.append(f"Excessive punctuation found: {punctuation}")

    if caps:
        score += len(caps) * 1
        reasons.append(f"ALL CAPS words found: {caps}")

    return score, reasons


def classify(score):
    THRESHOLD = 5
    if score >= THRESHOLD:
        return "🚨 Fake News (High Probability)"
    else:
        return "✅ Likely Real News"


def detect_fake_news(text):
    print("\n" + "="*55)
    print("       RULE-BASED FAKE NEWS DETECTOR")
    print("="*55)
    print(f"\n📰 Input Text:\n\"{text}\"\n")

    original, lowered, tokens = preprocess(text)

    clickbait_found   = check_clickbait(lowered)
    suspicious_found  = check_suspicious_phrases(lowered)
    emotional_found   = check_emotional_language(lowered)
    punctuation_found = check_excessive_punctuation(original)
    caps_found        = check_all_caps(original)

    score, reasons = calculate_score(
        clickbait_found,
        suspicious_found,
        emotional_found,
        punctuation_found,
        caps_found
    )

    result = classify(score)

    print(f"📊 Score: {score}")
    print(f"🏷️  Result: {result}\n")

    if reasons:
        print("🔍 Reasons:")
        for i, reason in enumerate(reasons, 1):
            print(f"  {i}. {reason}")
    else:
        print("🔍 No fake indicators found.")

    print("\n" + "="*55 + "\n")


if __name__ == "__main__":
    test_inputs = [
        "BREAKING!!! You won $10000!!! Click now!!!",
        "Scientists discover new species of frog in Amazon rainforest.",
        "SHOCKING SECRET exposed!!! Doctors hate this one weird trick!!!",
        "Government doesn't want you to know the truth about vaccines.",
        "The stock market closed slightly higher on Thursday.",
        "THIS WILL CHANGE YOUR LIFE FOREVER!!! Share before it gets deleted!!!"
    ]

    for news in test_inputs:
        detect_fake_news(news)

    print("\n💬 Enter your own text to check (or press Enter to skip):")
    user_input = input(">>> ").strip()
    if user_input:
        detect_fake_news(user_input)
    else:
        print("Skipped. Goodbye! 👋")
