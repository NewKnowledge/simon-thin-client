import os.path
import numpy as np
import pandas
import pickle
import requests
import ast
import typing
from json import JSONDecoder
from typing import List
from primitive_interfaces.base import PrimitiveBase, CallResult

from d3m_metadata import container, hyperparams, metadata as metadata_module, params, utils

__author__ = 'Distil'
__version__ = '1.0.0'

Inputs = container.List[container.pandas.DataFrame]
Outputs = container.List[container.List[str]]

class Params(params.Params):
    pass


class Hyperparams(hyperparams.Hyperparams):
    pass

class simon(PrimitiveBase[Inputs, Outputs, Params, Hyperparams]):
    metadata = metadata_module.PrimitiveMetadata({
        # Simply an UUID generated once and fixed forever. Generated using "uuid.uuid4()".
        'id': "d2fa8df2-6517-3c26-bafc-87b701c4043a",
        'version': __version__,
        'name': "simon",
        # Keywords do not have a controlled vocabulary. Authors can put here whatever they find suitable.
        'keywords': ['Data Type Predictor'],
        'source': {
            'name': __author__,
            'uris': [
                # Unstructured URIs.
                "https://github.com/NewKnowledge/simon-thin-client",
            ],
        },
        # A list of dependencies in order. These can be Python packages, system packages, or Docker images.
        # Of course Python packages can also have their own dependencies, but sometimes it is necessary to
        # install a Python package first to be even able to run setup.py of another package. Or you have
        # a dependency which is not on PyPi.
         'installation': [{
            'type': metadata_module.PrimitiveInstallationType.PIP,
            'package_uri': 'git+https://github.com/NewKnowledge/simon-thin-client.git@{git_commit}#subdirectory='.format(
                git_commit=utils.current_git_commit(os.path.dirname(__file__)),
            ),
        }],
        # The same path the primitive is registered with entry points in setup.py.
        'python_path': 'd3m.primitives.distil.simon',
        # Choose these from a controlled vocabulary in the schema. If anything is missing which would
        # best describe the primitive, make a merge request.
        'algorithm_types': [
            metadata_module.PrimitiveAlgorithmType.CONVOLUTIONAL_NEURAL_NETWORK,
        ],
        'primitive_family': metadata_module.PrimitiveFamily.DATA_CLEANING,
    })
    
    def __init__(self, *, hyperparams: Hyperparams, random_seed: int = 0, docker_containers: typing.Dict[str, str] = None)-> None:
        super().__init__(hyperparams=hyperparams, random_seed=random_seed, docker_containers=docker_containers)
                
        self._decoder = JSONDecoder()
        self._params = {}

    def fit(self) -> None:
        pass
    
    def get_params(self) -> Params:
        return self._params

    def set_params(self, *, params: Params) -> None:
        self.params = params

    def set_training_data(self, *, inputs: Inputs, outputs: Outputs) -> None:
        pass
        
    def produce(self, *, inputs: Inputs, timeout: float = None, iterations: int = None) -> CallResult[Outputs]:
        """
        Produce primitive's best guess for the structural type of each input column.
        
        Parameters
        ----------
        inputs : Input pandas frame

        Returns
        -------
        Outputs
            The outputs is a list that has length equal to number of columns in input pandas frame. 
            Each entry is a list of strings corresponding to each column's multi-label classification.
        """
        
        """ Accept a pandas data frame, predicts column types in it
        frame: a pandas data frame containing the data to be processed
        -> a list of lists of column labels
        """
        
        frame = inputs[1]
        
        try:
            r = requests.post(inputs[0], data = pickle.dumps(frame))
            return self.decoder.decode(r.text)
        except:
            # Should probably do some more sophisticated error logging here
            return "Failed predicting data frame"


if __name__ == '__main__':
    address = 'http://localhost:5000/'
    client = simon(hyperparams={})
    # frame = pandas.read_csv("https://query.data.world/s/10k6mmjmeeu0xlw5vt6ajry05",dtype='str')
    frame = pandas.read_csv("https://s3.amazonaws.com/d3m-data/merged_o_data/o_4550_merged.csv",dtype='str')
    results = client.produce(inputs = list([address,frame]))
    print(results)