#!usr/bin/python
import json
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import operator
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib
from matplotlib.pyplot import imread
import itertools


def Variance(scores, mean):
    sum = 0
    for i in scores:
        sum+=(i-mean)**2
    return ( sum/(len(scores)-1) )

def main():
    beer_data = open("data_2018.json").read()
    data = json.loads(beer_data)


    participantList = list(data.keys())
    beerNames = list(data.get(participantList[0]).keys())
    beerLists = []
    score = []
    beer_name = []
    myDict = {}
    means = {}
    controversy = {}

    for beer in beerNames:
        myDict[beer] = [[],[],[],[]]
        means[beer] = []
        controversy[beer]= []
        beer_name.append(beer)
    #print(beer_name)
    for name in participantList:

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
        controversy[beer].append(sqrt(Variance(myDict[beer][0], means[beer][0])))
        means[beer].append(sum(myDict[beer][1])/len(myDict[beer][1]))
        controversy[beer].append(sqrt(Variance(myDict[beer][1], means[beer][1])))
        means[beer].append(sum(myDict[beer][2])/len(myDict[beer][2]))
        controversy[beer].append(sqrt(Variance(myDict[beer][2], means[beer][2])))
        means[beer].append(sum(myDict[beer][3])/len(myDict[beer][3]))
        controversy[beer].append(sqrt(Variance(myDict[beer][3], means[beer][3])))
        means[beer].append(sum(means[beer])/len(means[beer]))

        controversy[beer].append(sum(controversy[beer])/len(controversy[beer]))
    def Extract(lst, i):
        return [item[i] for item in lst]

    #################################### OVERALL #################################
    sorted_means_overall = dict(zip(means.keys(),Extract(list(means.values()),4)))
    sorted_means_overall = sorted(sorted_means_overall.items(), key=operator.itemgetter(1))
    controversy_overall = dict(zip(controversy.keys(),Extract(list(controversy.values()),4)))
    controversy_overall = sorted(controversy_overall.items(), key=operator.itemgetter(1))

    #################################### XMAS FACTOR #############################
    sorted_means_xmas = dict(zip(means.keys(),Extract(list(means.values()),3)))
    sorted_means_xmas = sorted(sorted_means_xmas.items(), key=operator.itemgetter(1))
    controversy_xmas = dict(zip(controversy.keys(),Extract(list(controversy.values()),3)))
    controversy_xmas  = sorted(controversy_xmas .items(), key=operator.itemgetter(1))

    #################################### LABEL ###################################
    sorted_means_label = dict(zip(means.keys(),Extract(list(means.values()),2)))
    sorted_means_label = sorted(sorted_means_label.items(), key=operator.itemgetter(1))
    controversy_label = dict(zip(controversy.keys(),Extract(list(controversy.values()),2)))
    controversy_label  = sorted(controversy_label .items(), key=operator.itemgetter(1))

    #################################### TASTE ###################################
    sorted_means_taste = dict(zip(means.keys(),Extract(list(means.values()),0)))
    sorted_means_taste = sorted(sorted_means_taste.items(), key=operator.itemgetter(1))
    controversy_taste = dict(zip(controversy.keys(),Extract(list(controversy.values()),0)))
    controversy_taste  = sorted(controversy_taste .items(), key=operator.itemgetter(1))

    #################################### SMELL ###################################
    sorted_means_smell = dict(zip(means.keys(),Extract(list(means.values()),1)))
    sorted_means_smell = sorted(sorted_means_smell.items(), key=operator.itemgetter(1))
    controversy_smell = dict(zip(controversy.keys(),Extract(list(controversy.values()),1)))
    controversy_smell  = sorted(controversy_smell .items(), key=operator.itemgetter(1))




    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(sorted_means_taste[i][0], sorted_means_taste[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Taste Santa Hat score - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("Score [SH]")

    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(controversy_taste[i][0], controversy_taste[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Taste controversy - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("controversy")

    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(sorted_means_smell[i][0], sorted_means_smell[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Smell Santa Hat score - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("Score [SH]")

    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(controversy_smell[i][0], controversy_smell[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Smell controversy - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("controversy")

    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(sorted_means_label[i][0], sorted_means_label[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Label Santa Hat score - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("Score [SH]")

    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(controversy_label[i][0], controversy_label[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Label controversy - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("controversy")


    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(sorted_means_xmas[i][0], sorted_means_xmas[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Xmas-factor Santa Hat score - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("Score [SH]")


    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(controversy_xmas[i][0], controversy_xmas[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('X-mas factor controversy - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("controversy")

    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(sorted_means_overall[i][0], sorted_means_overall[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Overall Santa Hat score - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("Score [SH]")

    figure = plt.figure()
    for i, beer in enumerate(means):

        plt.bar(controversy_overall[i][0], controversy_overall[i][1])
        plt.xticks(rotation=20, ha="right", size = 4)

    plt.title('Overall controversy - christmas beers 2018')
    plt.xlabel("Beer")
    plt.ylabel("controversy")

    pdf = matplotlib.backends.backend_pdf.PdfPages("/mn/fys-server1/s3/andhegge/Desktop/Beer_tasting_2018_results.pdf")
    for fig in range(1, figure.number+1):
        pdf.savefig( fig )
    pdf.close()

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

    print('============\n', 'Controversy  Overall','\n============')
    for beer in controversy:
        print(beer, controversy[beer][4])

main()
