# cleaner.py
# Cleaning stages : remove URLs, HTML, Punctuation, digits.
# Only string methods used

def remove_urls(text, **kwargs):
    """
    Remove http/https URLs and www addresses from text.
    strategy : split into words, drop any word that starts with a URl prefix
    """    
    url_starts = ("http://", "https://", "www", "ftp://")
    words = text.split()
    kept = [w for w in words if not any(w.lower().startswith(p) for p in url_starts)]

    return " ".join(kept)

def remove_html_tags(text, **kwargs):
    """
    Strip HTML tags and keep their inner content.
    Uses a simple character-by-character scan - no regex

    Strategy:
        - When we see '<' set in_tag = true  → stop copying characters
        - When we see '>' set in_tag = False  →  resume copying
        - Everything outside tags goes into the result
    """

    result = ""
    in_tag = False

    for ch in text:
        if ch == "<":
            in_tag = True
            result += " "
        elif ch == ">":
            in_tag = False
        elif not in_tag:
            result += ch

    while "  " in result:
        result = result.replace("  ", " ")

    return result.strip()

def remove_punctuation(text, keep="", **kwargs):
    """
    Remove punctuation characters from text

    Args:
        keep : string of puntuation chars to preserve
    """
    result = ""
    for ch in text:
        if ch.isalnum() or ch.isspace() or ch in keep:
            result += ch
    return result

def remove_digits(text, **kwargs):
    """Remove all digits characters from text"""
    return "".join(ch for ch in text if not ch.isdigit())

def remove_special_chars(text, **kwargs):
    """Keep only letters, digits, and spaces."""
    result = ""
    for ch in text:
        if ch.isalnum() or ch.isspace():
            result += ch
    return result

def remove_extra_spaces(text, **kwargs):
    """Collapse multiple consecutive spaces into one"""
    result = text.strip()
    while " " in result:
        result = result.replace("  ", " ")
    return result

def deduplicate_lines(text, **kwargs):
    """
    Remove duplicate lines, preserving the order of first occurence.
    Useful for repeated boilerplate or scraped duplicate paragraphs.
    """
    seen = set()
    lines = []
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped and stripped not in seen:
            seen.add(stripped)
            lines.append(line)
    return "\n".join(lines)

def remove_emails(text, **kwargs):
    """
    Remove email addresses from text.
    Strategy : drop any word that contain '@' and a '.' after '@'  
    """

    words = text.split()
    result = []
    for word in words:
        at_pos = word.find("@")
        if at_pos > 0 and "." in word[at_pos:]:
            continue #looks like an email - skip it
        result.append(word)
    return " ".join(result)