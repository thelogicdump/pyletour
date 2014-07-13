from pprint import pprint
import string

import requests

APPSTATE_URL = 'http://www.letour.fr/useradgents/2014/json/appState.json'

def AppState(printState=False):
    appState = requests.get('http://www.letour.fr/useradgents/2014/json/appState.json').json()
    if printState:
        pprint(appState)
    return {'CurrentStage': int(appState[u'stage'][0:2])}

def ParseRidersList(currentRiders=False):
    riderList = {}
    teamList = {}
    riders = requests.get('http://www.letour.fr/useradgents/2014/json/starters.json').json()
    for rider in riders['r']:
        # print(rider)
        riderList[rider['n']] = {"Name": u"{0} {1}".format(rider['f'], string.capwords(rider['l'])),
                                 "Number": rider['n'],
                                 "UID": rider['b'],
                                 "Country": rider['c'],
                                 "Dropped": False}
    for team in riders['t']:
        # print(team)
        teamList[team['n']] = {"Name": team['d'].lower(),
                               "Number": team['n'],
                               "RiderList": {}}
        for riderNum in team['r']:
            teamList[team['n']]['RiderList'][riderNum] = riderList[riderNum]

    # pprint(riderList, indent=2)
    # pprint(teamList, indent=2)

    droppedList = requests.get('http://www.letour.fr/useradgents/2014/json/withdrawals.json').json()
    # print("Riders who dropped")
    for stage in droppedList:
        # print("Stage {0}".format(int(stage[u's'][0:2])))
        for rider in stage[u'w']:
            # print("\t{0}".format(riderList[rider['r']]['Name']))
            riderList[rider[u'r']]['Dropped'] = True

    if currentRiders:
        currentRiderList = {}
        for riderNum, riderDetails in riderList.items():
            if not riderDetails['Dropped']:
                currentRiderList[riderNum] = riderDetails

        return currentRiderList
    else:
        return riderList

if __name__ == '__main__':
    pprint(AppState(True), indent=2)
