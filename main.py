# main.py
# Run with : python main.py

from pipeline import run_pipeline, build_stage, log_summary
from cleaner import (remove_urls, remove_html_tags, remove_punctuation, remove_extra_spaces, remove_emails)
from normaliser import (to_lowercase, strip_whitespace, expand_contractions, normalise_unicode)
from filter_words import (remove_stopwords, filter_short_words, deduplicate_sentences )
from analyser import analyse_text
from reporter import build_report

# ── Sample text — replace with any string you want to analyse ─────────────────
SAMPLE_TEXT = """
TextFlow is an amazing text processing pipeline built entirely with Python.
It doesn't use any external libraries — it can't rely on pandas or NLTK.
The system won't fail even with messy input like URLs (https://example.com)
or HTML tags (<b>bold text</b> and <br/> line breaks).
The pipeline is modular, clean, and easy to extend. Each stage transforms
the text independently. You can add, remove, or reorder stages without
breaking anything else.
Data engineers love modular systems because they're easier to debug and test.
The best software is built with clear boundaries between components.
This project demonstrates that excellent code doesn't need complex libraries.
I've built this to showcase real Python fundamentals — loops, functions,
data structures, and string processing — working together in a clean pipeline.
"""
# --Define pipeline stages ------------------------------------------------------
# Each stage : (name, function, config_dict)
# Stages run left to right in the list

STANDARD_PIPELINE = [
    build_stage("normalise_unicode", normalise_unicode),
    build_stage("expand_contractions", expand_contractions),
    build_stage("remove_urls",       remove_urls),
    build_stage("remove_html",       remove_html_tags),
    build_stage("remove_emails",     remove_emails),
    build_stage("to_lowercase",      to_lowercase),
    build_stage("remove_punctuation",remove_punctuation, keep=""),
    build_stage("remove_stopwords",  remove_stopwords,   lang="en"),
    build_stage("filter_short",      filter_short_words, min_length=3),
    build_stage("dedup_sentences",   deduplicate_sentences),
    build_stage("strip_whitespace",  strip_whitespace),
]

LIGHT_PIPELINE = [
    build_stage("normalise_unicode", normalise_unicode),
    build_stage("expand_contractions", expand_contractions),
    build_stage("remove_urls",       remove_urls),
    build_stage("remove_html",       remove_html_tags),
    build_stage("to_lowercase",      to_lowercase),
    build_stage("strip_whitespace",  strip_whitespace),
]
