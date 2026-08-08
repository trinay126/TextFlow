# reporter.py
# Builds and prints the full Textflow analysis report.
# Pure string formatting 

WIDTH = 62

def divider(char="-"):
    return char * WIDTH

def section_header(title):
    return[f"\n{title}", divider()]

def header_box(pipeline_name, summary):
    lines = [
        "=" * WIDTH,
        "Textflow - Text Analytics Report".center(WIDTH),
        "=" * WIDTH,
        f" Pipeline   : {pipeline_name}",
        f" Stages run : {summary.get('stages_run', 0)}",
        f" Input chars : {summary.get('chars_before', 0):,}",
        f" Output chars : {summary.get('chars_after', 0):,}",
        f" Chars removed : {summary.get('chars_removed', 0):,}",
        f"  ({summary.get('pct_reduced', 0)}%)",
        "=" * WIDTH,
    ]
    return lines

def format_pipeline_log(log):
    """show what each sage did."""
    lines = section_header("PIPELINE STAGE LOG")
    lines.append(
        f" {'stage':<25} {'Before':>7} {'After':>7} {'Removed':>8}"
    )
    lines.append(f" {divider('-')}")
    for entry in log:
        removed_flag = " <" if entry ["removed"] > 0 else ""
        lines.append(
            f" {entry['stage']:<25}"
            f" {entry['before']:>7,}"
            f" {entry['after']:>7,}"
            f" {entry['removed']:>7,}{removed_flag}"
        )
    return lines

def format_word_stats(label, stats):
    """Format word-level statistics block"""
    lines = section_header(f"WORD STATISTICS ({label})")
    lines.append(f" Word count  : {stats.get('word_count', 0):,}")
    lines.append(f"  Unique words    : {stats.get('unique_words', 0):,}")
    lines.append(f"  Sentence count  : {stats.get('sentence_count', 0)}")
    lines.append(f"  Avg word length : {stats.get('avg_word_len', 0)} chars")
    lines.append(f"  Avg sent length : {stats.get('avg_sent_len', 0)} words")
    lines.append(f"  Longest word    : {stats.get('longest', '')}")
    lines.append(f"  Shortest word   : {stats.get('shortest', '')}")
    return lines

