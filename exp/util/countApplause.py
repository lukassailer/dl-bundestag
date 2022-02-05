from typing import List
import pandas as pd


def countApplause(commentList: List[str]) -> pd.DataFrame:
    """
    Count applause given by each party for a list of comments

    input:
        commentList: a list of comments

    output:
        pandas DataFrame linking each party to the times they applauded
    """
    # matchers are minimal to also match other forms (e.g. genitive)
    partyMatchers = ["AfD", "GRÜNE", "CDU/CSU", "LINKE", "FDP", "SPD"]

    # only take the part before "–" to drop to drop further comments
    applause = "".join([comment.split("–")[0]
                       for comment in commentList if "Beifall" in comment])

    applauseDF = pd.DataFrame(
        [{"party": party, "applause count": applause.count(party)} for party in partyMatchers])
    return applauseDF
