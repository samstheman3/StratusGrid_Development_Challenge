#!/usr/bin/env python
import unittest
from Development_Challenge import GetResponseBody
from Development_Challenge import GetAverageHeightandWeightForAllPokemonAndPokemonType

class DevelopmentChallengeTestCase(unittest.TestCase):
    def test_GetResponseBody(self):
        result = GetResponseBody('https://pokeapi.co/api/v2/pokemon?limit=2&offset=4')
        self.assertTrue(type(result) is dict)

    def test_GetAverageHeightandWeightForAllPokemonAndPokemonType(self):
        JSON = GetResponseBody('https://pokeapi.co/api/v2/pokemon?limit=2&offset=4')
        result = GetAverageHeightandWeightForAllPokemonAndPokemonType(JSON)
        self.assertTrue(type(result) is list and len(result) == 3)

if __name__ == '__main__':
    unittest.main()