import random
import bisect
import itertools


def tournament(tournament_size):
    def tournament_selector(population, num_parents):
        for _ in range(num_parents):
            yield max(random.sample(population, tournament_size))
    return tournament_selector


def _accumulate_scores(population):
    scores = list(itertools.accumulate(member.score for member in population))
    return scores, scores[-1]


def roulette(population, num_parents):
    #Uses code taken from
    #http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice

    cumulative_scores, total = _accumulate_scores(population)

    for _ in range(num_parents):
        rand = random.random() * total
        yield population[bisect.bisect(cumulative_scores, rand)]


def stochastic(population, num_parents):
    cumulative_scores, total = _accumulate_scores(population)
    average = total / num_parents

    rand = random.random() * average

    for float_index, in itertools.islice(itertools.count(rand, average), num_parents):
        yield population[bisect.bisect(cumulative_scores, float_index)]
