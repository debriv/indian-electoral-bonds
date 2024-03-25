import tabula
import warnings
import pandas

warnings.simplefilter(action='ignore', category=FutureWarning)

base_source_path = "ec_released_bond_data_files/"
base_destination_path = "pdf_parser/parsed_pdfs/"
file_name_list = [
    "electoral_bonds_disclosure_21_1",
    "electoral_bonds_disclosure_21_2",
    "electoral_bonds_disclosure_sbi_1",
    "electoral_bonds_disclosure_sbi_2"
                  ]

for file_name in file_name_list:
    print(
        f"{base_source_path}{file_name}.pdf",
        " started to be parsed into ", 
        f"{base_destination_path}{file_name}.csv"
        )
    tabula.convert_into(f"{base_source_path}{file_name}.pdf", 
                        f"{base_destination_path}{file_name}.csv", 
                        pages = 'all',
                        output_format="csv", 
                        stream=True)
    print(
        f"{base_source_path}{file_name}.pdf",
        " parsing is complete and the csv is available at ", 
        f"{base_destination_path}{file_name}.csv"
        )
