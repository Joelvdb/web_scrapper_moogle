import urllib.parse, requests, pickle


def get_html_from_page(page_url):
    """
    :param page_url: page_url
    :return: the html text
    """
    response = requests.get(page_url)
    html = response.text
    return html


def join_full_url(base, relative):
    full_url = urllib.parse.urljoin(base, relative)
    return full_url


def get_list_of_main_names(index_file):
    """
    :param index_file: index name of txt file of relative links
    :return: list of all relative names
    """
    names_list = []
    with open(index_file) as f:
        for line in f:
            names_list.append(line.rstrip())
    return names_list


def set_pickle(dict, out_file):
    filehandler = open(out_file, "wb")
    pickle.dump(dict, filehandler)
    filehandler.close()


def get_dict_of_html(base, names_list):
    """
    :param base: base_url
    :param index_file: index name of txt file of relative links
    :return:
    """
    dict = {}
    for name in names_list:
        dict[name] = get_html_from_page(join_full_url(base, name))
    return dict


def get_pickle(filename):
    """
    :param filename: file name of dict.pickle
    :return: saved counted links dict
    """
    filehandler = open(filename, 'rb')

    with filehandler as handle:
        dict = pickle.load(handle)
    filehandler.close()
    return dict
