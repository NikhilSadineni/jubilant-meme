import pandas as pd 
import csv


def get_tag_frequencies(file_name, col_name):
    """
        Calculates the frequencies of occurence of each tag
    """
    df = pd.read_excel(file_name)
    tag_frequencies = {}
    for i in df[col_name]:
        tag_in_row = str(i).split("|||")
        for tag in tag_in_row:
            tag_frequencies[tag] = tag_frequencies.get(tag,0) + 1
    return tag_frequencies

def ouput_frequencies_to_file(file_name, tag_frequencies):
    """
        Writes the tag frequencies to the given filename as csv
    """


    output_data = list(tag_frequencies.items())
    output_data.sort(key=lambda x: x[1], reverse= True)
    with open(file_name, 'w',newline='', encoding='utf-8') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Tag', 'Frequency'])
        # writing the data rows
        csvwriter.writerows(output_data)


if __name__ == '__main__':
    filename = input('Enter file name: ')

    tag_counts = get_tag_frequencies(filename, 'Test_Column')
    ouput_frequencies_to_file(filename +'-frequencies.csv', tag_counts)
