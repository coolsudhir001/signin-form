"""
Resume Analyzer Tool
A comprehensive tool for analyzing resumes, extracting key information,
and providing improvement suggestions.
"""

import re
import json
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum


class SectionType(Enum):
    """Enum for different resume sections."""
    CONTACT = "contact"
    SUMMARY = "summary"
    EXPERIENCE = "experience"
    EDUCATION = "education"
    SKILLS = "skills"
    CERTIFICATIONS = "certifications"
    PROJECTS = "projects"
    ADDITIONAL = "additional"


@dataclass
class ContactInfo:
    """Contact information extracted from resume."""
    name: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""
    linkedin: str = ""
    website: str = ""


@dataclass
class Experience:
    """Work experience information."""
    title: str = ""
    company: str = ""
    duration: str = ""
    description: List[str] = None
    
    def __post_init__(self):
        if self.description is None:
            self.description = []


@dataclass
class Education:
    """Education information."""
    degree: str = ""
    institution: str = ""
    graduation_year: str = ""
    gpa: str = ""
    details: List[str] = None
    
    def __post_init__(self):
        if self.details is None:
            self.details = []


@dataclass
class AnalysisScore:
    """Score and feedback for resume analysis."""
    category: str
    score: float
    max_score: float
    feedback: List[str]
    suggestions: List[str]


