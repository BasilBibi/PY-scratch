from abc import ABC, abstractmethod
import requests
import json
from jsonpath_ng import parse


class WordDictionary(ABC):
    @abstractmethod
    def lookup(self, word):
        return


class OxfordOnlineWordDictionary(WordDictionary):
    _app_id = '9286dd2e'
    _app_key = '8651b0907938b33bb76e99cb157288d2'
    _headers = {'app_id': _app_id, 'app_key': _app_key}
    _language = 'en'
    _base_url = f'https://od-api.oxforddictionaries.com:443/api/v1/entries/{_language}'
    _success = 200
    _word_not_found = 404

    __DEF_PATH = parse('$..definitions')
    __ETYM_PATH = parse('$..etymologies')

    def __init__(self, req=requests):
        self._req = req

    def lookup(self, word):
        url = f'{self._base_url}/{word.lower()}'
        r = self._req.get(url, headers=self._headers)

        if r.status_code == self._success:
            j = json.loads(r.text)
            return self._extract_results(j)
        elif r.status_code == self._word_not_found:
            return [f'Oxford Online Dictionary could not find {word}']
        else:
            return ['Oxford Online Dictionary did not respond']

    @staticmethod
    def _extract_results(lookup_result):
        definitions = OxfordOnlineWordDictionary._extract_definitions(lookup_result)
        etymologies = OxfordOnlineWordDictionary._extract_etymologies(lookup_result)
        return [f'{i+1} : {definition}'
                for i, definition in enumerate(etymologies + definitions)]

    @staticmethod
    def _extract_definitions(lookup_result):
        definition_matches = [match.value for match in
                              OxfordOnlineWordDictionary.__DEF_PATH.find(lookup_result)]
        return [match for match
                in OxfordOnlineWordDictionary._flatten_results(definition_matches)]

    @staticmethod
    def _extract_etymologies(lookup_result):
        etymology_matches = [match.value for match in OxfordOnlineWordDictionary.__ETYM_PATH.find(lookup_result)]
        return [match for match
                in OxfordOnlineWordDictionary._flatten_results(etymology_matches)]

    @staticmethod
    def _flatten_results(list_of_lists):
        return [item for sublist in list_of_lists for item in sublist]


class LocalWordDictionary(WordDictionary):
    def __init__(self, csv_file_path):
        self._internal_dict = LocalWordDictionary._make_internal_dict(csv_file_path)

    @staticmethod
    def _make_internal_dict(filename):

        def make_tuple(line):
            s = line.strip().split(',')
            return s[0], s[1]

        filepath = LocalWordDictionary._get_file_path(filename)
        with open(filepath, 'r') as fh:
            return dict([make_tuple(line) for line in fh.readlines()])

    @staticmethod
    def _get_file_path(filename):
        import os
        return os.path.join(os.path.dirname(__file__), filename)

    def lookup(self, word):
        try:
            return [f'1 : {self._internal_dict[word]}']
        except KeyError:
            return [f'{word} not found in LocalDictionary']
