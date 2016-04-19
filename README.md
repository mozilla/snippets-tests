Snippet-tests
=====================

Automated tests for the Snippets web app

Running Tests
-------------

### Java
You will need a version of the [Java Runtime Environment][JRE] installed

[JRE]: http://www.oracle.com/technetwork/java/javase/downloads/index.html

### Python
Before you will be able to run these tests, you'll need to have Python 2.6
installed.

__note__

The below instructions will install the required Python libraries into your
global Python installation. If you work on multiple Python projects that might
end up needing different versions of the same libraries, you might want to
follow `sudo easy_install pip` with `sudo pip install virtualenv`, and then
create and activate a [virtualenv](http://www.virtualenv.org) (e.g. `virtualenv
snippets-tests-env; source snippets-tests-env/bin/activate`) to
create a clean "virtual environment" for just this project. Then you can
`pip install -r requirements.txt` in your virtual environment
without needing to use `sudo`.

If you don't mind installing globally, just run:

    sudo easy_install pip

followed by:

    sudo pip install -r requirements.txt

__note__

if you are running on Debian or Ubuntu, you may need to do:
    
    sudo apt-get install python-setuptools
    
to install the required Python libraries.

### Running Tests
Once the above prerequisites have been met, you can run the tests using the
following command:

    py.test tests/test_snippets.py

For other possible options, type `py.test --help`.

Writing Tests
-------------

If you want to get involved and add more tests, then there's just a few things
we'd like to ask you to do:

1. Use the [template files][GitHub Templates] for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Make sure all tests are passing, and submit a pull request with your changes

[GitHub Templates]: https://github.com/mozilla/mozwebqa-examples
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide

License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/
