# =====================================================
# main.py
# This is the MAIN file of our Fake News Detector.
# Run this file to start the program.
#
# HOW TO RUN:
#   Open your terminal and type:
#       python main.py
# =====================================================


# -------------------------------------------------------
# IMPORTS
# "import" means we are borrowing tools from elsewhere.
# Python has many built-in tools - we just have to ask!
# -------------------------------------------------------

# 're' helps us search for patterns inside text
# For example: finding "!!!" or "???" in a sentence
import re

# 'string' gives us a ready-made list of punctuation
# like . , ! ? " ' etc.
import string

# We bring in our word lists from our own rules.py file
# Think of rules.py as a separate notebook full of red flags
from rules import CLICKBAIT_WORDS
from rules import SUSPICIOUS_PHRASES
from rules import EMOTIONAL_PHRASES


# =====================================================
# STEP 1 - CLEAN THE TEXT
#
# Before checking anything, we tidy up the text.
# We make it all lowercase so "BREAKING" and
# "breaking" are treated as the same word.
# =====================================================

def clean_text(text):

    # Keep the original text saved
    # We need the original later for the CAPS check
    original = text

    # Convert everything to lowercase
    # "BREAKING NEWS!!!" → "breaking news!!!"
    lowercased = text.lower()

    # Split the sentence into a list of individual words
    # "hello world" → ["hello", "world"]
    words = lowercased.split()

    # Give back all three versions so we can use them later
    return original, lowercased, words


# =====================================================
# STEP 2 - CHECK FOR CLICKBAIT WORDS
#
# We look through our CLICKBAIT_WORDS list
# and check if any of them appear in the news text.
#
# Example clickbait words: "shocking", "breaking",
# "secret", "exposed"
# =====================================================

def check_for_clickbait(lowercased_text):

    # Empty list - we will add to it if we find something
    found = []

    # Go through each clickbait word one by one
    for word in CLICKBAIT_WORDS:

        # Does this clickbait word appear in our news text?
        if word in lowercased_text:

            # Yes! Add it to our found list
            found.append(word)

    # Send back the list of what we found
    # If nothing was found, this will just be []
    return found


# =====================================================
# STEP 3 - CHECK FOR SUSPICIOUS PHRASES
#
# Same idea as Step 2 but we check full phrases,
# not just single words.
#
# Example: "doctors hate this", "click here now"
# =====================================================

def check_for_suspicious_phrases(lowercased_text):

    found = []

    for phrase in SUSPICIOUS_PHRASES:

        if phrase in lowercased_text:
            found.append(phrase)

    return found


# =====================================================
# STEP 4 - CHECK FOR EMOTIONAL LANGUAGE
#
# Fake news tries to make you panic or over-react.
# Phrases like "this will change your life forever"
# are meant to scare you into sharing the post.
# =====================================================

def check_for_emotional_language(lowercased_text):

    found = []

    for phrase in EMOTIONAL_PHRASES:

        if phrase in lowercased_text:
            found.append(phrase)

    return found


# =====================================================
# STEP 5 - CHECK FOR EXCESSIVE PUNCTUATION
#
# Fake news loves writing like this → "Click NOW!!!"
# Normal news does not use !!! or ???
#
# We use re.findall() to search for this pattern.
# The pattern r'[!?]{2,}' means:
#   [!?]   → either a ! or a ?
#   {2,}   → appearing 2 or more times in a row
# =====================================================

def check_for_excessive_punctuation(original_text):

    # findall() returns a list of all matches it finds
    matches = re.findall(r'[!?]{2,}', original_text)

    # Example: "Click NOW!!! Really???" → ['!!!', '???']
    return matches




# =====================================================
# STEP 6 - CALCULATE THE SCORE
#
# Every red flag we found adds points to the score.
# The higher the score, the more likely it is fake.
#
# Points system:
#   Each clickbait word      →  +2 points
#   Each suspicious phrase   →  +3 points
#   Each emotional phrase    →  +2 points
#   Excessive punctuation    →  +2 points (one time)
#   Each ALL CAPS word       →  +1 point
# =====================================================

