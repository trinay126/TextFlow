# analyser.py
# Analytics engine : readability, keywords, sentiment, word stats.

# -- Word Statistics --------------------

def word_stats(text):
    """
    Compute word - level statistics for a text string.

    Returns a dict with : word count, unique words, avg length,
    longest word, shortest word, sentence count.
    """
    words = text.split()
    sentences = max(1, sum( 1 for ch in text if ch in ".!?"))

    if not words:
        return{
            "word_count" : 0, "unique_words" : 0,
            "avg_word_len" : 0 , "longest" : "", "shortest" : "",
            "Sentence_count" : sentences, "avg_sent_len" : 0,
        }
    clean_words = [w.strip(".,!?;:\"'") for w in words if w.strip(".,!?;:\"'")]
    lengths = [len(w) for w in clean_words]

    return{
        "word_count" : len(words),
        "unique_words" : len(set(w.lower() for w in clean_words)),
        "avg_word_len" : round(sum(lengths) / max(1, len(lengths)), 1),
        "longest" : max(clean_words, key=len) if clean_words else "",
        "shortest" : min(clean_words, key=len) if clean_words else "",
        "sentence_count" : sentences,
        "avg_sent_len" : round(len(words) / sentences, 1),
    }
# --Readability -----------------------------------------------------
def count_syllables(word):
    """
    Approximate syllable count for a word.

    Rules :
        count vowel groups (consecutive vowels =  one syllable).
        substract silent 'e' at end of word.
        Minimum ! syllable per word.
    """
    word = word.lower().strip(".,!?;:'\"")
    vowels = "aeiou"
    count = 0
    prev_v = False

    for ch in word:
        is_v = ch in vowels
        if is_v and not prev_v:
            count+= 1
        prev_v = is_v
    #silent 'e' at end 
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)

def flesch_reading_ease(text):