class ResumeAnalyzer:
    """Main Resume Analyzer class."""
    
    def __init__(self, resume_text: str):
        """
        Initialize the analyzer with resume text.
        
        Args:
            resume_text: Raw text content of the resume
        """
        self.resume_text = resume_text
        self.lines = resume_text.split('\n')
        self.contact_info = ContactInfo()
        self.experiences: List[Experience] = []
        self.education: List[Education] = []
        self.skills: List[str] = []
        self.summary: str = ""
        self.analysis_results: Dict[str, AnalysisScore] = {}
    
    def extract_contact_info(self) -> ContactInfo:
        """Extract contact information from resume."""
        text = self.resume_text
        
        # Email extraction
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        email_match = re.search(email_pattern, text)
        self.contact_info.email = email_match.group(0) if email_match else ""
        
        # Phone extraction
        phone_pattern = r'(?:\+?1[-\.\s]?)?\(?(\d{3})\)?[-\.\s]?(\d{3})[-\.\s]?(\d{4})'
        phone_match = re.search(phone_pattern, text)
        self.contact_info.phone = phone_match.group(0) if phone_match else ""
        
        # LinkedIn extraction
        linkedin_pattern = r'(?:https?://)?(?:www\.)?linkedin\.com/(?:in|company)/[\w-]+'
        linkedin_match = re.search(linkedin_pattern, text, re.IGNORECASE)
        self.contact_info.linkedin = linkedin_match.group(0) if linkedin_match else ""
        
        # Website extraction
        website_pattern = r'https?://[^\s]+'
        website_matches = re.findall(website_pattern, text)
        if website_matches:
            self.contact_info.website = website_matches[0]
        
        # Extract name (usually first line)
        if self.lines:
            potential_name = self.lines[0].strip()
            if potential_name and len(potential_name) < 100:
                self.contact_info.name = potential_name
        
        return self.contact_info
    
    def extract_sections(self) -> Dict[str, str]:
        """Extract major sections from resume."""
        sections = {}
        current_section = None
        current_content = []
        
        section_headers = {
            'EXPERIENCE': SectionType.EXPERIENCE,
            'EMPLOYMENT': SectionType.EXPERIENCE,
            'WORK HISTORY': SectionType.EXPERIENCE,
            'EDUCATION': SectionType.EDUCATION,
            'SKILLS': SectionType.SKILLS,
            'TECHNICAL SKILLS': SectionType.SKILLS,
            'CERTIFICATIONS': SectionType.CERTIFICATIONS,
            'PROJECTS': SectionType.PROJECTS,
            'SUMMARY': SectionType.SUMMARY,
            'OBJECTIVE': SectionType.SUMMARY,
        }
        
        for line in self.lines:
            line_upper = line.upper().strip()
            
            # Check if this is a section header
            is_header = False
            for header_key, section_type in section_headers.items():
                if header_key in line_upper:
                    if current_section:
                        sections[current_section.value] = '\n'.join(current_content)
                    current_section = section_type
                    current_content = []
                    is_header = True
                    break
            
            if not is_header and current_section:
                current_content.append(line)
        
        if current_section:
            sections[current_section.value] = '\n'.join(current_content)
        
        return sections
    
    def analyze_formatting(self) -> AnalysisScore:
        """Analyze resume formatting."""
        score = 0
        max_score = 100
        feedback = []
        suggestions = []
        
        # Check length
        lines_count = len(self.lines)
        pages_estimate = lines_count / 40
        if pages_estimate <= 2:
            score += 20
            feedback.append("Good resume length (1-2 pages)")
        else:
            suggestions.append("Keep resume to 1-2 pages maximum")
        
        # Check for consistent spacing
        empty_lines = sum(1 for line in self.lines if not line.strip())
        if 0.1 < empty_lines / len(self.lines) < 0.3:
            score += 15
            feedback.append("Good use of whitespace")
        else:
            suggestions.append("Improve use of whitespace for readability")
        
        # Check for bullet points
        bullet_count = sum(1 for line in self.lines if line.strip().startswith(('-', '*', '+')))
        if bullet_count > 5:
            score += 20
            feedback.append("Good use of bullet points")
        else:
            suggestions.append("Use bullet points for better readability")
        
        # Check for consistency
        if len(self.contact_info.email) > 0:
            score += 15
            feedback.append("Contact information present")
        else:
            suggestions.append("Include email address for contact")
        
        # Check for dates
        date_pattern = r'\b(20\d{2}|19\d{2})\b'
        dates = re.findall(date_pattern, self.resume_text)
        if len(dates) >= 2:
            score += 15
            feedback.append("Dates included in experience/education")
        else:
            suggestions.append("Include dates for all experiences")
        
        # Check for action verbs
        action_verbs = [
            'led', 'managed', 'developed', 'created', 'implemented',
            'designed', 'improved', 'increased', 'reduced', 'optimized',
            'coordinated', 'collaborated', 'analyzed', 'delivered'
        ]
        action_verb_count = sum(
            1 for verb in action_verbs
            if verb.lower() in self.resume_text.lower()
        )
        if action_verb_count > 5:
            score += 15
            feedback.append("Strong action verbs used")
        else:
            suggestions.append("Use more strong action verbs (e.g., led, managed, developed)")
        
        return AnalysisScore(
            category="Formatting",
            score=score,
            max_score=max_score,
            feedback=feedback,
            suggestions=suggestions
        )
    
    def analyze_content(self) -> AnalysisScore:
        """Analyze resume content quality."""
        score = 0
        max_score = 100
        feedback = []
        suggestions = []
        
        sections = self.extract_sections()
        
        # Check for all major sections
        required_sections = [
            SectionType.CONTACT.value,
            SectionType.EXPERIENCE.value,
            SectionType.EDUCATION.value,
            SectionType.SKILLS.value
        ]
        
        present_sections = 0
        for section in required_sections:
            if section in sections and sections[section].strip():
                present_sections += 1
        
        section_score = (present_sections / len(required_sections)) * 25
        score += section_score
        
        if present_sections == 4:
            feedback.append("All major sections present")
        else:
            suggestions.append(f"Include all major sections: {', '.join(required_sections)}")
        
        # Check experience section
        if SectionType.EXPERIENCE.value in sections:
            exp_text = sections[SectionType.EXPERIENCE.value]
            if len(exp_text.strip()) > 50:
                score += 25
                feedback.append("Detailed experience section")
            else:
                suggestions.append("Expand your experience section with more details")
        else:
            suggestions.append("Add work experience section")
        
        # Check for quantifiable achievements
        numbers = re.findall(r'\b\d+[%$K-]?\b', self.resume_text)
        if len(numbers) >= 5:
            score += 25
            feedback.append("Quantifiable achievements included")
        else:
            suggestions.append("Add quantifiable metrics (percentages, dollar amounts, numbers)")
        
        # Check for skills
        if SectionType.SKILLS.value in sections:
            skills_text = sections[SectionType.SKILLS.value]
            skill_items = [s.strip() for s in re.split('[,\n]', skills_text) if s.strip()]
            if len(skill_items) >= 10:
                score += 25
                feedback.append("Comprehensive skills section")
                self.skills = skill_items
            else:
                suggestions.append("Expand skills section with more relevant skills")
        else:
            suggestions.append("Add a skills section")
        
        return AnalysisScore(
            category="Content",
            score=score,
            max_score=max_score,
            feedback=feedback,
            suggestions=suggestions
        )
    
    def analyze_keywords(self) -> AnalysisScore:
        """Analyze resume for relevant keywords and ATS optimization."""
        score = 0
        max_score = 100
        feedback = []
        suggestions = []
        
        # Common tech keywords
        tech_keywords = [
            'python', 'java', 'javascript', 'sql', 'aws', 'azure',
            'agile', 'git', 'rest api', 'machine learning', 'data',
            'react', 'nodejs', 'docker', 'kubernetes', 'ci/cd'
        ]
        
        found_keywords = []
        for keyword in tech_keywords:
            if keyword.lower() in self.resume_text.lower():
                found_keywords.append(keyword)
        
        if len(found_keywords) >= 5:
            score += 50
            feedback.append(f"Good keyword coverage ({len(found_keywords)} keywords found)")
        else:
            score += (len(found_keywords) / 5) * 50
            suggestions.append("Add more relevant technical keywords for better ATS optimization")
        
        # Check for common phrases
        professional_phrases = [
            'increased', 'improved', 'developed', 'implemented',
            'led team', 'project management', 'cross-functional',
            'resulted in', 'achieved'
        ]
        
        found_phrases = sum(
            1 for phrase in professional_phrases
            if phrase.lower() in self.resume_text.lower()
        )
        
        if found_phrases >= 5:
            score += 30
            feedback.append("Professional language and phrases used")
        else:
            score += (found_phrases / 5) * 30
            suggestions.append("Use more professional achievement-oriented phrases")
        
        # Check for jargon/buzzwords
        if 'synergy' in self.resume_text.lower() or 'leverage' in self.resume_text.lower():
            suggestions.append("Avoid overused buzzwords like 'synergy' or 'leverage'")
        else:
            score += 20
            feedback.append("Avoids common resume cliches")
        
        return AnalysisScore(
            category="Keywords & ATS",
            score=score,
            max_score=max_score,
            feedback=feedback,
            suggestions=suggestions
        )
    
    def analyze_grammar(self) -> AnalysisScore:
        """Basic grammar analysis (simple checks)."""
        score = 50
        max_score = 100
        feedback = []
        suggestions = []
        
        # Check for common typos/issues
        issues = [
            (r'\brecieved\b', 'received'),
            (r'\bencourage\b', 'encouraged'),
            (r'\bExperiance\b', 'Experience'),
        ]
        
        found_issues = []
        for pattern, correction in issues:
            if re.search(pattern, self.resume_text, re.IGNORECASE):
                found_issues.append((pattern, correction))
        
        if not found_issues:
            score += 25
            feedback.append("No common spelling errors detected")
        else:
            suggestions.append(f"Fix spelling: {', '.join([f'{p[0]} -> {p[1]}' for p in found_issues])}")
        
        # Check sentence structure
        sentences = re.split(r'[.!?]+', self.resume_text)
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        
        if 8 < avg_sentence_length < 20:
            score += 25
            feedback.append("Good sentence structure and length")
        else:
            suggestions.append("Vary sentence length for better readability")
        
        return AnalysisScore(
            category="Grammar & Language",
            score=score,
            max_score=max_score,
            feedback=feedback,
            suggestions=suggestions
        )
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive analysis report."""
        self.extract_contact_info()
        
        # Run all analyses
        formatting_score = self.analyze_formatting()
        content_score = self.analyze_content()
        keywords_score = self.analyze_keywords()
        grammar_score = self.analyze_grammar()
        
        self.analysis_results = {
            'formatting': formatting_score,
            'content': content_score,
            'keywords': keywords_score,
            'grammar': grammar_score,
        }
        
        # Calculate overall score
        total_score = sum(s.score for s in self.analysis_results.values())
        total_max = sum(s.max_score for s in self.analysis_results.values())
        overall_percentage = (total_score / total_max) * 100
        
        # Compile all suggestions
        all_suggestions = []
        for analysis in self.analysis_results.values():
            all_suggestions.extend(analysis.suggestions)
        
        report = {
            'contact_info': asdict(self.contact_info),
            'overall_score': round(overall_percentage, 1),
            'category_scores': {
                k: {
                    'score': v.score,
                    'max_score': v.max_score,
                    'percentage': round((v.score / v.max_score) * 100, 1),
                    'feedback': v.feedback,
                    'suggestions': v.suggestions
                }
                for k, v in self.analysis_results.items()
            },
            'top_suggestions': all_suggestions[:5],
            'total_suggestions': len(all_suggestions)
        }
        
        return report


if __name__ == "__main__":
    sample_resume = """
    John Doe
    john.doe@email.com | (555) 123-4567
    
    PROFESSIONAL EXPERIENCE
    Senior Engineer | Tech Company | 2020 - Present
    - Led development of microservices
    - Improved system performance by 40%
    
    EDUCATION
    Bachelor of Science | University | 2018
    
    SKILLS
    Python, JavaScript, AWS, Docker
    """
    
    analyzer = ResumeAnalyzer(sample_resume)
    report = analyzer.generate_report()
    print(f"Overall Score: {report['overall_score']}/100")
