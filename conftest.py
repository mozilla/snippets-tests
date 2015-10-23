# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest


def pytest_addoption(parser):
    parser.addoption('--base-url',
                     default='https://snippets.allizom.org',
                     help='base url for the snippets instance.')


@pytest.fixture
def base_url(request):
    return request.config.option.base_url
