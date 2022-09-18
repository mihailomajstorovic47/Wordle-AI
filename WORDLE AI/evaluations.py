
def wordle_evaluate(row):
    evaluation = []
    for tile in row:
        if 'absent' in tile.get_attribute("data-state"):
            evaluation.append(0)
        elif 'present' in tile.get_attribute("data-state"):
            evaluation.append(1)
        elif 'correct' in tile.get_attribute("data-state"):
            evaluation.append(2)
    return tuple(evaluation)


def wordmaster_evaluate(row):
    evaluation = []
    for tile in row:
        if 'nm-inset-n-green' in tile.get_attribute("class"):
            evaluation.append(2)
        elif 'nm-inset-yellow-500' in tile.get_attribute("class"):
            evaluation.append(1)
        elif 'nm-inset-n-gray' in tile.get_attribute("class"):
            evaluation.append(0)
    return tuple(evaluation)


def get_evaluation(answer, word):
    output = [0, 0, 0, 0, 0]

    for i in range(5):
        if word[i] == answer[i]:
            output[i] = 2
            answer = answer[:i] + ' ' + answer[i + 1:]
    for i in range(5):
        char = word[i]
        if char in answer and output[i] == 0:
            output[i] = 1
            first_occurence = answer.find(char)
            answer = answer[:first_occurence] + ' ' + answer[first_occurence + 1:]
    return tuple(output)