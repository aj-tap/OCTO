from csv import DictWriter

class Writer: 

    def __init__(self,filename):
        headercsv = ['FRAME','INDEX','TYPE','CFLVL']
        self.filename = filename #result.csv ## add csv extension using join 
        with open(filename, 'w', ) as csvfile:
            dictwriter_obj = DictWriter(csvfile, fieldnames=headercsv)
            dictwriter_obj.writeheader()
            csvfile.close()

#with open(filename, 'a', newline='') as csvfile:
#						dictwriter_obj = DictWriter(csvfile, fieldnames=headercsv)
#						dictwriter_obj.writerow(temp)
#						csvfile.close()