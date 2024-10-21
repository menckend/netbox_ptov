# NetBox ptov Plugin

NetBox plugin for creating virtual lab topologies (of Arista switches only) that match "live-device"'s configuration and topology.


* Documentation: https://menckend.github.io/netbox_ptov
* dcnodatg project: htpps://menckend.github.io/dcnodatg/

## Features

Provides the ability to select a list of Arista switches from the Netbox "devices" table and instantiate a virtual-lab topology based on their run-state, using the dcnodatg project.  dcnodatg's p_to_v function uses the Arista eAPI to query the switches, pulling startup-config, LLDP neighbor details, and LLDP "self" details.  It then trims out AAA, logging, SNMP,  and other configuration elements not suited for (or just plain not implemented on) the Arista cEOS container images.  Following that, it instantiates a new project on an existing GNS3 server (you'll need to *have* a GNS3 server, with cEOS images pre-installed and defined in GNS3 as device templates.)  Once the project is created, it then instantiates GNS3 nodes for each of the switches it originally polled, pushing the "cEOS-isifed"-version of each switch's startup configuration the corresponding Docker container, and creating connections in the GNS3 project topology (based on what was discovered in the LLDP neighbor tables and "self" information of each switch.)


## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
|     4.1.x      |    >=0.1.14    |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/menckend/netbox-ptov-plugin
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/menckend/netbox_ptov
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'netbox_ptov'
]

PLUGINS_CONFIG = {
    "netbox_ptov": {},
}
```

## Credits

Based on the NetBox plugin tutorial:

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`netbox-community/cookiecutter-netbox-plugin`](https://github.com/netbox-community/cookiecutter-netbox-plugin) project template.
