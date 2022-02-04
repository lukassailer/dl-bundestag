import pandas as pd

RESOURCE_FOLDER = '../res/'


def exportJson(dataFrame: pd.DataFrame, fileName: str):
    """
    write a pandas DataFrame into a json-formatted file

    input:
        - dataFrame: a pandas DataFrame with rows "sentences", "main-speaker" and "main-speaker-party"
        - fileName: the file name 
    """
    dataFrame.to_json(RESOURCE_FOLDER + fileName, orient='records')


def importJson(fileName: str) -> pd.DataFrame:
    """
    read a pandas DataFrame from a json-formatted file

    input:
        - fileName: the file name 

    output:
        - dataFrame: a pandas DataFrame with rows "sentences", "main-speaker" and "main-speaker-party"
    """
    return pd.read_json(RESOURCE_FOLDER + fileName, orient='records')
