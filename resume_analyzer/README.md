# Resume Analyzer Tool

A comprehensive Python tool for analyzing resumes, extracting key information, and providing actionable improvement suggestions.

## Features

- **Contact Information Extraction**: Email, phone, LinkedIn, website, and name
- **Section Detection**: Automatically identifies resume sections
- **Formatting Analysis**: Resume length, spacing, bullet points, consistency
- **Content Quality Assessment**: Required sections, detailed descriptions
- **Keywords & ATS Optimization**: Technical keywords and professional language
- **Grammar Check**: Spelling and sentence structure analysis
- **Comprehensive Report**: Detailed scores with feedback and suggestions

## Installation

```bash
# No external dependencies required - uses only Python standard library
python --version  # Requires Python 3.7+
```

## Quick Start

### Basic Usage

```python
from resume_analyzer import ResumeAnalyzer

with open('your_resume.txt', 'r') as f:
    resume_text = f.read()

analyzer = ResumeAnalyzer(resume_text)
report = analyzer.generate_report()

print(f"Overall Score: {report['overall_score']}/100")
print(f"Contact Info: {report['contact_info']}")
```

### Run Example

```bash
python example_usage.py
```

## Report Structure

### Overall Score
- Combined score out of 100

### 4 Category Scores

1. **Formatting** - Length, spacing, bullet points, dates, action verbs
2. **Content** - Section completeness, achievements, skills
3. **Keywords & ATS** - Technical keywords, professional phrases, buzzwords
4. **Grammar & Language** - Spelling, sentence structure

## Scoring Breakdown

- **90-100**: Excellent
- **80-89**: Good with minor improvements
- **70-79**: Average with noticeable gaps
- **60-69**: Needs significant improvements
- **Below 60**: Major overhaul recommended

## Example Output

```
==============================================
RESUME ANALYSIS REPORT
==============================================

OVERALL SCORE: 85.5/100

FORMATTING: 85.0%
  Strengths:
    - Good resume length
    - Good use of bullet points

CONTENT: 90.0%
  Strengths:
    - All major sections present
    - Quantifiable achievements included

KEYWORDS & ATS: 82.0%
GRAMMAR & LANGUAGE: 88.5%

TOP SUGGESTIONS:
1. Add more relevant technical keywords
2. Improve use of whitespace
```

## Classes

### ResumeAnalyzer

Main analysis class with methods:

- `extract_contact_info()` - Extract contact information
- `extract_sections()` - Parse resume sections
- `analyze_formatting()` - Evaluate formatting
- `analyze_content()` - Assess content quality
- `analyze_keywords()` - Check keywords and ATS
- `analyze_grammar()` - Perform grammar analysis
- `generate_report()` - Create complete analysis report

### Data Classes

- `ContactInfo` - Extracted contact details
- `Experience` - Work experience details
- `Education` - Education information
- `AnalysisScore` - Score and feedback

## Keywords Supported

The tool recognizes:
- **Languages**: Python, Java, JavaScript, SQL, Go, C++
- **Frameworks**: React, Django, Node.js, Spring, FastAPI
- **Tools**: AWS, Azure, Docker, Kubernetes, Git
- **Methodologies**: Agile, Scrum, CI/CD, Machine Learning

## Usage Tips

1. Use clear section headers (EXPERIENCE, EDUCATION, SKILLS)
2. Include dates in YYYY format
3. Use bullet points for accomplishments
4. Include quantifiable metrics
5. Use strong action verbs
6. Add relevant technical keywords

## License

MIT License
