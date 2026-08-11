# 📝 TextFlow

> A modular, configurable text-processing and analytics pipeline built entirely with Python's standard library.

TextFlow takes raw text, processes it through a configurable sequence of cleaning and normalization stages, and produces both cleaned text and a detailed analytics report.

The project demonstrates how a text-processing pipeline can be designed using Python fundamentals such as functions, loops, strings, lists, dictionaries, sets, comprehensions, and modular architecture.

---

## 🚀 Features

- 🔄 Configurable multi-stage text processing
- 🧹 URL and HTML tag removal
- 📧 Email address removal
- 🔤 Unicode normalization and case conversion
- ✍️ Contraction expansion
- 🧹 Punctuation and whitespace cleaning
- 🚫 Stopword removal
- 📏 Short-word filtering
- ♻️ Duplicate sentence removal
- 📊 Word and sentence statistics
- 📖 Flesch Reading Ease calculation
- 🔑 Keyword frequency and density analysis
- ❤️ Rule-based sentiment analysis
- 📋 Detailed pipeline execution logging
- 📈 Before/after character reduction statistics
- 🧩 Multiple predefined pipelines
- ⚡ Zero external dependencies

---

## 🏗️ Architecture

TextFlow follows a modular pipeline architecture:

    Raw Text
        ↓
    Pipeline Configuration
        ↓
    ┌─────────────────────────────────┐
    │         Processing Stages       │
    │                                 │
    │ Unicode Normalization           │
    │ Contraction Expansion           │
    │ URL Removal                     │
    │ HTML Removal                    │
    │ Email Removal                   │
    │ Lowercase Conversion            │
    │ Punctuation Removal             │
    │ Stopword Removal                │
    │ Short Word Filtering            │
    │ Duplicate Sentence Removal      │
    │ Whitespace Normalization        │
    └────────────────┬────────────────┘
                     ↓
               Cleaned Text
                     ↓
             Analytics Engine
                     ↓
    ┌─────────────────────────────────┐
    │ Word Statistics                 │
    │ Readability                     │
    │ Keywords                        │
    │ Sentiment                       │
    └────────────────┬────────────────┘
                     ↓
                Final Report

---

## 📁 Project Structure

    textflow/
    │
    ├── main.py
    ├── pipeline.py
    ├── cleaner.py
    ├── normaliser.py
    ├── filter_words.py
    ├── analyser.py
    ├── reporter.py
    ├── requirements.txt
    └── .gitignore

### Module Responsibilities

| File | Responsibility |
|------|----------------|
| `main.py` | Application entry point and pipeline configuration |
| `pipeline.py` | Executes processing stages sequentially |
| `cleaner.py` | Removes URLs, HTML, emails, punctuation, digits and unwanted characters |
| `normaliser.py` | Handles case, whitespace, Unicode and contractions |
| `filter_words.py` | Handles stopwords, short words and duplicate sentences |
| `analyser.py` | Calculates text statistics, readability, keywords and sentiment |
| `reporter.py` | Formats and displays the final analytics report |

---

## 🔄 Available Pipelines

TextFlow provides three predefined pipelines.

### 1. Standard Pipeline

The complete processing pipeline:

    Unicode Normalization
            ↓
    Contraction Expansion
            ↓
    URL Removal
            ↓
    HTML Removal
            ↓
    Email Removal
            ↓
    Lowercase
            ↓
    Punctuation Removal
            ↓
    Stopword Removal
            ↓
    Short Word Filtering
            ↓
    Duplicate Sentence Removal
            ↓
    Whitespace Normalization

### 2. Light Pipeline

A lightweight cleaning pipeline that performs basic normalization without aggressive filtering.

### 3. Keyword Pipeline

A pipeline optimized for keyword extraction through stronger filtering and normalization.

---

## 📊 Analytics

### 📈 Word Statistics

TextFlow calculates:

- Total word count
- Unique word count
- Sentence count
- Average word length
- Average sentence length
- Longest word
- Shortest word

### 📖 Readability Analysis

TextFlow implements the Flesch Reading Ease formula directly.

    90–100  Very Easy
    70–80   Easy
    60–70   Standard
    50–60   Fairly Difficult
    30–50   Difficult
    0–30    Very Difficult

### 🔑 Keyword Density

TextFlow identifies frequently occurring keywords and calculates their density relative to the total number of words.

The report displays the top 10 keywords.

### ❤️ Sentiment Analysis

TextFlow implements a rule-based sentiment analyzer.

It:

1. Detects positive words
2. Detects negative words
3. Detects basic negation
4. Flips sentiment when appropriate
5. Calculates a normalized sentiment score

Example:

    "I love this application."
            ↓
        Positive

    "I do not love this application."
            ↓
        Negative

The sentiment score ranges from:

    -1.0  ←────────  0  ────────→  +1.0
    Negative                     Positive

---

## 🧩 Pipeline Design

Each processing stage follows a common interface:

    stage_function(text, **config) -> transformed_text

Stages are represented as:

    (stage_name, stage_function, config)

Example:

    build_stage(
        "remove_stopwords",
        remove_stopwords,
        lang="en"
    )

