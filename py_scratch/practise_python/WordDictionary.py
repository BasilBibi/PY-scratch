from abc import ABC, abstractmethod
import requests
import json


class Dictionary(ABC):
    @abstractmethod
    def lookup(self, word):
        return

    @abstractmethod
    def extract_definition_from_result(self, lookup_result):
        return


class OnlineOxfordDictionary(Dictionary):
    # for more information on how to install requests
    # http://docs.python-requests.org/en/master/user/install/#install
    _app_id = '9286dd2e'
    _app_key = '8651b0907938b33bb76e99cb157288d2'
    _language = 'en'
    _base_url = f'https://od-api.oxforddictionaries.com:443/api/v1/entries/{_language}'
    _success = 200
    _word_not_found = 404

    def lookup(self, word):
        url = f'{OnlineOxfordDictionary._base_url}/{word.lower()}'
        r = requests.get(url, headers={'app_id': OnlineOxfordDictionary._app_id, 'app_key': OnlineOxfordDictionary._app_key})

        if r.status_code == self._success:
            return self.extract_definition_from_result(r.text)
        elif r.status_code == self._word_not_found:
            return [f'Oxford Online Dictionary could not find {word}']
        else:
            return ['Oxford Online Dictionary did not respond']

    def extract_definition_from_result(self, lookup_result):
        j = json.loads(lookup_result)
        senses = j['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
        definitions = [f'{i+1} : {sense["short_definitions"][0]}' for i, sense in enumerate(senses)]
        return definitions


class LocalDictionary(Dictionary):
    def __init__(self, csv_file_path):
        self._internal_dict = LocalDictionary._make_internal_dict(csv_file_path)

    @staticmethod
    def _make_internal_dict(filename):

        def make_tuple(line):
            s = line.strip().split(',')
            return s[0],s[1]

        filepath = LocalDictionary._get_file_path(filename)
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

    def extract_definition_from_result(self, lookup_result):
        pass
