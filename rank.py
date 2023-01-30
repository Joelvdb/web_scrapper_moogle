import copy
from basic_url_functions import *


def sum_of_points(dict, name_list):
    """
    :param dict: the count_dict[name]
    :param name_list: relative links names
    :return: 
    """
    sum = 0
    for name in name_list:
        if name in dict:
            sum += dict[name]
    return sum


def get_point(dict, name):
    if name in dict:
        return dict[name]
    return 0


def set_r_dict(name_list, iterations, dict):
    """
    :param name_list: name list of relative links
    :param iterations: number of iterations
    :param dict: dict of count
    :return:
    """
    r = {}
    new_r = {}
    for name in name_list:
        r[name] = 1
        new_r[name] = 0

    for i in range(iterations):
        for name1 in name_list:
            for name2 in name_list:
                if sum_of_points(dict[name1], name_list) > 0:
                    new_r[name2] += r[name1] * (get_point(dict[name1], name2) / sum_of_points(dict[name1], name_list))

        r = copy.deepcopy(new_r)
        for name in name_list:
            new_r[name] = 0
    return r


def set_pickle_rank(name_list, iterations, dict, out_file):
    file = open(out_file, "wb")
    pickle.dump(set_r_dict(name_list, iterations, get_pickle(dict)), file)
    file.close()


def main(iterations, dict, out_file):
    set_pickle_rank(get_pickle(dict).keys(), iterations, dict, out_file)
