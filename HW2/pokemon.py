#CS210 Assignment 2
# Aatif Sayed & Umar Khattak

import csv

# Task 1.1
def task_1_1(file) :
    with open(file) as pokemonFile :
        reader = csv.reader(pokemonFile)
        next(reader)  # skip header line
        fire_count = 0
        fire_40_count = 0
        for line in reader :
            if line[4] == 'fire' :
                fire_count = fire_count + 1
                if float(line[2]) >= 40 :
                    fire_40_count = fire_40_count + 1
    percentage = round((fire_40_count / fire_count) * 100)
    result = 'Percentage of fire type Pokemons at or above level 40 = ' + str(percentage)
    resultFile = open('pokemon1.txt', 'w')
    resultFile.write(result)
    resultFile.close()

    
# Tasks 1.2 and 1.3
def tasks_1_2_and_1_3(file) :
#   Task 1.2 begins here  
    with open(file) as pokemonFile :
        reader = csv.reader(pokemonFile)
        next(reader)  # skip header line
        pokemon_dict = {}
        for line in reader :
            if line[4] == 'NaN' :
                continue
            if not (line[5] in pokemon_dict.keys()) :
                pokemon_dict[line[5]] = [line[4]]
            else :
                pokemon_dict[line[5]].append(line[4])
    for k,v in pokemon_dict.items() :
        occurrences = {}
        for _type in v :
            if _type in occurrences :
                occurrences[_type] += 1
            else :
                occurrences[_type] = 1
        max_val = max(list(occurrences.values()))
        indices = [index for index, val in enumerate(list(occurrences.values())) if val == max_val]
     #  choose type by sorting tied items alphabetically and choosing whichever occurs first
        if len(indices) != 1 :
            list_to_sort = []
            for index in indices :
                list_to_sort.append(v[index])
            list_to_sort.sort()
            pokemon_dict.update({k:list_to_sort[0]})
     #  choose type by finding most frequently appearing type for that specific weakness
        else :
            pokemon_dict.update({k:v[indices[0]]})

#   Task 1.3 begins here  
    atk_above_40_total = 0
    atk_above_40_count = 0
    atk_below_40_total = 0
    atk_below_40_count = 0
    def_above_40_total = 0
    def_above_40_count = 0
    def_below_40_total = 0
    def_below_40_count = 0
    hp_above_40_total = 0
    hp_above_40_count = 0
    hp_below_40_total = 0
    hp_below_40_count = 0
    
    with open(file) as pokemonFile :
        reader = csv.reader(pokemonFile)
        next(reader)  # skip header line
        for line in reader :
            if line[6] == 'NaN' :
                pass
            else :
                if float(line[2]) > 40 :
                    atk_above_40_total += float(line[6])
                    atk_above_40_count += 1
                else :
                    atk_below_40_total += float(line[6])
                    atk_below_40_count += 1
            if line[7] == 'NaN' :
                pass
            else :
                if float(line[2]) > 40 :
                    def_above_40_total += float(line[7])
                    def_above_40_count += 1
                else :
                    def_below_40_total += float(line[7])
                    def_below_40_count += 1
            if line[8] == 'NaN' :
                pass
            else :
                if float(line[2]) > 40 :
                    hp_above_40_total += float(line[8])
                    hp_above_40_count += 1
                else :
                    hp_below_40_total += float(line[8])
                    hp_below_40_count += 1
    atk_above_40_average = round(atk_above_40_total / atk_above_40_count, 1)
    atk_below_40_average = round(atk_below_40_total / atk_above_40_count, 1)
    def_above_40_average = round(def_above_40_total / def_above_40_count, 1)
    def_below_40_average = round(def_below_40_total / def_above_40_count, 1)
    hp_above_40_average = round(hp_above_40_total / hp_above_40_count, 1)
    hp_below_40_average = round(hp_below_40_total / hp_above_40_count, 1)

    with open(file) as pokemonFile :
        reader = csv.reader(pokemonFile)
        resultFile = open('pokemonResult.csv', 'w', newline = '')
        writer = csv.writer(resultFile)
        for line in reader :
            if line[4] == 'NaN' :
                line[4] = pokemon_dict.get(line[5])
            if line[6] == 'NaN' :
                if float(line[2]) > 40 :
                    line[6] = atk_above_40_average
                else :
                    line[6] = atk_below_40_average
            if line[7] == 'NaN' :
                if float(line[2]) > 40 :
                    line[7] = def_above_40_average
                else :
                    line[7] = def_below_40_average
            if line[8] == 'NaN' :
                if float(line[2]) > 40 :
                    line[8] = hp_above_40_average
                else :
                    line[8] = hp_below_40_average
            writer.writerow(line)
        resultFile.close()

# Task 1.4
def task_1_4(file):
    with open(file) as pokemonFile :
        reader = csv.reader(pokemonFile)
        next(reader)  # skip header line
        type_to_personality_dict = {}
        for line in reader :
            if not (line[4] in type_to_personality_dict.keys()) :
                type_to_personality_dict[line[4]] = [line[3]]
            else :
                if line[3] in type_to_personality_dict.get(line[4]) :
                    continue
                else :
                    type_to_personality_dict[line[4]].append(line[3])
    result = 'Pokemon type to personality mapping:\n\n'
    for k,v in type_to_personality_dict.items() :
        result += '   ' + k + ': '
        for personality in v :
            if personality == v[-1] :
                result += personality + '\n'
            else :
                result += personality + ', '
    resultFile = open('pokemon4.txt', 'w')
    resultFile.write(result)
    resultFile.close()
   
# Task 1.5
def task_1_5(file):
    with open(file) as pokemonFile :
        reader = csv.reader(pokemonFile)
        next(reader)  # skip header line
        hp_count = 0
        total = 0
        for line in reader:
            if line[9] == '3.0':
                hp_count = hp_count + 1
                total = total + float(line[8])
            else:
                continue
        average = round((total / hp_count))
        result = 'Average hit point for Pokemons of stage 3.0 = ' + str(average)
        resultFile = open('pokemon5.txt', 'w')
        resultFile.write(result)
        resultFile.close()
        
task_1_1('pokemonTrain.csv')
tasks_1_2_and_1_3('pokemonTrain.csv')
task_1_4('pokemonResult.csv')
task_1_5('pokemonResult.csv')