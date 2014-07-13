import requests

from core import ParseRidersList, AppState
from util import SecondsToMinutesSeconds
from teams import TIMS_TEAM, ALEX_TEAM, PICOT_TEAM

def ParseStageRank(stage, riderlist):
    stageString = "{0:02}00".format(stage)
    ranks = requests.get('http://www.letour.fr/useradgents/2014/json/afterrank{StageNum}.json'.format(StageNum=stageString)).json()
    for index, posInfo in enumerate(ranks[u'ite'][u'r']):
        riderNum = posInfo[u'r']
        if index == 0:
            winnerTime = posInfo[u's']

        timeDiff = posInfo[u's'] - winnerTime
        print(u"{0:<7} - #{1:<3} {2:<32} - +{3:<5}".format(SecondsToMinutesSeconds(posInfo[u's']),
                                                           riderList[riderNum]['Number'],
                                                           riderList[riderNum]['Name'],
                                                           SecondsToMinutesSeconds(timeDiff)))

        if riderNum in TIMS_TEAM:
            print("\t\tIn my Team")
        if riderNum in ALEX_TEAM:
            print("\t\tIn Alex's Team")
        if riderNum in PICOT_TEAM:
            print("\t\tIn Picot's Team")

if __name__ == '__main__':
    stageNum = AppState()['CurrentStage']
    riderList = ParseRidersList(currentRiders=True)
    ParseStageRank(stageNum - 1, riderList)
