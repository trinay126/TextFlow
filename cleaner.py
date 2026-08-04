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

    # Collapse multiple spaces left behind by removed tags
    while " " in result:
        result = result.replace(" ", " ")
    return result.strip()
