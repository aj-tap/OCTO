from csv import DictWriter


class WriterCsv:

    def __init__(self, filename="result.csv"):
        self.filename = filename
        self.header_csv = ['FRAME', 'INDEX', 'TYPE', 'CFLVL']
        self.create_file()

    def create_file(self):
        with open(self.filename, 'w', ) as csvfile:
            dictwriter_obj = DictWriter(csvfile, fieldnames=self.header_csv)
            dictwriter_obj.writeheader()
            csvfile.close()

    def append_data(self, data):
        with open(self.filename, 'a', newline='') as csvfile:
            dictwriter_obj = DictWriter(csvfile, fieldnames=self.header_csv)
            dictwriter_obj.writerow(data)
            csvfile.close()
