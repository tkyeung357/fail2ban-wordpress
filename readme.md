# why
a fail2ban and wordpress setup to study and test how to use fail2ban to protect wordpress wp-login.php and xmlrpc.php

# build task and check fail2ban status
config located in .vscode/tasks.json
- Mac: shift+cmd+b 

# fail2ban
- config located in /fail2ban/
- filter located in /filter.d/

# how to test
I use burp suite intrunder to test fail2ban
payload:
- snipe-login.txt 
- snipe-rpc.txt