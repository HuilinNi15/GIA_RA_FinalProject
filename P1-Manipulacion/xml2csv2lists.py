import xml.etree.ElementTree as ET
import csv
import os

def xml_to_csv(xml_file, csv_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find all Conf elements
    conf_elements = root.findall(".//Conf")

    # Open CSV file for writing
    with open(csv_file, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write components to CSV file
        for conf in conf_elements:
            components = conf.text.strip().replace("[", "").replace("]", "").replace("'", "").split()
            components_str = ', '.join(components[:6])
            csvwriter.writerow(components_str.split(', ')[:6])

def parse_xml_to_list_of_lists(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_of_lists = []
    path_counter = 1

    for element in root:
        if element.tag in ['Transit', 'Transfer']:
            current_group = []
            for conf in element.findall('Conf'):
                components = conf.text.strip().replace("[", "").replace("]", "").replace("'", "").split()
                # Convert string components to float
                components = [float(comp) for comp in components[:6]]
                current_group.append(components)
            list_of_lists.append((f"path{path_counter}", current_group, element.tag))
            path_counter += 1

    return list_of_lists

def save_to_txt(list_of_lists, txt_file):
    with open(txt_file, "w") as file:
        for path, group, tag in list_of_lists:
            file.write(f"{path} = [\n")
            for i, row in enumerate(group):
                if i == len(group) - 1:
                    file.write("    " + str(row) + "\n")
                else:
                    file.write("    " + str(row) + ",\n")
            file.write("] ")
            file.write(f"# {tag}\n\n")

# Lists of XML and corresponding CSV files
xml_files = ['taskfile_tampconfig_chess_red.xml', 'taskfile_tampconfig_chess_red_2.xml', 'taskfile_tampconfig_chess_red_3.xml']
csv_files = ['taskfile_tampconfig_chess_red.csv', 'taskfile_tampconfig_chess_red_2.csv', 'taskfile_tampconfig_chess_red_3.csv']

# Process each XML file
for xml_file, csv_file in zip(xml_files, csv_files):
    # Convert XML to CSV
    xml_to_csv(xml_file, csv_file)

    # Parse XML and convert to list of lists grouped by headers
    list_of_lists = parse_xml_to_list_of_lists(xml_file)

    # Determine the output text file name based on the XML file name
    base_name = os.path.splitext(xml_file)[0]
    txt_file = base_name + '.txt'

    # Save the list of lists to a text file
    save_to_txt(list_of_lists, txt_file)

    print(f"Output saved to {txt_file}")
