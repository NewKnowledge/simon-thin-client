# simon-thin-client
Thin client for interacting with dockerized TA1 primitives. All code is written in Python 3.5 and must be run in 3.5 or greater. 

## Output
The output for every function should be as follows:
A list of lists of labels.

e.g. if all labels are text (remember that the order of labels matches the order in the source file), the output shoudl be as follows:

```[["['text']", "['text']", "['text']", "['text']"]]```

## Available Functions

#### processDataFrame
This is the main function we use to communicate in the D3M environment. Passes input pandas data frame it to the listener.predict function, and returns a list of lists of label strings.

Additionally, the following functions are provided as part of the API:


#### processNumpyArray
This is the function that the next two reference. It accepts a numpy array, removes the first row if it includes the headers, and then serializes it with pickle and sends it to a REST endpoint using POST. 

#### processArray
Accepts a standard python array as input and translates it to a numpy array and passes it to processNumpyArray


#### processCSVFile
Accepts a filename instead of an array, and passes that filename to a different endpoint on the Simon REST api. The api will then load the file using pandas and process the values as if they were passed in as a numpy array. NOTE: This is lightly tested, and is largely included as a demonstration of how to add this functionality in case we need to provide it in the future. I would recommend not providing it as an option for end users without some more thorough testing first. 