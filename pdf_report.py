from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.units import inch
from reportlab.lib import colors

def generate_interview_report(data, output_filename):
    if "interviewAnalysis" not in data:
        raise ValueError("Missing 'interviewAnalysis' key in input data.")
    
    analysis = data["interviewAnalysis"]

    doc = SimpleDocTemplate(output_filename, pagesize=A4,
                            rightMargin=40, leftMargin=40,
                            topMargin=60, bottomMargin=40)
    
    styles = getSampleStyleSheet()
    story = []

    def add_section(title, content, style_name="BodyText"):
        story.append(Paragraph(f"<b>{title}</b>", styles["Heading3"]))
        if isinstance(content, list):
            for item in content:
                story.append(Paragraph(f"- {item}", styles[style_name]))
        else:
            story.append(Paragraph(str(content), styles[style_name]))
        story.append(Spacer(1, 12))

    # Add sections
    add_section("Overall Feedback", analysis.get("overallFeedback", "N/A"))
    add_section("Strengths", analysis.get("strengths", []))
    add_section("Weaknesses", analysis.get("weaknesses", []))
    add_section("Recommendations", analysis.get("recommendations", []))
    add_section("Final Score", f"{analysis.get('finalScore', 'N/A')}/100")
    add_section("Score Justification", analysis.get("scoreJustification", "N/A"))
    add_section("Tips for Tackling the Interview", analysis.get("tipsForTacklingTheInterview", []))

    doc.build(story)
    print(f"PDF report generated: {output_filename}")
