:orphan:

installing hostprobe
===============================
The best way of installing hostprobe is through pip:

.. code-block:: bash

    pip install hostprobe


If you are using an ARM64 device (ie. raspberry pi), you may need to use

.. code-block:: bash

    pip install hostprobe --break-system-packages


If you wish to install hostprobe version from github (good for getting prereleases), use:

.. code-block:: bash

    pip install hostprobe@git+https://github.com/malachi196/hostprobe