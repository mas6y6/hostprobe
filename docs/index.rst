hostprobe docs
=============================
Welcome to the ``hostprobe`` docs!

.. image:: _static/hostprobe.png
    :alt: hostprobe logo

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :glob:

    content/*

Hostprobe strives to be a cross platform toolkit for networking. 

|

``
>>> from hostprobe import netprobe  
>>> onlinehosts = netprobe("192.168.0.1") #returns a list  
>>> print(f"some online hosts: {onlinehosts}")  
["192.168.0.1", "192.168.0.7"]
``

about
----------------------------------
This project is meant to be a cross-system
toolkit for probing networks, with tools similar
to nmap, but in python. Confirmed operating systems are
* Windows
* MacOS
* Linux
* Unix