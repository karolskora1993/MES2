class DataWriter(object):
    @staticmethod
    def writeData(data, fileName):

        with open(fileName, 'w') as file:
            file.write(data)

