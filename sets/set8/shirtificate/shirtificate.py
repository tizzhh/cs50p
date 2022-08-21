from fpdf import FPDF

name = input("Name: ").strip()

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 30)
pdf.cell(0, 0, "CS50 Shirtificate", new_x = "LMARGIN", align = "C")
pdf.image("shirtificate.png", w = pdf.epw, y = 40)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 170, name, new_x = "LMARGIN", align = "C")
pdf.output("shirtificate.pdf")

