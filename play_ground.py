
import aspose.pdf as ap

input_pdf =  """A000001.pdf"""
output_pdf =  f"{input_pdf}.xlsx"

# Open PDF document
document = ap.Document(input_pdf)

save_option = ap.ExcelSaveOptions()

# Save the file into MS Excel format
document.save(output_pdf, save_option)
