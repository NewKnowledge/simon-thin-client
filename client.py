import numpy as np
import pandas
import pickle
import traceback
import requests
from json import JSONDecoder
from typing import List


class SimonThinClient:
    def __init__(self, address: str):
        self.address = address
        self.decoder = JSONDecoder()

    def processNumpyArray(self, array: np.ndarray, input_data_shape = None, input_data_types = None, first_value_label = False) -> str:
        """ Accept a numpy array, process it 
        with the primitive, and return a JSON string
        with the results
        array: the numpy array to process with the primitive
        -> a json string containing the results of running the primitive
        """
        # Strip labels out -- we dont use them in any of our primitives (yet?)
        if(first_value_label):
            array = array[:,1:]

        try:
            r = requests.post(self.address, data = pickle.dumps(array))
            return self.decoder.decode(r.text)
        except:
            # Should probably do some more sophisticated error logging here
            return "Failed serializing and posting data to container"


    def processArray(self, array: List[List[str]], input_data_shape = None, input_data_types = None, first_value_label = False) -> str:
        """ Translate the python array to numpy array and pass 
        processing onto processNumpyArray
        """
        return self.processNumpyArray(np.array(array), input_data_shape, input_data_types, first_value_label)


    def processDataFrame(self, frame: pandas.DataFrame) -> str:
        """ Accept a pandas data frame, extract the contents
        into a numpy array, and pass to "processArray"
        frame: a pandas data frame containing the data to be processed
        -> a json string containing the results of running the primitive
        """
        try:
            return self.processArray(frame.values)
        except:
            return "Failed extracting values from data frame"


    def processCSVFile(self, fileName):
        """ Accept a local or hosted path to a csv file, load that file
        into a pandas DataFrame, and pass to processDataFrame
        fileName: the relative or full path to a csv file
        -> a json string containing the results of running the primitive
        """
        try:
            r = requests.post(self.address + "/fileName", data = fileName)
            return self.decoder.decode(r.text)
        except:
            return "Failed to open file " + str(fileName) + " as csv"


if __name__ == '__main__':
    address = 'http://localhost:5000/'
    client = SimonThinClient(address)
    results = client.processArray(np.array([[1,2],[3,4]]))
    print(results)