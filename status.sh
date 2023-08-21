#!/bin/bash

docker exec -it wordpress-fail2ban-server fail2ban-client status
docker exec -it wordpress-fail2ban-server fail2ban-client banned
