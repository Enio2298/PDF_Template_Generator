from fpdf import FPDF
import pandas as pd

# Los argumentos son "P" por portrait y "L" por Landscape
# "mm" está por milimetros

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Marca la parte de arriba de la página
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.set_draw_color(254, 95, 85)
    pdf.set_line_width(1)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1, border=0)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    ye = 21
    while ye < 276:
        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0)
        pdf.line(x1=10, y1=ye + 10, x2=200, y2=ye + 10)
        ye = ye + 10

        # Marcan el pie de página para la página principal
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        ye = 11
        while ye < 276:
            pdf.line(x1=10, y1=ye + 10, x2=200, y2=ye + 10)
            ye = ye + 10

pdf.output("output.pdf")