def calculate_score(clickbait, suspicious, emotional, punctuation, caps):

    # Start the score at zero
    score = 0

    # We'll collect reasons to show the user later
    reasons = []

    # --- Add points for clickbait words ---
    if len(clickbait) > 0:
        points_added = len(clickbait) * 2
        score = score + points_added
        reasons.append("Clickbait words found: " + str(clickbait))

    # --- Add points for suspicious phrases ---
    if len(suspicious) > 0:
        points_added = len(suspicious) * 3
        score = score + points_added
        reasons.append("Suspicious phrases found: " + str(suspicious))

    # --- Add points for emotional language ---
    if len(emotional) > 0:
        points_added = len(emotional) * 2
        score = score + points_added
        reasons.append("Emotional language found: " + str(emotional))

    # --- Add points for excessive punctuation ---
    if len(punctuation) > 0:
        score = score + 2
        reasons.append("Excessive punctuation found: " + str(punctuation))

    # --- Add points for ALL CAPS words ---
    if len(caps) > 0:
        points_added = len(caps) * 1
        score = score + points_added
        reasons.append("ALL CAPS words found: " + str(caps))

    return score, reasons


# =====================================================
# STEP 7 - DECIDE IF IT IS FAKE OR REAL
#
# We use a "threshold" (a cut-off number).
# If the score is 5 or more → probably Fake News
# If the score is less than 5 → probably Real News
#
# Think of it like a temperature check:
#   score >= 5 = fever (something is wrong!)
#   score < 5  = normal (looks okay)
# =====================================================

def decide_fake_or_real(score):

    # This is our cut-off number
    THRESHOLD = 5

    if score >= THRESHOLD:
        return "FAKE NEWS"
    else:
        return "LIKELY REAL"


# =====================================================
# STEP 8 - SHOW THE RESULT
#
# This function prints everything nicely so the
# user can easily read and understand the output.
# =====================================================

def show_result(text, score, label, reasons):

    print("\n" + "-" * 55)
    print("INPUT  : " + text)
    print("SCORE  : " + str(score))
    print("RESULT : " + label)
    print("WHY?")

    # If we found reasons, print each one
    if len(reasons) > 0:
        for reason in reasons:
            print("   -> " + reason)

    # If no reasons, the text was clean
    else:
        print("   -> No red flags found.")

    print("-" * 55)


# =====================================================
# STEP 10 - THE MAIN FUNCTION
#
# This is where everything comes together.
# We call all the steps one by one in order.
# =====================================================

def run_detector(text):

    # Step 1: Clean the text
    original, lowercased, words = clean_text(text)

    # Step 2: Run all our checks
    clickbait   = check_for_clickbait(lowercased)
    suspicious  = check_for_suspicious_phrases(lowercased)
    emotional   = check_for_emotional_language(lowercased)
    punctuation = check_for_excessive_punctuation(original)
   
    # Step 3: Calculate the total score
    score, reasons = calculate_score(
        clickbait,
        suspicious,
        emotional,
        punctuation,
    )

    # Step 4: Decide fake or real
    label = decide_fake_or_real(score)

    # Step 5: Show the result to the user
    show_result(text, score, label, reasons)


# =====================================================
# THIS PART RUNS WHEN YOU EXECUTE THE FILE
#
# We test the detector on 6 example sentences.
# Then we let the user type their own sentence.
# =====================================================

if __name__ == "__main__":

    print("\n" + "=" * 55)
    print("      RULE-BASED FAKE NEWS DETECTOR")
    print("=" * 55)

    # --- Test examples (feel free to change these!) ---
    test_examples = [
        "BREAKING!!! You won $10000!!! Click now!!!",
        "Scientists discover new species of frog in Amazon.",
        "SHOCKING SECRET exposed!!! Doctors hate this trick!!!",
        "Government doesn't want you to know the truth!!!",
        "The stock market closed higher on Thursday.",
        "FREE MONEY!!! Share before it gets deleted!!!"
    ]

    print("\nRunning on test examples...\n")

    # Loop through each example and run the detector
    for example in test_examples:
        run_detector(example)

    # --- Let the user type their own text ---
    print("\nNow try your own text!")
    print("Type a news headline below and press Enter:")
    print("(Just press Enter without typing to skip)\n")

    user_text = input(">>> ").strip()

    # Only run if the user actually typed something
    if user_text != "":
        run_detector(user_text)
    else:
        print("\nNo input given. Goodbye!")
