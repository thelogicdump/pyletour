import requests

from core import ParseRidersList, AppState
from util import SecondsToMinutesSeconds
from teams import TIMS_TEAM, ALEX_TEAM, PICOT_TEAM

def ParseCurrentState(stage, riderlist):
    stageString = "{0:02}00".format(stage)
    currentRanks = requests.get('http://www.letour.fr/useradgents/2014/json/livestage{StageNum}.json'.format(StageNum=stageString)).json()
    for index, group in enumerate(currentRanks['g']):
        print("Group {0}".format(index + 1))
        if u'd' in group:
            print("Behind by {0}".format(SecondsToMinutesSeconds(group[u'd'])))
        if u'r' in group:
            for riderInfo in group[u'r']:
                riderNum = riderInfo[u'r']
                print(u"\t{0:<3} - {1:<32} - GCPos {2:<3} - GCTime +{3:<7}".format(riderList[riderNum]['Number'],
                                                                                   riderList[riderNum]['Name'],
                                                                                   riderInfo[u'p'],
                                                                                   SecondsToMinutesSeconds(riderInfo[u't'])))
                if riderNum in TIMS_TEAM:
                    print("\t\tIn my Team")
                if riderNum in ALEX_TEAM:
                    print("\t\tIn Alex's Team")
                if riderNum in PICOT_TEAM:
                    print("\t\tIn Picot's Team")
        else:
            print("Pelaton")

if __name__ == '__main__':
    stageNum = AppState()['CurrentStage']
    riderList = ParseRidersList(currentRiders=True)
    ParseCurrentState(stageNum, riderList)
