hostprobe docs
=============================
Welcome to the ``hostprobe`` docs!

.. image:: _static/hostprobe.png
    :alt: hostprobe logo

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :caption: Hostprobe:

    content/installation
    content/api

Hostprobe strives to be a minimal cross-platform toolkit for networking. It uses the
built-in python socket module to extract info from a network, such as if a 
device is online, or all the online devices on your network. Hostprobe should
have the capabilities of nmap, while being completely cross system, and in python.

.. code-block:: python

    from hostprobe import netprobe  
    onlinehosts = netprobe("192.168.0.1") #returns a list  
    print(f"some online hosts: {onlinehosts}")  
    #["192.168.0.1", "192.168.0.7"]


about
----------------------------------
This project is meant to be a cross-system network
probning toolkit, although confirmed operating systems are:

* Windows
* MacOS
* Linux
* Unix