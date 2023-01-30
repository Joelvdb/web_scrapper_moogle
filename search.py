from basic_url_functions import *


def separate_query_to_words_list(query):
    return query.split()


def get_calculated_score(page_score, word_score):
    return page_score * word_score


def sort_dict(dict):
    new_dict = {}
    for dict_key in sorted(dict, key=dict.get, reverse=True):
        new_dict[dict_key] = dict[dict_key]
    return new_dict


def check_if_words_in_page(page_name, words_dict, words):
    check = True

    for word in words:
        if word not in words_dict:
            return False
        if page_name not in words_dict[word]:
            check = False
    return check


def get_first_pages_with_words(words, words_dict, sorted_ranking_dict, max_results):
    first_pages = []
    names_list = list(sorted_ranking_dict.keys())
    for i in names_list:
        if len(first_pages) == max_results:
            return first_pages
        if check_if_words_in_page(i, words_dict, words):
            first_pages.append(i)
    return first_pages


def get_page_score(ranking_dict, page_name):
    return ranking_dict[page_name]


def nice_print_page_score(sorted_score):
    name_list = sorted_score.keys()
    for name in name_list:
        print(name + ' ' + str(sorted_score[name]))


def get_minimum_count(words_dict, page, words_list):
    minimum = words_dict[words_list[0]][page]
    for word in words_list:
        word_count = words_dict[word][page]
        if word_count < minimum:
            minimum = word_count
        else:
            continue
    return minimum


def sum_score(ranking_dict, words_dict, words_list, first_pages):
    word_score = {}
    for page in first_pages:
        page_score = ranking_dict[page]
        word_count = get_minimum_count(words_dict, page, words_list)
        sum = get_calculated_score(page_score, word_count)
        word_score[page] = sum
    sorted_score = sort_dict(word_score)
    nice_print_page_score(sorted_score)


def rank_results(max_results, ranking_dict_file, words_dict_file, query):
    query_list = separate_query_to_words_list(query)
    ranking_dict = get_pickle(ranking_dict_file)
    words_dict = get_pickle(words_dict_file)
    sorted_ranking_dict = sort_dict(ranking_dict)
    first_pages_with_words = get_first_pages_with_words(query_list, words_dict, sorted_ranking_dict, max_results)
    while first_pages_with_words == [] and query_list != []:
        query_list.pop()
        first_pages_with_words = get_first_pages_with_words(query_list, words_dict, sorted_ranking_dict, max_results)

    sum_score(ranking_dict, words_dict, query_list, first_pages_with_words)
