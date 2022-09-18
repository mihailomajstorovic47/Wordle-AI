def get_wordle_guesses_list():
    word_list = []
    with open("wordle_guesses.txt", "r") as file:
        for word in file:
            word_list.append(word.strip())
    return word_list


def get_wordle_answers_list():
    word_list = []
    with open("wordle_answers.txt", "r") as file:
        for word in file:
            word_list.append(word.strip())
    return word_list


def get_wordmaster_guesses_list():
    word_list = []
    with open("wordmaster_guesses.txt", "r") as file:
        for word in file:
            word_list.append(word.strip())
    return word_list


def get_wordmaster_answers_list():
    word_list = []
    with open("wordmaster_answers.txt", "r") as file:
        for word in file:
            word_list.append(word.strip())
    return word_list