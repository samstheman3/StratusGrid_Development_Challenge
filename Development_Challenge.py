#!/usr/bin/env python
from typing import Type
import requests
import json
import time
import sys

def GetUserInput(prompt):
    while (True):
        try:
            userInput = int(input(prompt))
            if (userInput < 0):
                print('Please Enter in a Positive Value')
                continue
            break
        except ValueError:
            print('Please Enter in a Valid Number')
            continue
    return userInput
    
def GetResponseBody(URL):
    response = requests.get(URL)
    parsedResponse = json.loads(response.text)
    return parsedResponse

def GetAverageHeightandWeightForAllPokemonAndPokemonType(JSON):
    totalWeight = 0
    totalHeight = 0
    iterator = 0
    TypeDic = {
                'Height':{'bug':0, 'dark':0, 'dragon':0, 'electric':0, 'fairy':0, 'fighting':0, 'fire':0, 'flying':0, 'ghost':0, 'grass':0, 'ground':0, 'ice':0, 'normal':0, 'poison':0, 'psychic':0, 'rock':0, 'steel':0, 'water':0},
                'Weight':{'bug':0, 'dark':0, 'dragon':0, 'electric':0, 'fairy':0, 'fighting':0, 'fire':0, 'flying':0, 'ghost':0, 'grass':0, 'ground':0, 'ice':0, 'normal':0, 'poison':0, 'psychic':0, 'rock':0, 'steel':0, 'water':0},
                'Total': {'bug':0, 'dark':0, 'dragon':0, 'electric':0, 'fairy':0, 'fighting':0, 'fire':0, 'flying':0, 'ghost':0, 'grass':0, 'ground':0, 'ice':0, 'normal':0, 'poison':0, 'psychic':0, 'rock':0, 'steel':0, 'water':0}
                }

    results = JSON['results']

    for pokemon in results:
        #Code to get pokemon information
        individualURL = pokemon['url']
        response = requests.get(individualURL)
        parsedResponse = json.loads(response.text)

        #Code for all pokemon
        totalHeight += parsedResponse['height']
        totalWeight += parsedResponse['weight']
        iterator += 1

        #Code for pokemon type
        weight = parsedResponse['weight']
        height = parsedResponse['height']
        types = parsedResponse['types']
        for item in types:
            type = item['type']
            name = type['name']
            TypeDic['Weight'][name] += weight
            TypeDic['Height'][name] += height
            TypeDic['Total'][name] += 1

    #Code for all pokemon
    averageHeight = totalHeight / iterator
    averageWeight = totalWeight / iterator

    #Code for pokemon type
    for measure in TypeDic:
        if measure == 'Weight' or measure == 'Height':
            for element in TypeDic[measure]:
                if TypeDic[measure][element] > 0:
                    TypeDic[measure][element] = TypeDic[measure][element] / TypeDic['Total'][element]
        else:
            break

    averages = [averageHeight, averageWeight, TypeDic]
    return averages

def main():
    startTime = time.time()

    prompt = 'Please Enter in a Limit: '
    limit = GetUserInput(prompt)

    prompt = 'Please Enter in an Offset: '
    offset = GetUserInput(prompt)

    URL = 'https://pokeapi.co/api/v2/pokemon?limit=' + str(limit) + '&offset=' + str(offset)
    JSON = GetResponseBody(URL)

    averages = GetAverageHeightandWeightForAllPokemonAndPokemonType(JSON)

    print('The Average Height of all Pokemon: ' + str(averages[0]))
    print('The Average Weight of all Pokemon: ' + str(averages[1]))

    averagesForPokemonTypes = averages[2]

    for measure in averagesForPokemonTypes:
        if measure == 'Weight' or measure == 'Height':
            print('Average ' + measure +  ' of types: ')
            for types in averagesForPokemonTypes[measure]:
                print(' ' + str(types) + ': ' + str(averagesForPokemonTypes[measure][types]))
        else:
            break

    executionTime = (time.time() - startTime)
    print('The Excecution Time of the Project in Seconds: ' + str(executionTime))

    input('Press the enter key to continue...')

    sys.exit

if __name__ == "__main__":
    main()







