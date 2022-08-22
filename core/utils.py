from . import constants


def get_cities_states():
    cities = []
    states = []
    for state in constants.STATE_MAP:
        for city in constants.STATE_MAP[state]:
            cities.append((city, city))
        states.append((state, state))
    return cities, states
