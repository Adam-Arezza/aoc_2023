# format of the maps
#[destination range start, source range start, range length]
# in seed-to-soil-map below
# 98,99 map to 50,51
# 50,...97 map to 52...99
# therefore, seed 55 would map to soil 57
# goal is to traverse through the map(s) to get to location#
# then pick the lowest location number

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
    maps = []
    for i in map:
        #print(src)
        #print(i)
        for m in map[i]:
            #print(m)
            if src >= m["source_start"] and src <= m["source_start"] + m["range"]-1:
                #print(f'Found {src} in {range(m["source_start"],m["source_start"]+ m["range"]-1)}')
                #print(f'Destination is {src} - {m["source_start"]} + {m["destination_start"]}')
                src = m["destination_start"] + src - m["source_start"] 
                maps.append(src)
                break
    #print(f'Seed: {seed}, maps: {maps}')
    return src


with open("inputs/day_5_example.txt", "r") as example:
    example = example.readlines()

with open("inputs/day_5.txt","r") as inputs:
    inputs = inputs.readlines()

mappings, seeds = parse_maps(example)
#print(seeds)
#print(mappings["soil_to_fertilizer"])

final_locations = []
for i in range(len(seeds)):
    final_locations.append((seeds[i], get_seed_location(seeds[i],mappings)))
print(final_locations)

mappers, initial_seeds = parse_maps(inputs)
seed_locations = []
for i in range(len(seeds)):
    #every second number is a range
    #so create a range of seeds based on the previous number as the start and the range
    #loop through all of the seeds and get each of their locations
    if i % 2 == 0 and i > 0:
        continue
    else:
        try:
            seed_range = range(seeds[i], seeds[i] + seeds[i+1])
            for seed 
        except Exception as e:
            print(e)
        #for seed in seed_range:
        #    seed_locations.append(seed, get_seed_location(seed, mappings))
    #seed_locations.append((initial_seeds[i], get_seed_location(initial_seeds[i],mappers)))
print(seed_locations)

#lowest_location_number = seed_locations[0][1]
#for seed,location in seed_locations:
#    if location < lowest_location_number:
#        lowest_location_number = location
#    print(f'initial seed: {seed} location: {location}')
#print(lowest_location_number)
