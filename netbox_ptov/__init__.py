from netbox.plugins import PluginConfig
from .version import __version__


class ptovConfig(PluginConfig):
    name = 'netbox_ptov'
    verbose_name = 'netbox_ptov'
    description = 'Does this description take preference, or some other one?'
    version = __version__
    author = 'Mencken the init.py Davidson'
    author_email = 'mencken@gmail.com.gmail.mencken.com'
    base_url = "netbox_ptov"
    default_settings = {
        'device_ext_page': 'right',
        'top_level_menu': False
        }


config = ptovConfig
