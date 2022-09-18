import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
import numpy as np
from get_words_list import get_wordle_guesses_list, get_wordle_answers_list, get_wordmaster_guesses_list, get_wordmaster_answers_list
from evaluations import get_evaluation, wordle_evaluate, wordmaster_evaluate

def play(rows, guesses, answers, is_wordle):
    words = guesses
    narrowed_down_list = answers
    for guess_num in range(5):
        min_wordcount = 1000000
        chosen_word = ""
        evaluation_to_wordlist_map = {}
        if guess_num != 0:
            words_to_consider = words
        else:
            words_to_consider = ["roate"]
        for word_to_guess in words_to_consider:
            temp_eval_to_words_map = {}
            for possible_answer in narrowed_down_list:
                evaluation = get_evaluation(possible_answer, word_to_guess)
                if tuple(evaluation) not in temp_eval_to_words_map:
                    temp_eval_to_words_map[tuple(evaluation)] = [possible_answer]
                else:
                    temp_eval_to_words_map[tuple(evaluation)].append(possible_answer)
            biggest_possible_remaining_wordcount = max([len(val) for val in temp_eval_to_words_map.values()])
            if biggest_possible_remaining_wordcount < min_wordcount:
                min_wordcount = biggest_possible_remaining_wordcount
                chosen_word = word_to_guess
                evaluation_to_wordlist_map = temp_eval_to_words_map
        type(chosen_word)
        time.sleep(2)
        if is_wordle:
            answer_evaluation = wordle_evaluate(rows[guess_num])
        else:
            answer_evaluation = wordmaster_evaluate(rows[guess_num])
        if answer_evaluation in evaluation_to_wordlist_map:
            narrowed_down_list = evaluation_to_wordlist_map[answer_evaluation]
        if answer_evaluation == [2, 2, 2, 2, 2]:
            print(guess_num + 2)
            return [chosen_word]
        time.sleep(1)
        if len(narrowed_down_list) == 1:
            type(narrowed_down_list[0])
            print(guess_num + 2)
            return [chosen_word]

    return narrowed_down_list


def run():
    start_button = 'esc'
    browser = webdriver.Chrome(ChromeDriverManager().install())
    is_wordle = False

    if is_wordle:
        browser.get("https://www.nytimes.com/games/wordle/")
        keyboard.wait(start_button)
        rows = np.array(browser.find_elements(By.CLASS_NAME, 'Tile-module_tile__3ayIZ')).reshape(6, 5)
        play(rows, get_wordle_guesses_list(), get_wordle_answers_list(), is_wordle)
    else:
        browser.get("https://octokatherine.github.io/word-master/")
        keyboard.wait(start_button)
        rounds = 200
        for iter in range(rounds):
            rows = np.array(browser.find_elements(By.TAG_NAME, 'span')).reshape(6, 5)
            play(rows, get_wordmaster_guesses_list(), get_wordmaster_answers_list(), is_wordle)
            time.sleep(2)
            keyboard.press('esc')
            time.sleep(2)
            keyboard.release('esc')
            time.sleep(1)
            browser.find_element(By.XPATH, '//button[text()="Play Again"]').click()
            time.sleep(1)
    keyboard.wait(start_button)


def type(word):
    keyboard.write(word, delay=0.05)
    keyboard.press_and_release('enter')

