import streamlit as st
import requests

def get_section(file_content, section_number):
    sections = file_content.split('\n')
    found_sections = []
    for line in sections:
        if line.strip().startswith("Section"):
            current_section_number = line.strip().split(" ")[1]
            if current_section_number == str(section_number):
                found_sections.append(line)
            elif found_sections:
                break
        elif found_sections:
            found_sections.append(line)
    return '\n'.join(found_sections)

# Streamlit UI
st.title('Text Viewer - Adi Parva')

# File paths
file_paths = ['https://raw.githubusercontent.com/Mnb24/MBAnalysis/main/BD1.txt', 
              'https://raw.githubusercontent.com/Mnb24/MBAnalysis/main/KMG1.txt', 
              'https://raw.githubusercontent.com/Mnb24/MBAnalysis/main/MND1.txt']

# File names
file_names = ["Bibek Debroy's", "KM Ganguly's", "MN Dutt's"]

# Allow user to input section number
section_number = st.number_input('Enter the section number (1 to 236):', min_value=1, step=1)

if st.button('View Section'):
    for i, (file_path, file_name) in enumerate(zip(file_paths, file_names)):
        response = requests.get(file_path)
        file_content = response.text
        section_content = get_section(file_content, section_number)
        st.markdown(f"## Section {section_number} from {file_name}:")
        st.write(section_content)
