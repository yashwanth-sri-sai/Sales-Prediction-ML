import markdown
from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass

def generate():
    try:
        with open("interview_guide.md", "r", encoding="utf-8") as f:
            text = f.read()
        
        # Convert Markdown to HTML
        html = markdown.markdown(text)
        
        # Replace hr tags and standard formatting that fpdf2 can handle
        html = html.replace("<hr />", "<br><br>")
        
        pdf = MyFPDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=12)
        
        # FPDF2 HTMLMixin doesn't support all complex CSS, but standard tags work nicely
        pdf.write_html(html)
        pdf.output("Project_Interview_Guide.pdf")
        print("PDF generated successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate()
