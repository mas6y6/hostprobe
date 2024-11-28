hostprobe docs
=============================
Welcome to the ``hostprobe`` docs!

.. image:: https://github.com/malachi196/hostprobe/blob/main/logo/hostprobe-logo.png
    :alt: hostprobe logo

.. toctree::
    :maxdepth: 2

Hostprobe strives to be a cross platform toolkit for networking.
``
>>> from hostprobe import netprobe
>>> onlinehosts = netprobe("192.168.0.1") #returns a list
>>> print(f"some online hosts: {onlinehosts}")
["192.168.0.1", "192.168.0.7"]

about
----------------------------------

``
api
++++++++++++++++++++++++++++++++++
