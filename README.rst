=======
ddns
=======

Connect to any host with dynamic IP address. With **ddns**, you don't need to bother with ever changing public IP addresses.

Currently supported DNS hosting providers:

- Cloudflare

This tool is described as part of my blog post. To see how I use it, check blog.karakays.com/how-I-connect-home-remotely.

---------------
Installation
---------------

Clone this repository and install

.. code:: bash

   $ pip install .

Set your CloudFlare credentials & details

.. code:: bash

   $ export CF_API_KEY='your-cf-api-key' \
   CF_EMAIL='your-cf-account-email' \
   CF_ZONE='your-zone-id' \
   CF_DOMAIN='your-cf-domain'

---------------
License
---------------

`MIT license`

---------------
Authors
---------------

Selçuk Karakayalı <skarakayali@gmail.com>

.. _homepage: https://jwz.org
