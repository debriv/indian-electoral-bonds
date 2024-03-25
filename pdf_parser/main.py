import tabula
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas
pdf_path = "ec_released_bond_data_files/electoral_bonds_disclosure_21_1.pdf"

# dfs = tabula.read_pdf(pdf_path, pages=3, stream=True)
# # read_pdf returns list of DataFrames
tabula.convert_into(pdf_path, "pdf_parser/parsed_pdfs/electoral_bonds_disclosure_21_1.csv", pages = 'all'
                    ,output_format="csv", stream=True)
# print(dfs)