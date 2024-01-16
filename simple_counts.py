import csv



def get_data(file_name):
    """
        Gets the header and all the rows from the given file
    """
    data = []
    header = None
    with open(file_name,'r') as file:
        csvFile = csv.reader(file)
        flag = 0
        for line in csvFile:
            if not flag:
                header = line
                flag =1
                continue
            data.append(line)
    return {
        'header' : header,
        'data' : data
    }

def get_tag_frequencies(file_data, col_number):
    """
        Calculates the frequencies of occurence of each tag
    """

    tag_frequencies = {}
    for i in file_data['data']:
        tag_in_row = i[col_number].split("|||")
        for tag in tag_in_row:
            tag_frequencies[tag] = tag_frequencies.get(tag,0) + 1
    return tag_frequencies

def ouput_frequencies_to_file(file_name, tag_frequencies):
    """
        Writes the tag frequencies to the given filename as csv
    """
    output_data = list(tag_frequencies.items())
    output_data.sort(key=lambda x: x[1], reverse= True)
    with open(file_name, 'w',newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(output_data)


if __name__ == '__main__':
    filename = input('Enter file name: ')

    csv_data = get_data(filename)

    tag_counts = get_tag_frequencies(csv_data, 0)
    ouput_frequencies_to_file(filename +'frequencies.csv', tag_counts)
