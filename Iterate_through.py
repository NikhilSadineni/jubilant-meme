import os

from xlsx_counts import get_tag_frequencies, ouput_frequencies_to_file

def get_frequencies_for_all_files(directory_path):
    """
        Given a directory_path get frequencies
        for all files
    """
    for root,subdirs,files in os.walk(directory_path):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension == '.xlsx':
                path = root + "\\"+file
                print(f'Processing {path}')
                tag_frequencies = get_tag_frequencies(root + "\\"+file, 'Test_Column')        
                ouput_frequencies_to_file(root +"\\" +  file + '-frequencies.csv',tag_frequencies)

if __name__ == '__main__':
    get_frequencies_for_all_files(r"C:\Users\nikhi\Desktop\Files\XpertDox\SAS_QC_Counts")
