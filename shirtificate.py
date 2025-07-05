from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 38)
    pdf.cell(44)
    pdf.cell(10, 10,"CS50 Shirtificate", "C")
    pdf.ln(25)
    pdf.image("shirtificate.png", x=0.5, y=40)
    pdf.set_font("courier", "B", 20)
    pdf.set_text_color(255,255,255)
    pdf.cell(50)
    pdf.cell(10, 155,f"{name} took CS50", "C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()