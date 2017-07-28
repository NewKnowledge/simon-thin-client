# simon-thin-client
Thin client for interacting with dockerized TA1 primitives. All code is written in Python 3.5 and must be run in 3.5 or greater. 

## Output
The output for every function should be as follows:
An array with two values, the first being an array of column indices for the labels, and the second being an array of labels.
Every value in the labels array should be a JSON string containing the set of labels for a given column. This output must be provided by the model. If it is better to just fix the order of the labels before returning, rather than including an index, then that will require modifying the expected output signature of the included functions. 

e.g. if all labels are text and the order of labels matches the order in the source file, the output shoudl be as follows:

```[[0, 1, 2, 3], ["['text']", "['text']", "['text']", "['text']"]]```

if the second column contains money, but was ordered last in the output, it should be as follows:

```[[0, 2, 3, 1], ["['text']", "['text']", "['text']", "['money']"]]```

if the second column contains both text and coordinates, it should be as follows:

```[[0, 1, 2, 3], ["['text']", "['text', 'coordinates']", "['text']", "['text']"]]```


## Available Functions

#### processNumpyArray
This is the function that the next two reference. It accepts a numpy array, removes the first row if it includes the headers, and then serializes it with pickle and sends it to a REST endpoint using POST. 

#### processArray
Accepts a standard python array as input and translates it to a numpy array and passes it to processNumpyArray

#### processDataFrame
Extracts the values from the data frame as a numpy arry and passes it to the processNumpyArray function

#### processCSVFile
Accepts a filename instead of an array, and passes that filename to a different endpoint on the Simon REST api. The api will then load the file using pandas and process the values as if they were passed in as a numpy array. NOTE: This is lightly tested, and is largely included as a demonstration of how to add this functionality in case we need to provide it in the future. I would recommend not providing it as an option for end users without some more thorough testing first. 