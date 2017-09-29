import numpy as np
import pandas
import pickle
import requests
import ast
from json import JSONDecoder
from typing import List
from primitive_interfaces.base import PrimitiveBase

Inputs = pandas.frame
Outputs = List[List[str]]
Params = dict
CallMetadata = dict

class simon(PrimitiveBase[Inputs, Outputs, Params]):
    __author__ = "distil"
    __metadata__ = {}
    def __init__(self, address: str)-> None:
        self.address = address
        self.decoder = JSONDecoder()
        self.callMetadata = {}
        self.params = {}

    def fit(self) -> None:
        pass
    
    def get_params(self) -> Params:
        return self.params

    def set_params(self, params: Params) -> None:
        self.params = params

    def get_call_metadata(self) -> CallMetadata:
        return self.callMetadata
        
    def produce(self, *, inputs: Inputs, timeout: float = None, iterations: int = None) -> Outputs:
        """
        Produce primitive's best guess for the structural type of each input column.
        
        Parameters
        ----------
        inputs : Input pandas frame
        
        timeout : float
            A maximum time this primitive should take to produce outputs during this method call, in seconds.
            Inapplicable for now...
        iterations : int
            How many of internal iterations should the primitive do. Inapplicable for now...

        Returns
        -------
        Outputs
            The outputs is a list that has length equal to number of columns in input pandas frame. 
            Each entry is a list of strings corresponding to each column's multi-label classification.
        """
        return self.processDataFrame(Inputs)

    def processNumpyArray(self, array: np.ndarray, input_data_shape = None, input_data_types = None, first_value_label = False) -> str:
        """ Accept a numpy array, process it 
        with the primitive, and return a JSON string
        with the results
        array: the numpy array to process with the primitive
        -> a list of JSON strings, one string for each column in the source data
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
        """ Accept a pandas data frame, predicts column types in it
        frame: a pandas data frame containing the data to be processed
        -> a list of lists of column labels
        """
        
        try:
            r = requests.post(self.address, data = pickle.dumps(frame))
            return self.decoder.decode(r.text)
        except:
            # Should probably do some more sophisticated error logging here
            return "Failed predicting data frame"


    def translateStringToList(self, listString: str) -> List[str]:
        """ Provided as a helper function to translate the string of labels
        for each column into a proper python list of strings. Not sure whether
        or not we want to expose this, but I'm providing it just in case
        """
        return ast.literal_eval(listString)

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
    client = simon(address)
    # frame = pandas.read_csv("https://query.data.world/s/10k6mmjmeeu0xlw5vt6ajry05",dtype='str')
    frame = pandas.read_csv("https://s3.amazonaws.com/d3m-data/merged_o_data/o_4550_merged.csv",dtype='str')
    results = client.processDataFrame(frame)
    print(results)