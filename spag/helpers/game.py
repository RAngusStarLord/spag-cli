import requests
from spag.helpers import constants, urlJoin


def get_games(name):

    base_url = constants.gb_url
    extension = "/games/"

    try:
        f = open("key.txt", "r")
        key = f.read()
        f.close()
    except FileNotFoundError:
        return "Cannot find API Key - have you run configure"

    url_parameters = {
        "api_key": key,
        "format": "json",
        "field_list": "name,guid"
    }

    if name != "":
        url_parameters.update({"filter": "name:%s" % name})

    headers = {
        "User-Agent": "SPAG Python CLI"
    }

    url = urlJoin.join_url(base_url, extension, url_parameters)

    r = requests.request("GET", url, headers=headers)
    r = r.json()

    return r["results"]


def get_dlc_date(url):
    try:
        f = open("key.txt", "r")
        key = f.read()
        f.close()
    except FileNotFoundError:
        return "Cannot find API Key - have you run configure"

    url_parameters = {
        "api_key": key,
        "format": "json",
        "field_list": "release_date"
    }

    headers = {
        "User-Agent": "SPAG Python CLI"
    }

    url = urlJoin.join_url(url, "", url_parameters)

    r = requests.request("GET", url, headers=headers)
    r = r.json()

    return r["results"]


def sort_dlcs(payload):
    for dlc in payload["results"]["dlcs"]:
        release_date = get_dlc_date(dlc["api_detail_url"])
        del dlc["api_detail_url"]
        del dlc["site_detail_url"]
        del dlc["id"]
        dlc.update(release_date)

    payload["results"]["dlcs"].sort(key=lambda x: x["release_date"])

    return payload


def get_game(guid, dlc):

    base_url = constants.gb_url
    extension = "/game/%s/" % guid

    try:
        f = open("key.txt", "r")
        key = f.read()
        f.close()
    except FileNotFoundError:
        return "Cannot find API Key - have you run configure"

    url_parameters = {
        "api_key": key,
        "format": "json",
        "field_list": "name,guid"
    }

    headers = {
        "User-Agent": "SPAG Python CLI"
    }

    if dlc is True:
        url_parameters.update({"field_list": "name,guid,dlcs"})

    url = urlJoin.join_url(base_url, extension, url_parameters)

    r = requests.request("GET", url, headers=headers)
    r = r.json()

    if dlc is True and "dlcs" in r["results"]:
        r = sort_dlcs(r)

    return r["results"]
