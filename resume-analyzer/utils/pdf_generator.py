from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

def build_resume_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(f"<b>{data.get('name','')}</b>", styles["Title"]))
    story.append(Spacer(1, 10))

    contact = " | ".join(filter(None, [
        data.get("email"),
        data.get("phone"),
        data.get("location")
    ]))
    story.append(Paragraph(contact, styles["Normal"]))
    story.append(Spacer(1, 12))

    if data.get("summary"):
        story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
        story.append(Paragraph(data["summary"], styles["Normal"]))
        story.append(Spacer(1, 12))

    if data.get("skills"):
        story.append(Paragraph("<b>Skills</b>", styles["Heading2"]))
        story.append(Paragraph(", ".join(data["skills"]), styles["Normal"]))
        story.append(Spacer(1, 12))

    if data.get("experience"):
        story.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
        for exp in data["experience"]:
            story.append(Paragraph(
                f"<b>{exp.get('role')}</b> - {exp.get('company')} ({exp.get('duration','')})",
                styles["Normal"]
            ))
            for b in exp.get("bullets", []):
                story.append(Paragraph(f"• {b}", styles["Normal"]))
            story.append(Spacer(1, 10))

    if data.get("projects"):
        story.append(Paragraph("<b>Projects</b>", styles["Heading2"]))
        for proj in data["projects"]:
            story.append(Paragraph(f"<b>{proj.get('title')}</b>", styles["Normal"]))
            story.append(Paragraph(proj.get("description",""), styles["Normal"]))
            story.append(Spacer(1, 10))

    if data.get("education"):
        story.append(Paragraph("<b>Education</b>", styles["Heading2"]))
        for edu in data["education"]:
            story.append(Paragraph(
                f"{edu.get('degree')} - {edu.get('institution')}",
                styles["Normal"]
            ))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()