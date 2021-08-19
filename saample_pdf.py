from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times",'',10)
pdf.cell(20,5,"this is sample pdf bnvhdzbvjdb",0,1)
pdf.output('sample.pdf')