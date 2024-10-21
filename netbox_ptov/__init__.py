"""Top-level package for NetBox ptov."""

__author__ = """Mencken Davidson"""
__email__ = "mencken@gmail.com"
__version__ = "0.1.12"


from netbox.plugins import PluginConfig


class ptovConfig(PluginConfig):
    name = "netbox_ptov"
    verbose_name = "NetBox ptov plugin"
    description = "NetBox plugin for creating GNS3 virtual-labs of Arista switches."
    version = "version"
    base_url = "netbox_ptov"


config = ptovConfig
