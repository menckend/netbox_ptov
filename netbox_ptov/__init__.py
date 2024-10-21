"""Top-level package for NetBox ptov."""

#__author__ = """Mencken Davidson"""
#__email__ = "mencken@gmail.com"
#__version__ = "0.1.14"


from netbox.plugins import PluginConfig
from .version import __version__


class ptovConfig(PluginConfig):
    name = "netbox_ptov"
    author = "Mencken Davidson"
    author_email = "mencken@gmail.com"
    verbose_name = "NetBox ptov plugin"
    description = "NetBox plugin for creating GNS3 virtual-labs of Arista switches."
    version = "0.1.14"
    base_url = "netbox_ptov"
   default_settings = {
        'device_ext_page': 'right',
        'top_level_menu' : False,
    }


config = ptovConfig
