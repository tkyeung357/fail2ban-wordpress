# why
a fail2ban and WordPress setup to study and test how to use fail2ban to protect WordPress wp-login.php and xmlrpc.php

# build task and check fail2ban status
config located in .vscode/tasks.json
- Mac: shift+cmd+b 

# fail2ban
- config located in /fail2ban/
- filter located in /filter.d/

# How to test
I use Burp suite intruder to test fail2ban
payload:
- snipe-login.txt 
- snipe-rpc.txt

# Updates
- 2023-Aug-28 Add demo of Fail2Ban API (Ref: https://github.com/egorsmkv/fail2ban-scripts)