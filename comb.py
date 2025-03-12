"""
def generate_all(elements, N, K):
    if K == 0 or N == 0 or N < K: # Kombinacje K == 0: [[]], inne []
        return [[]]
    elements = elements[:N]
    result = []
    for i in range(N):
        # Permutacje
        rest = elements[:i] + elements[i + 1:]
        for p in generate_permutations(rest, len(rest)):
            result.append([elements[i]] + p)
        # Kombinacje
        rest = elements[i + 1:]
        for c in generate_combinations(rest, len(rest), K - 1):
            result.append([elements[i]] + c)
        # Multizbiory
        for m in generate_multisets(elements[i:], len(elements[i:]), K - 1):
            result.append([elements[i]] + m)
    return result
    
i = 1
for a in enumerate(generate_all(cities, N, K):
    print(f"{i}: {[city['name'] for city in a]}")
    i += 1
"""

"""
def load_cities(filename):
    cities = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()[1:]  # Czyta wszystkie linie z pliku, pomijając pierwszą (nagłówek)
        for line in lines:  # Iteruje przez każdą linię w pliku
            parts = line.split()  # Dzieli linię na części (oddzielone białymi znakami)
            city = {  # Tworzy słownik z informacjami o mieście
                "id": int(parts[0]),  #
                "name": parts[1],
                "population": int(parts[2]),
                "lat": float(parts[3]),
                "lon": float(parts[4])
            }
            cities.append(city)
    return cities
"""

"""
def shortest_tsp_route(cities, N):
    cities = cities[:N]
    best_route, min_distance = None, float('inf')  # Inicjalizuje zmienne do przechowywania najlepszej trasy i minimalnej odległości
    for perm in generate_permutations(cities, N):  # Iteruje przez wszystkie permutacje miast
        distance = 0  # Inicjalizuje zmienną do przechowywania całkowitej odległości trasy
        for i in range(len(perm) - 1):  # Iteruje przez miasta w permutacji
            distance += haversine(perm[i]['lat'], perm[i]['lon'], perm[i+1]['lat'], perm[i+1]['lon'])  # Dodaje odległość między kolejnymi miastami
        distance += haversine(perm[-1]['lat'], perm[-1]['lon'], perm[0]['lat'], perm[0]['lon'])  # Dodaje odległość powrotu do pierwszego miasta
        if distance < min_distance:  # Sprawdza, czy bieżąca trasa jest krótsza od dotychczasowej najlepszej
            min_distance = distance  # Aktualizuje minimalną odległość
            best_route = perm  # Aktualizuje najlepszą trasę
    return best_route, min_distance
    
best_route, min_distance = shortest_tsp_route(cities, N)  # Znajduje najkrótszą trasę TSP dla N miast
print("Najkrótsza trasa:", [city["name"] for city in best_route])  # Wyświetla nazwy miast w najkrótszej trasie
print("Długość trasy:", min_distance, "km")  # Wyświetla długość najkrótszej trasy
"""

"""
def closest_population_subset(cities, N):
    cities = cities[:N]  # Ogranicza listę miast do pierwszych N miast
    total_population = sum(city['population'] for city in cities)  # Oblicza całkowitą populację N miast
    target = total_population / 2  # Oblicza docelową populację (50% całkowitej populacji)
    best_subset, best_diff = None, float('inf')  # Inicjalizuje zmienne do przechowywania najlepszego podzbioru i najmniejszej różnicy
    for r in range(1, len(cities) + 1):  # Iteruje przez możliwe rozmiary podzbiorów
        for subset in generate_combinations(cities, N, r):  # Iteruje przez wszystkie kombinacje miast o danym rozmiarze
            subset_population = sum(city['population'] for city in subset)  # Oblicza populację bieżącego podzbioru
            diff = abs(subset_population - target)  # Oblicza różnicę między populacją podzbioru a docelową populacją
            if diff < best_diff:  # Sprawdza, czy bieżąca różnica jest mniejsza od dotychczasowej najlepszej
                best_diff, best_subset = diff, subset  # Aktualizuje najlepszą różnicę i podzbiór
    return best_subset
    
best_subset = closest_population_subset(italy_cities, N)  # Znajduje podzbiór miast z populacją najbliższą 50%
print("Najlepszy podzbiór:", [city["name"] for city in best_subset])  # Wyświetla nazwy miast w najlepszym podzbiorze
"""
