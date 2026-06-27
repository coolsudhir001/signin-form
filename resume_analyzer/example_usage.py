"""
Example usage of the Resume Analyzer Tool
"""

import json
from resume_analyzer import ResumeAnalyzer


SAMPLE_RESUME = """
Jane Smith
jane.smith@email.com | (555) 987-6543 | San Francisco, CA
linkedin.com/in/janesmith

PROFESSIONAL SUMMARY
Full-stack software engineer with 6+ years of experience building scalable web applications.

PROFESSIONAL EXPERIENCE

Senior Software Engineer | TechCorp Inc. | 2021 - Present
- Led migration of legacy monolith to microservices, reducing latency by 35%
- Managed team of 4 engineers
- Implemented CI/CD pipeline reducing deployment time by 75%
- Optimized database queries improving response time by 60%

Full Stack Engineer | StartupXYZ | 2019 - 2021
- Developed React-based application serving 50,000+ users
- Built RESTful APIs using Node.js handling 10,000+ requests per day
- Set up AWS infrastructure including EC2, RDS, S3

EDUCATION

Bachelor of Science in Computer Science | State University | 2018
GPA: 3.7/4.0

TECHNICAL SKILLS

Languages: JavaScript, Python, Java, SQL, TypeScript
Frontend: React, Vue.js, Redux
Backend: Node.js, Express, Django
Databases: PostgreSQL, MongoDB, Redis
Tools: Git, Docker, Kubernetes, AWS, GitHub Actions
"""


def analyze_resume(resume_text, verbose=True):
    """Analyze a resume and return the report."""
    analyzer = ResumeAnalyzer(resume_text)
    report = analyzer.generate_report()
    
    if verbose:
        print_report(report)
    
    return report


def print_report(report):
    """Pretty print the analysis report."""
    print("=" * 70)
    print("RESUME ANALYSIS REPORT".center(70))
    print("=" * 70)
    
    contact = report['contact_info']
    print(f"\nCONTACT INFORMATION:")
    print(f"   Name: {contact['name']}")
    print(f"   Email: {contact['email']}")
    print(f"   Phone: {contact['phone']}")
    
    print(f"\n{'=' * 70}")
    score = report['overall_score']
    print(f"OVERALL SCORE: {score}/100")
    print(f"{'=' * 70}")
    
    print(f"\nCATEGORY BREAKDOWN:\n")
    
    for category, data in report['category_scores'].items():
        percentage = data['percentage']
        print(f"{category.upper()}: {percentage}%")
        
        if data['feedback']:
            print(f"  Strengths:")
            for item in data['feedback']:
                print(f"    - {item}")
        
        if data['suggestions']:
            print(f"  Areas for Improvement:")
            for item in data['suggestions']:
                print(f"    - {item}")
        
        print()
    
    print(f"{'=' * 70}")
    print(f"TOP PRIORITY IMPROVEMENTS ({report['total_suggestions']} total):\n")
    
    for i, suggestion in enumerate(report['top_suggestions'], 1):
        print(f"{i}. {suggestion}")
    
    print(f"\n{'=' * 70}\n")


def save_report_json(report, filename='resume_analysis.json'):
    """Save the report to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Report saved to {filename}")


if __name__ == "__main__":
    print("Resume Analyzer Tool - Example Usage\n")
    print("Analyzing sample resume...\n")
    report = analyze_resume(SAMPLE_RESUME, verbose=True)
    
    # Save as JSON
    save_report_json(report)
    
    # Extract specific information
    print("\nDETAILED METRICS:\n")
    print(f"Contact extraction accuracy: {'Yes' if report['contact_info']['email'] else 'No'}")
    print(f"Overall score: {report['overall_score']}/100")
    print(f"Total improvement areas: {report['total_suggestions']}")
