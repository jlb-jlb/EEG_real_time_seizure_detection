from utils.data_loader import DataLoader
import logging


def format_csv_to_tse(filename: str):
    assert filename.endswith('.csv'), "filename must end with .csv"
    with open(filename, 'r') as f:
        data = f.read()
        # convert to list of lines
        data = data.split('\n')
        data = data[4:]
        # replace , with spaces
        data = [line.replace(',', ' ') for line in data]
        # remove empty lines
        data = [line for line in data if line != '']  
    
    # save data as .tse
    filename_tse = filename
    filename_tse = filename_tse.replace('.csv', '.tse')

    with open(filename_tse, 'w') as f:
        f.write('\n'.join(data))


    logging.debug(data[2:])
    # for line in data:
    #     print(line)


def format_csv_bi_to_tse_bi(filename: str):
    assert filename.endswith('.csv_bi') == True, "filename must end with .csv_bi"
    
    with open(filename, 'r') as f:
        data = f.read()
        # convert to list of lines
        data = data.split('\n')
        data = data[4:]
        # replace , with spaces
        data = [line.replace(',', ' ') for line in data]
        # remove empty lines
        data = [line for line in data if line != '']  
    
    # save data as .tse
    filename_tse = filename
    filename_tse = filename_tse.replace('.csv_bi', '.tse_bi')

    with open(filename_tse, 'w') as f:
        f.write('\n'.join(data))


    logging.debug(data[2:])
    # for line in data:
    #     print(line)


def main():
    TRAINING_DATA_PATH = "/home/joscha.l.bisping/bachelor_thesis/TUH_EEG_2/edf/train"
    data_loader = DataLoader(TRAINING_DATA_PATH, extensions=[".edf", ".csv", ".csv_bi"], shuffle=False)

    files = data_loader.get_next()
    while files is not None:
        file_dict = {"eeg": files[0], "csv": files[1], "csv_bi": files[2]}
        format_csv_to_tse(file_dict["csv"])
        format_csv_bi_to_tse_bi(file_dict["csv_bi"])
        print(" "*250, end="\r")
        print(file_dict["csv"], end="\r")

        files = data_loader.get_next()
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    logging.info("Starting preprocessing")
    main()
    logging.info("Finished preprocessing")