This design allows stages to be:

- Added
- Removed
- Reordered
- Configured independently

without modifying the pipeline executor.

---

## 📋 Pipeline Logging

Every processing stage records its effect on the input.

Example:

    Stage                     Before    After    Removed
    ----------------------------------------------------
    normalise_unicode             420      420          0
    expand_contractions           420      428         -8
    remove_urls                   428      380         48
    remove_html                   380      350         30
    remove_emails                 350      320         30
    remove_punctuation            320      300         20
    remove_stopwords              300      215         85
    filter_short                  215      200         15

The pipeline summary includes:

- Number of stages executed
- Input character count
- Output character count
- Total characters removed
- Percentage reduction

---

## 🛠️ Technologies

    Language        : Python
    Architecture    : Modular Pipeline Architecture
    NLP Approach    : Rule-Based / String Processing
    Dependencies    : Python Standard Library

---

## 📦 Requirements

TextFlow has no third-party dependencies.

    Python 3.8+

The project uses the Python standard library.

---

## ▶️ Getting Started

### Clone the repository

    git clone https://github.com/YOUR_USERNAME/textflow.git

### Navigate into the project

    cd textflow

### Run the application

    python main.py

---

## ⚙️ Running Different Pipelines

The default pipeline is:

    run_textflow(
        text=SAMPLE_TEXT,
        pipeline_name="standard"
    )

Run the light pipeline:

    run_textflow(
        pipeline_name="light"
    )

Run the keyword pipeline:

    run_textflow(
        pipeline_name="keyword"
    )

Available pipelines:

    AVAILABLE_PIPELINES = {
        "standard": STANDARD_PIPELINE,
        "light": LIGHT_PIPELINE,
        "keyword": KEYWORD_PIPELINE,
    }

---

## 📋 Example Processing

### Input

    TextFlow is an amazing text processing pipeline!
    It doesn't use external libraries.

    Visit https://example.com

    <b>Python makes development powerful.</b>

### Processing

    Raw Text
       ↓
    Normalize Unicode
       ↓
    Expand Contractions
       ↓
    Remove URLs
       ↓
    Remove HTML
       ↓
    Remove Punctuation
       ↓
    Remove Stopwords
       ↓
    Filter Short Words
       ↓
    Normalize Whitespace

### Output

    textflow amazing text processing pipeline
    use external libraries
    python makes development powerful

The exact output depends on the selected pipeline and input text.

---

## 🧠 Python Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| Functions | Processing and analytics stages |
| `**kwargs` | Configurable pipeline stages |
| Strings | Text transformation |
| Lists | Pipeline stages and word processing |
| Tuples | Stage definitions |
| Dictionaries | Analytics and configuration |
| Sets | Stopwords and duplicate detection |
| List Comprehensions | Filtering and transformation |
| Lambda | Keyword sorting |
| Loops | Character and word processing |
| Conditionals | Processing decisions |
| Mathematical Operations | Readability and sentiment calculations |
| Modular Programming | Separate processing modules |

---

## 🎯 Design Goals

### Modularity

Each processing operation is implemented as an independent function.

### Configurability

Different pipelines can use different combinations of processing stages.

### Transparency

Every stage records what happened to the input.

### Zero Dependencies

The core processing mechanics are implemented using Python's standard library.

---

## 🔮 Future Improvements

Possible future extensions include:

- REST API using FastAPI
- File upload support
- Batch document processing
- Persistent analytics storage
- Additional language support
- Advanced NLP models
- Database integration
- Web interface
- Automated test suite
- Performance benchmarking
- Async processing for large workloads

---

## 🎤 Interview Talking Points

### Why did you build TextFlow?

> I wanted to understand how text-processing pipelines work internally rather than simply calling an NLP library. I designed each transformation as an independent stage and created a pipeline executor to run those stages sequentially.

### Why use a pipeline architecture?

> It separates individual transformations from execution logic, making the system easier to extend, debug and reorder.

### Why didn't you use NLTK or spaCy?

> The goal of this project was to demonstrate Python fundamentals and understand the mechanics behind common text-processing operations. External NLP libraries could be introduced later when more sophisticated linguistic processing is required.

### How would you scale this?

> I would first expose the pipeline through a FastAPI service, then add batch processing, persistence, asynchronous execution and eventually distributed processing for large workloads.

---

## 📌 Current Scope

    Python Fundamentals
            +
    String Processing
            +
    Modular Architecture
            +
    Pipeline Design
            +
    Text Analytics
            +
    Rule-Based NLP

TextFlow is intentionally a fundamentals-focused text-processing project rather than a production NLP framework.

---

## 👨‍💻 Author

**Your Name**

Computer Science Student  
Python | Backend Development | AI Engineering

---

## ⭐ Project Highlights

    ✓ Modular architecture
    ✓ Configurable processing pipeline
    ✓ Zero external dependencies
    ✓ Rule-based sentiment analysis
    ✓ Readability analysis
    ✓ Keyword density analysis
    ✓ Detailed processing logs
    ✓ Multiple pipeline configurations
    ✓ Built from Python fundamentals

---

## 📄 License

This project is available for educational and portfolio purposes.