#Prepare defanged iocs for a kql query in seconds
#kql_prepper v 1.2 Shawn Graham


import re
import os
import argparse

def refang_ip_or_domain(fanged):
    # Replace '[.]' with '.' and '[dot]' with '.'
    refanged = fanged.replace('[.]', '.').replace('[dot]', '.')
    # Replace '[://]' with '://'
    refanged = refanged.replace('[://]', '://')
    # Replace 'hxxp' with 'http'
    refanged = refanged.replace('hxxp', 'http')
    return refanged

def prep_iocs_for_kql(iocs):
    # Add quotation marks and commas to each IOC
    prepped_iocs = [f'"{ioc.strip()}"' for ioc in iocs]
    return prepped_iocs

def process_iocs(input_file_path, output_file_path):
    # Read the input file
    with open(input_file_path, 'r') as file:
        defanged_iocs = file.readlines()

    # Refang IOCs
    refanged_iocs = [refang_ip_or_domain(ioc.strip()) for ioc in defanged_iocs]

    # Prepare IOCs for KQL
    prepped_iocs = prep_iocs_for_kql(refanged_iocs)

    # Write prepped IOCs to output file
    with open(output_file_path, 'w') as file:
        for i, ioc in enumerate(prepped_iocs):
            if i < len(prepped_iocs) - 1:
                file.write(ioc + ',\n')
            else:
                file.write(ioc + '\n')

    print(f"Refanged and prepped IOCs have been written to {output_file_path}")

def display_cyberpunk_graphic(file_name):
    graphic = """
██╗  ██╗ ██████╗ ██╗             ██████╗ ██████╗ ███████╗██████╗ ██████╗ ███████╗██████╗
██║ ██╔╝██╔═══██╗██║             ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
█████╔╝ ██║   ██║██║             ██████╔╝██████╔╝█████╗  ██████╔╝██████╔╝█████╗  ██████╔╝
██╔═██╗ ██║▄▄ ██║██║             ██╔═══╝ ██╔══██╗██╔══╝  ██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██╗╚██████╔╝███████╗███████╗██║     ██║  ██║███████╗██║     ██║     ███████╗██║  ██║
╚═╝  ╚═╝ ╚══▀▀═╝ ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                     
    """
    print(graphic)
    print(f"Processing file: {file_name}")

def main():
    parser = argparse.ArgumentParser(description="Refang IOCs and prepare them for KQL.")
    parser.add_argument('input_file', help="Path to the input file containing defanged IOCs.")
    parser.add_argument('output_file', help="Path to the output file where prepped IOCs will be written.")
    args = parser.parse_args()

    display_cyberpunk_graphic(args.input_file)
    process_iocs(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
