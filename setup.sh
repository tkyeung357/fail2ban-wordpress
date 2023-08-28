#!/bin/bash

set -e

echo "Starting UFW..."
ufw default allow incoming
ufw default allow outgoing
ufw enable

echo "Starting Fail2Ban..."
fail2ban-client -x start

echo "Starting Apache2..."
#service apache2 start
python3 /api/app.py

exec "$@"
