"""Top-level package for NetBox ptov."""

# __author__ = """Mencken Davidson"""
# __email__ = "mencken@gmail.com"
# __version__ = "0.1.14"


from netbox.plugins import PluginConfig
from .version import __version__


class ptovConfig(PluginConfig):
    base_url = "netbox_ptov"
    default_settings = {
        'device_ext_page': 'right',
        'top_level_menu': False
        }


config = ptovConfig
