# rules.py
# This file contains all the lists and rules used to detect fake news
# Each list is a collection of words or phrases that are commonly found in fake news
 
# List 1: Clickbait words - these are dramatic words used to grab attention
CLICKBAIT_WORDS = [
    "breaking", "shocking", "secret", "exposed", "you won",
    "unbelievable", "mind blowing", "incredible", "bombshell",
    "exclusive", "urgent", "alert", "warning", "miracle",
    "banned", "censored", "leaked", "scandal", "explosive"
]
 
# List 2: Suspicious phrases - these are typical fake news / scam phrases
SUSPICIOUS_PHRASES = [
    "doctors hate this",
    "government doesn't want you to know",
    "big pharma hiding",
    "click here now",
    "limited time offer",
    "share before it gets deleted",
    "mainstream media won't show you",
    "what they are hiding",
    "the truth about",
    "you won't believe",
    "this will shock you"
]
 
# List 3: Emotional / exaggerated language phrases
EMOTIONAL_PHRASES = [
    "this will change your life forever",
    "life changing",
    "once in a lifetime",
    "destroy everything",
    "end of the world",
    "life will never be the same",
    "going viral"
]
