=======
ddns
=======

Connect to any host with dynamic IP address. With **ddns**, you don't need to bother with ever changing public IP addresses.

Currently supported DNS hosting providers:

- Cloudflare

This tool is described as part of my blog post. To see how I use it, check `blog.karakays.com/how-I-do-connect-home-from-remote`_.


---------------
Requirements
---------------
apt install dnsutils

---------------
Installation
---------------

Install it from source. Clone this repository and run

.. code:: bash

   $ pip install .

Next, set your CloudFlare credentials & other details in environmental variables.

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

.. _blog.karakays.com/how-I-do-connect-home-from-remote: https://blog.karakays.com/how-i-do-connect-home-from-remote
