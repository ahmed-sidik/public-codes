"""
def all(elements, N):
    if K == 0 or N == 0: # combinations: N < K, N == 0: []
	return [[]]
    elements = elements[:N]
    generated = []
    for i in range(N):
	# permutations
        rest = elements[:i] + elements[i+1:]
        for a in permutations(rest, len(rest)):
	# combinations
	rest = elements[i+1:]
        for a in combinations(rest, len(rest), K-1):
	# multisets
	rest = elements[i:]
        for a in multisets(rest, len(rest), K-1):
            generated.append([elements[i]] + a)
    return generated
"""

import math

def load_cities(filename):
    cities = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()[1:]
        for line in lines:
            parts = line.split()
            city = {
                "id": int(parts[0]),  #
                "name": parts[1],
                "population": int(parts[2]),
                "latitude": float(parts[3]),
                "longitude": float(parts[4])
            }
            cities.append(city)
    return cities

def permutations(elements, N):
    if N == 0:
        return [[]]
    elements = elements[:N]
    generated = []
    for i in range(N):
        rest = elements[:i] + elements[i+1:]
        for p in permutations(rest, len(rest)):
            generated.append([elements[i]] + p)
    return generated

def combinations(elements, N, K):
    if K == 0:
        return [[]]
    if N < K or N == 0:
        return []
    elements = elements[:N]
    generated = []
    for i in range(N):
        rest = elements[i+1:]
        for c in combinations(rest, len(rest), K-1):
            generated.append([elements[i]] + c)
    return generated

def multisets(elements, N, K):
    if K == 0 or N == 0:
        return [[]]
    elements = elements[:N]
    generated = []
    for i in range(N):
        rest = elements[i:]
        for m in multisets(rest, len(rest), K-1):
            generated.append([elements[i]] + m)
    return generated

def radians(deg):
    return deg * math.pi / 180

def haversine(latitude1, longitude1, latitude2, longitude2):
    phi1, phi2 = radians(latitude1), radians(latitude2)
    diff_phi = radians(latitude2 - latitude1)
    diff_lambda = radians(longitude2 - longitude1)
    alfa = (math.sin(diff_phi/2))**2 + math.cos(phi1) * math.cos(phi2) * (math.sin(diff_lambda/2))**2
    return 2 * 6371 * math.asin(math.sqrt(alfa))

def shortest_route(cities, N):
    cities = cities[:N]
    best_route, min_distance = None, float('inf')
    for p in permutations(cities, N):
        distance = 0
        for i in range(len(p) - 1):
            distance += haversine(p[i]['latitude'], p[i]['longitude'], p[i+1]['latitude'], p[i+1]['longitude'])
        distance += haversine(p[-1]['latitude'], p[-1]['longitude'], p[0]['latitude'], p[0]['longitude'])
        if distance < min_distance:
            min_distance = distance
            best_route = p
    return best_route, min_distance

def closest_population_comb(cities, N):
    cities = cities[:N]
    total_population = sum(city['population'] for city in cities)
    target = total_population / 2
    best_c, best_diff = None, float('inf')
    for r in range(1, len(cities) + 1):
        for c in combinations(cities, N, r):
            c_population = sum(city['population'] for city in c)
            diff = abs(c_population - target)
            if diff < best_diff:
                best_diff, best_c = diff, c
    return best_c

cities = load_cities("France.txt")
N, M = 3, 2

i = 1
# 1) Dla podanej liczby N wypisać ponumerowane wszystkie porządki odwiedzin N miast 1,2,...,N
for p in permutations(cities, N):
    city_names = [city['name'] for city in p]
    print(i, city_names)
    i += 1
print("")

# Dla podanych liczb N i M wypisać ponumerowane wszystkie porządki odwiedzin M z N miast 1,2,...,N
# Dla podanych liczb N i K <= N wypisać ponumerowane wszystkie podzbiory K z N miast 1,2,...,N
i = 1
for c in combinations(cities, N, M):
    city_names = [city['name'] for city in c]
    print(i, city_names)
    i += 1
print("")

# Dla podanych liczb N i M wypisać ponumerowane wszystkie podzbiory, z możliwymi powtórzeniami, M z N miast 1,2,...,N
i = 1
for m in multisets(cities, N, M):
    city_names = [city['name'] for city in m]
    print(i, city_names)
    i += 1
print("")

# Korzystając z informacji o współrzędnych x i y miast, podać przebieg i długość najkrótszej trasy-cyklu odwiedzin miast.
route, distance = shortest_route(cities, N)
print("Najkrótsza trasa:", [city["name"] for city in route])
print("Długość trasy:", distance, "km")
print("")

# Korzystając z informacji o liczbie ludności miast, podać podzbiór, dla którego sumaryczna liczba mieszkańców jest najbliższa 50% liczby mieszkańców (bez powtórzeń) N miast.
best_comb = closest_population_comb(cities, N)
print("Najlepszy podzbiór:", [city["name"] for city in best_comb])

