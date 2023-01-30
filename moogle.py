import sys
import download_and_get_links as dl
import rank
import words_dict as wd
import search as se


def crawl(base_url: str, index_file: str, out_file: str):
    dl.main(out_file, base_url, index_file)


def page_rank(iterations: int, dict_file: str, out_file: str):
    rank.main(iterations, dict_file, out_file)  # fix index_file_thing


def words_dict(base_url: str, index_file: str, out_file: str):
    wd.set_words_dict_pickle(base_url, index_file, out_file)


def search(query: str, rank_dict_path: str, word_dict_path: str, max_results: int):
    se.rank_results(max_results, rank_dict_path, word_dict_path, query)


if __name__ == '__main__':
    if sys.argv[1] == 'crawl':
        base_url = sys.argv[2]
        INDEX_FILE = sys.argv[3]
        out_file = sys.argv[4]
        crawl(base_url, INDEX_FILE, out_file)
    if sys.argv[1] == 'page_rank':
        iterations = int(sys.argv[2])
        dict_file = sys.argv[3]
        out_file = sys.argv[4]
        page_rank(iterations, dict_file, out_file)
    if sys.argv[1] == 'words_dict':
        base_url = sys.argv[2]
        INDEX_FILE = sys.argv[3]
        out_file = sys.argv[4]
        words_dict(base_url, INDEX_FILE, out_file)
    if sys.argv[1] == 'search':
        query = sys.argv[2]
        ranking_dict_file = sys.argv[3]
        words_dict_file = sys.argv[4]
        max_results = int(sys.argv[5])
        search(query, ranking_dict_file, words_dict_file, max_results)
