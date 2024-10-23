# NetBox PtoV Plugin

Netbox plugin for pulling runstate (config and topology) from Arista switches and replicating them in a GNS3 virtual lab using Arista cEOS containers

* Free software: Apache-2.0
* Documentation: https://menckend.github.io/netbox-ptov-plugin/

## Features

Creates a new model/table for storing the DNS names of your GNS3 servers.  *"Boring, Sidney!"*, I know, but it also provides a screen/page that prompts you:

* Select a GNS3 server and as few or as many Arista switches as you want from your devices table.
* Enter a set of Arista EOS credentials
* Enter a project-name to use for a new project on the GNS3 server

And then creates a GNS3 virtual-lab, populated with Arista cEOS container/nodes, each of which is:

* MLAG friendly  (each container is configured to use the system-mac address of the "real" switch it is emulating)
* Running a (cEOS/lab conformed) copy of the startup-config of the switch it is emulating
* Running the same cEOS version as the switch that it is emulating (if you have a matching Docker template installed on your GNS3 server)
* Happy to run as an EVPN/VXLAN fabric, if that's your bag.  (There's some per-VRF/network-namespace ipfilters tweaking that may still need to be cleared up.)

... and spits back a URL at which you can access the virtual-lab you just created. 

## Contemplated Use-cases

Change modeling, obviously.  Invasive troubleshooting of pesky routing issues that you wouldn't want to spend *six hours* setting up a vlab for, but that would be well-worth the effort if it only took two minutes to set up.

[![image](./docs/_static/images/ptov-pic1.png_){:class="img-fluid"}]

## Under the hood

<details><summary>

### Prompts Netbox user to provide/select input

</summary>

* One or more Arista switches from Netbox's device table
* Arista EOS credentials
* An existing GNS3 server (v2.x)
* A project name to use on the GNS3 server

[![image](./_static/images/ptov-pic1.png_){:class="img-fluid"}]

</details>










<details><summary> &nbsp;

### Creates a virtual lab using the [dcnodatg package](https://menckend.github.io/dcnodatg)

</summary>


* Collects configuration and LLDP neighbor details (using Arista eAPI) of the switches specified by the user
* Performs cEOS-lab compatibilty scrubbing on each of the collected configurations
  * Removes logging, AAA, ASIC-only, etc... configuration elements
  * Translates EOS interface names to cEOS interface names
  * Implements an event-driven configuration section that forces the cEOS container to use the same system MAC address as the physical switch
    * Enabling successful mLAG configuration between cEOS instances
  * Etc...
* Iterates through LLDP neighbor information to create a list of physical links between the polled switches
* Creates a new project on the GNS3 server (using the GNS3 API)
* Extracts the existing Docker configuration templates from the GNS3 server (using GNS3 API)
* Identifies the GNS3 device templates for the Arista cEOS versions that match each switch's EOS version
* Instantiates a GNS3 node in the new project for each switch (using GNS3 API)
* Pushes the cEOS-ready version of each switch's startup config to the corresponding Docker container on the GNS3 server (using the Docker API exposed by containerd on the GNS3 server)
* Creates links between the cEOS nodes on the GNS3 project that correspond to the discovered links between the physical switches

</details>

## Features



## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
|     4.1        |      0.1.0     |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/menckend/netbox_ptov
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
