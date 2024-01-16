import pandas as pd 

def get_data(file_name):
    """
        Gets the header and all the rows from the given file
    """
    data = []
    header = None

    df = pd.read_excel(file_name)
    print(df)
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

get_data('Testing Tag Counts.xlsx')