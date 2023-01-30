import bs4
from basic_url_functions import *


def set_count_zero(names_list):
    """

    :param names_list:all the pages names
    :return: a dict[name1][name2]=0
    """
    dict = {}
    for link_master in names_list:
        dict[link_master] = {}
        for link_count in names_list:
            dict[link_master][link_count] = 0
    return dict


def count_number_of_links(html, relative):
    """
    :param html: html text
    :param relative: the relative link
    :return: the numbers of relative link in html
    """
    count = 0
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            if target == relative:
                count += 1
    return count


def count(names_list, html_dict):
    """
    :param base: base_url
    :param index_file: index name of txt file of relative links
    :return: dict of counted links in each link
    """
    traffic_dict_counted = set_count_zero(names_list)
    for name1 in names_list:
        for name2 in names_list:
            count_number = count_number_of_links(html_dict[name1], name2)
            if count_number > 0:
                traffic_dict_counted[name1][name2] = count_number
            else:
                traffic_dict_counted[name1].pop(name2)
        if traffic_dict_counted[name1] == None:
            traffic_dict_counted.pop(name1)
    return traffic_dict_counted


def set_pickle_dict(out_file, names_list, html_dict):
    count1 = count(names_list, html_dict)
    filehandler = open(out_file, "wb")
    pickle.dump(count1, filehandler)
    filehandler.close()


def main(out_file, base_url, index_file):
    names_list = get_list_of_main_names(index_file)
    html_dict = get_dict_of_html(base_url, names_list)
    set_pickle(count(names_list, html_dict), out_file)
