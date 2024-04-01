import os
import PyPDF2

def extract_text_from_pdf(input_path):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
        return text

def save_text_to_pdf(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

def convert_folder_to_text_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            text = extract_text_from_pdf(input_path)
            save_text_to_pdf(text, output_path)

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    convert_folder_to_text_pdf(input_folder, output_folder)
