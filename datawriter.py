class DataWriter(object):
    @staticmethod
    def writeData(fileName, data):

        with open(fileName, 'w') as file:
            file.write(str(data))

