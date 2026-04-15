with open("data/unprocessed_data.txt", "r") as file:
# Import keyword lists from rules file
from rules import CLICKBAIT_WORDS, SUSPICIOUS_PHRASES, EMOTIONAL_PHRASES

import re
import string


# Preprocess the text (original + lowercase + tokens)
def preprocess(text):
    original_text = text              # Keep original for caps/punctuation check
    lowered_text = text.lower()       # Convert to lowercase for matching
    tokens = lowered_text.split()     # Split text into words
    return original_text, lowered_text, tokens


# Check if any clickbait words are present
def check_clickbait(lowered_text):
    found = []
    for word in CLICKBAIT_WORDS:
        if word in lowered_text:
            found.append(word)
    return found


# Check suspicious phrases like conspiracy-type lines
def check_suspicious_phrases(lowered_text):
    found = []
    for phrase in SUSPICIOUS_PHRASES:
        if phrase in lowered_text:
            found.append(phrase)
    return found


# Check emotional or exaggerated language
def check_emotional_language(lowered_text):
    found = []
    for phrase in EMOTIONAL_PHRASES:
        if phrase in lowered_text:
            found.append(phrase)
    return found


# Check for too many ! or ? marks together
def check_excessive_punctuation(text):
    matches = re.findall(r'[!?]{2,}', text)
    return matches


# Check words written in ALL CAPS (3 or more letters)
def check_all_caps(original_text):
    words = original_text.split()
    caps_words = []
    for word in words:
        clean_word = word.strip(string.punctuation)  # Remove punctuation
        if clean_word.isupper() and len(clean_word) >= 3:
            caps_words.append(clean_word)
    return caps_words


# Calculate total score based on detected indicators
def calculate_score(clickbait, suspicious, emotional, punctuation, caps):
    score = 0
    reasons = []

    # Clickbait words add 2 points each
    if clickbait:
        score += len(clickbait) * 2
        reasons.append(f"Clickbait words detected: {clickbait}")

    # Suspicious phrases add 3 points each
    if suspicious:
        score += len(suspicious) * 3
        reasons.append(f"Suspicious phrases detected: {suspicious}")

    # Emotional language adds 2 points each
    if emotional:
        score += len(emotional) * 2
        reasons.append(f"Emotional/exaggerated language detected: {emotional}")

    # Excess punctuation adds 2 points
    if punctuation:
        score += 2
        reasons.append(f"Excessive punctuation found: {punctuation}")

    # ALL CAPS words add 1 point each
    if caps:
        score += len(caps) * 1
        reasons.append(f"ALL CAPS words found: {caps}")

    return score, reasons


# Decide final label based on score
def classify(score):
    THRESHOLD = 5  # If score is 5 or more, mark as fake
    if score >= THRESHOLD:
        return " Fake News (High Probability)"
    else:
        return "Likely Real News"


# Main function to run full detection
def detect_fake_news(text):
    print("\n" + "="*55)
    print("       RULE-BASED FAKE NEWS DETECTOR")
    print("="*55)
    print(f"\nInput Text:\n\"{text}\"\n")

    # Preprocess text
    original, lowered, tokens = preprocess(text)

    # Run all checks
    clickbait_found   = check_clickbait(lowered)
    suspicious_found  = check_suspicious_phrases(lowered)
    emotional_found   = check_emotional_language(lowered)
    punctuation_found = check_excessive_punctuation(original)
    caps_found        = check_all_caps(original)

    # Calculate score
    score, reasons = calculate_score(
        clickbait_found,
        suspicious_found,
        emotional_found,
        punctuation_found,
        caps_found
    )

    # Get final result
    result = classify(score)

    print(f"Score: {score}")
    print(f" Result: {result}\n")

    # Print reasons if any found
    if reasons:
        print( Reasons:")
        for i, reason in enumerate(reasons, 1):
            print(f"  {i}. {reason}")
    else:
        print(" No fake indicators found.")

    print("\n" + "="*55 + "\n")
