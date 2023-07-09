from config import getScoreList
from util import isTextHasOneThingsInlist


def getScore(resultList):
    score = 0
    scoredict = {}
    scorelist = getScoreList()
    actualResultList = resultList[0][1:]
    actualResultList.append([" ", " "])
    for index, item in enumerate(actualResultList):
        if(index == 10):
            break
        # 我们认为最后一句最有可能包含信息
        mostLikelyContainsInfoText = item[-1]
        actualResult = False
        for scoreItem in scorelist.items():
            if actualResult:
               continue
            if isTextHasOneThingsInlist(mostLikelyContainsInfoText, scoreItem[1]):
                score += int(scoreItem[0])
                actualResult = True
                scoredict[str(index)] = int(scoreItem[0])

        if not  actualResult:
            allInfo = []
            # 这个放前面，因为这个最可能有
            allInfo+=actualResultList[index+1][0].split("。|?|，")
            allInfo += item[0:-1]
            for text in allInfo:
                for scoreItem in scorelist.items():
                    if actualResult:
                        continue
                    if isTextHasOneThingsInlist(mostLikelyContainsInfoText, scoreItem[1]):
                        score += int(scoreItem[0])
                        actualResult = True
                        scoredict[str(index)] = int(scoreItem[0])

    return  scoredict

