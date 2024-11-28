# From: https://github.com/wkaczurba/utils

import re

fname1="depTree1"
fname2="depTree2"

def load_dependencies_from_deptree(fname : str):
    f = open(fname, 'r')    
    deps = {}

    for line in f.readlines():
        removed_prefix=re.sub(r'^.* ', '', line)
        removed_nl=re.sub(r'\n', '', removed_prefix)

        l = removed_nl.split(":")
        dependency = {
            'group' : l[0],
            'artifact' : l[1],
            'type' : l[2],
            'version' : l[3]
            #'compile' : l[4]
        }

        key = f"{dependency['group']}:{dependency['artifact']}"
        if key in deps.keys():
            deps[key].append(dependency)
        else:
            deps[key] = [ dependency ]

    # Check duplicates:
    no_duplicates_found = True
    for key in deps.keys():
        l = deps[key]
        if len(l) > 1:
            print(f"Error: {deps[key]} contain multiple versions")
            no_duplicates_found = False
            break

    if no_duplicates_found:
        print("No duplicates found")
    return deps

deps1 = load_dependencies_from_deptree('depTree1')
deps2 = load_dependencies_from_deptree('depTree2')

def intersection_as_list(l1, l2):
    inter = [key1 for key1 in l1 if key1 in l2]
    return inter

def common_set(d1 : dict, d2 : dict):
    all_keys_set = set(list(d1.keys()) + list(d2.keys()))
    return all_keys_set

def compare(d1 : dict, d2 : dict):
    cs = common_set(d1, d2)
    result = {}
    for k in cs:
        left = d1.get(k)
        right = d2.get(k)
        result[k] = {
            'left': left,
            'right': right
        }
    return result
        

#len1 = len(deps1.keys())
#len2 = len(deps2.keys())
#print (f"deps1 len= {len1}")
#print (f"deps2 len= {len2}")

#ins1 = len(intersection_as_list(deps1, deps2))
#print (f"ins1 len= {ins1}")

# Common set:
cs=common_set(deps1, deps2)
#print (f"Commons set: {cs}")

compare_results = compare(deps1, deps2)
for dependency in compare_results.keys():
    l = compare_results[dependency]['left']
    if l:
        l = l[0]['version']
    else:
        l = '-'

    r = compare_results[dependency]['right']
    if r:
        r = r[0]['version']
    else:
        r = '-'
        
    print(f'{dependency}\t{l}\t{r}')
