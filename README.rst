CRC-ITU |Build Status| |Coverage Status|
========================================

Installation
------------

Install universal wheel

.. code:: bash

    $ pip install CRC-ITU


Install with cython extension

.. code:: bash

    $ pip install cython
    $ pip install --no-binary :all: CRC-ITU


Usage
-----

.. code:: python

    from crc_itu import crc16
    print(hex(crc16(b'your bytes')))

.. |Build Status| image:: https://travis-ci.org/ak64th/CRC-ITU.svg?branch=master
   :target: https://travis-ci.org/ak64th/CRC-ITU

.. |Coverage Status| image:: https://coveralls.io/repos/github/ak64th/CRC-ITU/badge.svg?branch=master
   :target: https://coveralls.io/github/ak64th/CRC-ITU?branch=master