__author__ = """Mencken Davidson"""
__email__ = "mencken@gmail.com"


from netbox.plugins import PluginConfig
from ._version import __version__


class ptov_config(PluginConfig):
    name = 'netbox_ptov'
    verbose_name = 'Physical to Virtual-lab'
    description = 'Builds GNS3 labs w/ config and topology scraped from Arista switches in device tabls'
    version = __version__
    author = 'Mencken Davidson'
    author_email = 'mencken@gmail.com'
    base_url = 'netbox_ptov'
    default_settings = {
        'top_level_menu': False
        }


config = ptov_config
