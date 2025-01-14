
__version__ = '3.0.7'
__message__ = 'Version 3 is now online with many new features!\n3.0.1 - Add filter for overbloomig during alignment.\n3.0.2 - Link exoplanet data directly to ExoClock.\n3.0.3 - Option to fit for a/Rs and i.\n3.0.4 - Option to crop reduced images.\n3.0.5 - New catalogue of planets.\n3.0.6 - New catalogue of planets.'

from .__run__ import run_app


def __get_abspath__():
    import os
    return os.path.abspath(os.path.dirname(__file__))
