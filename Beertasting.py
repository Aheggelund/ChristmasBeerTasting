#!usr/bin/python
import json
import numpy as np
import math
import matplotlib.pyplot as plt
import operator

def main():
    beer_data = open("data_2018.json").read()
    data = json.loads(beer_data)


    participantList = list(data.keys())
    beerNames = list(data.get(participantList[0]).keys())
    beerLists = []

    myDict = {}
    means = {}
    controversy = {}

    for beer in beerNames:
        myDict[beer] = [[],[],[],[]]
        means[beer] = []
        controversy[beer]= []

    for name in participantList:
        #beers = data.get(participantList[name])
        #print('====================\n', participantList[name], '\n====================')
        #beerLists = list(beers.values())
        for beer in beerNames:
            if data[name][beer][0] > 0:
                myDict[beer][0].append(data[name][beer][0])
            if data[name][beer][1] > 0:
                myDict[beer][1].append(data[name][beer][1])
            if data[name][beer][2] > 0:
                myDict[beer][2].append(data[name][beer][2])
            if data[name][beer][3] > 0:
                myDict[beer][3].append(data[name][beer][3])


    for beer in myDict:

        means[beer].append(sum(myDict[beer][0])/len(myDict[beer][0]))
        controversy[beer].append((sum(means[beer][0])-(sum(myDict[beer][0])/len(myDict[beer][0])))**2)
        means[beer].append(sum(myDict[beer][1])/len(myDict[beer][1]))
        controversy[beer].append((sum(means[beer][1])-(sum(myDict[beer][1])/len(myDict[beer][1])))**2)
        means[beer].append(sum(myDict[beer][2])/len(myDict[beer][2]))
        controversy[beer].append((sum(means[beer][1])-(sum(myDict[beer][2])/len(myDict[beer][2])))**2)
        means[beer].append(sum(myDict[beer][3])/len(myDict[beer][3]))
        controversy[beer].append((sum(means[beer][1])-(sum(myDict[beer][3])/len(myDict[beer][3])))**2)
        means[beer].append(sum(means[beer])/len(means[beer]))
    #for beer in means:
        #means = sorted(means, key=itemgetter(beer))
    for beer in controversy:
        plt.plot(controversy[beer], label=str(beer))

    plt.legend()
    plt.show()
    print('============\n', 'Taste','\n============')
    for beer in means:
        print(beer, means[beer][0])
    print('============\n', 'Smell','\n============')
    for beer in means:
        print(beer, means[beer][1])
    print('============\n', 'Label','\n============')
    for beer in means:
        print(beer, means[beer][2])
    print('============\n', 'X-mas Factor','\n============')
    for beer in means:
        print(beer, means[beer][3])
    print('============\n', 'Overall','\n============')
    for beer in means:
        print(beer, means[beer][4])
    print('============\n', 'Controversy Taste','\n============')
    for beer in controversy:
        print(beer, controversy[beer][0])
    print('============\n', 'Controversy Smell','\n============')
    for beer in controversy:
        print(beer, controversy[beer][1])
    print('============\n', 'Controversy Label','\n============')
    for beer in controversy:
        print(beer, controversy[beer][2])
    print('============\n', 'Controversy Xmas factor','\n============')
    for beer in controversy:
        print(beer, controversy[beer][3])

main()
