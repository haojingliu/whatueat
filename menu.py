# -*- coding: utf-8 -*-
from src.recipes import get_my_recipes
from random import randint
from collections import defaultdict
import json

def main():
    recipes = get_my_recipes()
    total_recipes = len(recipes)
    courses = 7
    res = []
    gridients = defaultdict(int)
    for i in range(courses):
        idx = randint(0, total_recipes - 1)
        print(idx)
        this_recipe, this_gridient = recipes[idx]
        res.append(this_recipe)
        for g, c in this_gridient.iteritems():
            gridients[g] += c
    print json.dumps([ _.decode('utf8') for _ in res])
    print '======== gridient ========='
    print gridients


main()