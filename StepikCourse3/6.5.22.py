from collections import defaultdict


def wins(pairs):
    winner_loser = defaultdict(set)

    for winner, loser in pairs:
        winner_loser[winner].add(loser)

    return winner_loser
