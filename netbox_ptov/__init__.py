from netbox.plugins import PluginConfig
from netbox_ptov._version import __version__
from importlib import metadata

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    __version__ = "0.1.0"

class PtovConfig(PluginConfig):
    name = 'netbox_ptov'
    verbose_name = 'Physical to Virtual-lab'
    description = 'Builds GNS3 labs with config and topology scraped from Arista switches in device tables'
    version = __version__
    author = 'Mencken Davidson'
    author_email = 'mencken@gmail.com'
    base_url = 'netbox_ptov'
    min_version = '4.2.0'
    max_version = '4.2.9'
    required_settings = []
    default_settings = {
        'top_level_menu': True
    }

    def ready(self):
        """
        Register models with NetBox's registry system
        """
        super().ready()
        from .models import GNS3Server, ptovjob, switchtojob
        from netbox.registry import registry
        registry['plugins']['netbox_ptov'] = {
            'models': {
                'gns3server': GNS3Server,
                'ptovjob': ptovjob,
                'switchtojob': switchtojob
            }
        }


config = PtovConfig
