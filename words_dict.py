from collections import Counter, defaultdict
from basic_url_functions import *
import bs4


def get_all_words_from_text(text):
    """
    :param text: text - string
    :return: return list of words
    """
    new_text = text.rstrip()
    words = new_text.split()
    words.sort()
    return words


def count_from_sorted_list(sorted_list):
    """
    :param sorted_list: sorted words list
    :return: return the count of first word and new list without the first word
    """
    count = 1
    i = 0
    if not len(sorted_list) <= 1:
        while sorted_list[i] == sorted_list[i + 1]:
            count += 1
            i += 1
            if i == len(sorted_list):
                break
    return count, sorted_list[count:]


def count_words_from_list(words_list, name):
    """
    :param words_list: words list
    :param name: name from index_file
    :return:
    """
    start = 0
    dict_count = {}
    cut_words_list = words_list[start:]

    while len(cut_words_list) > 0:
        dict_count[name], new_list = count_from_sorted_list(cut_words_list)
        cut_words_list = new_list

    return dict_count


def get_text_from_all_paragraph(html):
    """
    :param html: html text
    :return: the text from paragraphs
    """
    txt = ''
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all('p'):
        content = p.text
        txt += ' '
        txt += content
    return txt


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


def remove_duplicates(mylist):
    mylist = list(dict.fromkeys(mylist))
    return mylist


def get_words_dict(html_dict, names_list):
    words_dict = defaultdict(dict)
    for name in names_list:
        html = html_dict[name]
        paragraphs = get_text_from_all_paragraph(html)
        all_words = get_all_words_from_text(paragraphs)  # sorted
        counted = Counter(all_words)
        for word in all_words:
            words_dict[r"{}".format(word)][name] = counted[r"{}".format(word)]
    return words_dict


def set_words_dict_pickle(base_url, index, out_file):
    names_list = get_list_of_main_names(index)
    html_dict = get_dict_of_html(base_url, names_list)
    dict = get_words_dict(html_dict, names_list)
    set_pickle(dict, out_file)
