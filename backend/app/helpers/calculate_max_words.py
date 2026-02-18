def calculate_max_words(doc_words: int, detail_level: str) -> int:
    # Base summary size based on document length
    if doc_words < 800:
        base = int(doc_words * 0.6)
    elif doc_words < 3000:
        base = int(doc_words * 0.3)
    else:
        base = 800  # cap for very large docs

    # Adjust based on user preference
    if detail_level == "concise":
        return int(base * 0.6)
    elif detail_level == "standard":
        return int(base * 1.4)
    elif detail_level == "detailed":
        return int(base * 2)
    else:  # standard
        return base 