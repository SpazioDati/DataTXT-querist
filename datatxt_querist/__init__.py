# -*- coding: utf-8 -*-
"""
DataTXT-querist
A simple library to query DataTXT API
"""

import urllib
import requests

DATATXTBASEURL = 'http://spaziodati.eu/datatxt/v3/'

MAXTRIES = 10


class DataTXTQuerist(object):
    """
    Performs a query on DataTXT API
    """

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.params = dict()

    def set_params(self, lang='en', rho=0.3, dbpedia=False):
        assert isinstance(lang, str) and lang in ['it', 'en']
        assert isinstance(rho, float)
        assert isinstance(dbpedia, bool)

        self.params.update({'lang': lang,
                            'rho': rho,
                            'dbpedia': dbpedia
                            })
        return self

    def query(self, text, lang=None, rho=None, dbpedia=None):

        if lang is not None:
            assert isinstance(lang, str) and lang in ['it', 'en']
            self.params['lang'] = lang
        if rho is not None:
            assert isinstance(rho, float)
            self.params['rho'] = rho
        if dbpedia is not None:
            assert isinstance(dbpedia, bool)
            self.params['dbpedia'] = dbpedia

        reqparams = dict()
        reqparams['text'] = urllib.unquote(text).replace(' ', '_')
        reqparams['app_id'] = self.app_id
        reqparams['app_key'] = self.app_key
        reqparams.update(self.params)
        res = requests.get(DATATXTBASEURL, params=reqparams)

        if not res.ok:
            res.raise_for_status()

        return res.json()

if __name__ == "__main__":

    dtq = DataTXTQuerist(app_id='YOUR APP ID',
                         app_key='YOUR APP KEY')

    dtq.set_params(lang='it',
                   rho=0.2,
                   dbpedia=True)

    # Produces
    #http://spaziodati.eu/datatxt/v3/
    #?dbpedia=true
    #&rho=0.2
    #&lang=it
    #&app_id=YOUR APP ID
    #&app_key=YOUR APP KEY
    #&text=il+primo+ministro+David+Cameron+%C3%A8+nato+a+Londra
    print dtq.query('il primo ministro David Cameron è nato a Londra')
    print

    # Produces
    #http://spaziodati.eu/datatxt/v3/
    #?dbpedia=true
    #&rho=0.5
    #&lang=en
    #&app_id=YOUR APP ID
    #&app_key=YOUR APP KEY
    #&text=Diego+Armando+Maradona+played+in+SSC+Napoli+from+1984+to+1991
    print dtq.query('Maradona played in SSC Napoli from 1984 to 1991',
                    lang='en',
                    rho=0.15,
                    dbpedia=True
                    )
    print
