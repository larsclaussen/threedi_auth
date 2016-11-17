=============================
threedi-auth
=============================

.. image:: https://badge.fury.io/py/threedi_auth.png
    :target: https://badge.fury.io/py/threedi_auth

.. image:: https://travis-ci.org/larsclaussen/threedi_auth.png?branch=master
    :target: https://travis-ci.org/larsclaussen/threedi_auth

Gebruiker authenticatie en autorisatie vonden tot nu toe beide plaats in de SSO server. Aangezien dit leidde tot beheerproblemen is besloten om de SSO server alleen nog maar authenticatie te laten doen. De verschillende applicaties zoals Lizard en 3Di zorgen dan zelf voor implementatie van de autorisatie kant, is het idee. In dit plan wordt de uitwerking hiervan voorgesteld.

Documentation
-------------

The full documentation is at https://threedi_auth.readthedocs.org.

Quickstart
----------

Install threedi-auth::

    pip install threedi_auth

Then use it in a project::

    import threedi_auth

Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
