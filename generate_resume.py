from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def create_resume():
    # ✅ images folder ထဲမှာ output ထုတ်မယ်
    output_folder = os.path.join(os.getcwd(), "images")
    os.makedirs(output_folder, exist_ok=True)

    pdf_path = os.path.join(output_folder, "resume.pdf")

    # PDF Setup
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Header
    elements.append(Paragraph("<b>Myat Thu</b>", styles["Title"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Computer Technology (Embedded Systems), UCSM", styles["Normal"]))
    elements.append(Paragraph("Intermediate English | JLPT N4 | Python | Java | HTML | CSS | JS | Android", styles["Normal"]))
    elements.append(Spacer(1, 20))

    # Skills
    elements.append(Paragraph("<b>Skills</b>", styles["Heading2"]))
    elements.append(Paragraph("- Python, Java, HTML, CSS, JavaScript", styles["Normal"]))
    elements.append(Paragraph("- Android Development", styles["Normal"]))
    elements.append(Paragraph("- Flask Framework (Basic Backend)", styles["Normal"]))
    elements.append(Spacer(1, 15))

    # Education
    elements.append(Paragraph("<b>Education</b>", styles["Heading2"]))
    elements.append(Paragraph("University of Computer Studies, Mandalay — 4th Year (Computer Technology, Embedded Systems)", styles["Normal"]))
    elements.append(Spacer(1, 15))

    # Languages
    elements.append(Paragraph("<b>Languages</b>", styles["Heading2"]))
    elements.append(Paragraph("English — Intermediate", styles["Normal"]))
    elements.append(Paragraph("Japanese — JLPT N4", styles["Normal"]))

    doc.build(elements)
    print(f"✅ Resume PDF created successfully at: {pdf_path}")

if __name__ == "__main__":
    create_resume()