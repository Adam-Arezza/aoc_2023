# format of the maps
#[destination range start, source range start, range length]
# in seed-to-soil-map below
# 98,99 map to 50,51
# 50,...97 map to 52...99
# therefore, seed 55 would map to soil 57
# goal is to traverse through the map(s) to get to location#
# then pick the lowest location number
import math

def parse_maps(maps):
    seeds = []
    current_map = ""
    mapping = {}
    for i in range(len(maps)):
        map = maps[i].split("\n")
        if map[-1] == "":
            map.pop()
        map = map[0].split()
        if len(map) > 0 and not map[-1].isdigit():
            map.pop()
            current_map = map[0].replace("-","_")
            if len(current_map) > 0:
                mapping[current_map] = []
        else:
            if len(map) > 3:
                for j in map:
                    if j.isdigit():
                        seeds.append(int(j))
            else:
                try:
                    mapper = {}
                    for i in range(len(map)):
                        if i == 0:
                            mapper["destination_start"] = int(map[i])
                        if i == 1:
                            mapper["source_start"] = int(map[i])
                        if i == 2:
                            mapper["range"] = int(map[i])
                    if len(mapper.keys()) > 0:
                        mapping[current_map].append(mapper)
                except Exception as e:
                    print(e)
    return mapping,seeds


def get_seed_location(seed,map):
    src = seed
    for i in map:
        for m in map[i]:
            if src >= m["source_start"] and src <= m["source_start"] + m["range"]-1:
                src = m["destination_start"] + src - m["source_start"] 
                break
    return src


with open("inputs/day_5_example.txt", "r") as example:
    example = example.readlines()

with open("inputs/day_5.txt","r") as inputs:
    inputs = inputs.readlines()

mappings, seeds = parse_maps(example)

#final_locations = []
#for i in range(len(seeds)):
#    final_locations.append((seeds[i], get_seed_location(seeds[i],mappings)))

lowest = math.inf
for i in range(0,len(seeds),2):
    try:
        seed_range = range(seeds[i], seeds[i+1] + seeds[i])
        for seed in seed_range:
            location = get_seed_location(seed,mappings)
            if location < lowest:
                lowest = location
    except Exception as e:
        print(e)
print(lowest)
