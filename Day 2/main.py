import itertools

move_scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

rps_scores = {
    'AA': 3,
    'AB': 0,
    'AC': 6,
    'BA': 6,
    'BB': 3,
    'BC': 0,
    'CA': 0,
    'CB': 6,
    'CC': 3,
}

if __name__ == '__main__':
    lines = open('input.txt', encoding='utf-8').readlines()
    strategy = [line.strip().split() for line in lines]

    score = 0
    for play_1, play_2 in strategy:
        play_2 = {
            'X': 'A',
            'Y': 'B',
            'Z': 'C',
        }[play_2]
        round_score = rps_scores[play_2 + play_1]
        round_score += move_scores[play_2]
        score += round_score
    print('Answer one:', score)

    matching_move = {
        'AX': 'C',
        'AY': 'A',
        'AZ': 'B',
        'BX': 'A',
        'BY': 'B',
        'BZ': 'C',
        'CX': 'B',
        'CY': 'C',
        'CZ': 'A',
    }
    score = 0
    for play_1, result in strategy:
        round_score = {
            'X': 0,
            'Y': 3,
            'Z': 6,
        }[result]
        round_score += move_scores[matching_move[play_1 + result]]
        score += round_score
    print('Answer two:', score)
