# -*- coding: utf-8 -*-
from urllib import urlencode

from django.conf import settings
from django.core.urlresolvers import reverse


def get_abs_url(voting, referer):
    voting_url = reverse('voting', args=[voting.url_hash])
    qs = urlencode({'ref': referer})
    return '{}{}?{}'.format(settings.BASE_URL, voting_url, qs)


def get_abs_deadline_hack_url(voting):
    voting_url = reverse('voting', args=[voting.url_hash])
    return '{}/deadline_hack{}'.format(settings.BASE_URL, voting_url)
