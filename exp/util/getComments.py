from typing import List
import pandas as pd

"""
get comments for dataframe
comments can be filtered by speaker or party name

input:
    - dataFrame: a pandas DataFrame with rows "sentences", "main-speaker" and "main-speaker-party"
    - speakerFilter: speaker name to filter speeches by
    - partyFilter party name to filter speeches by

output:
    List of comments
"""


def getComments(dataFrame: pd.DataFrame, speakerFilter: str = None, partyFilter: str = None) -> List[str]:
    comments = []
    for (sentences, speaker, party) in zip(dataFrame["sentences"], dataFrame["main-speaker"], dataFrame["main-speaker-party"]):
        if (speakerFilter is None or speaker == speakerFilter) and (partyFilter is None or party == partyFilter):
            for sentence in sentences:
                if "comment" in sentence:
                    comments.append(sentence["comment"])
    return comments
