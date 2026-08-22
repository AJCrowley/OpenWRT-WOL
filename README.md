# OpenWRT-WOL

## Wake on LAN python script for OpenWRT routers

Just put the python script in the /root home directory.

To install, make sure to:

```opkg install python3 etherwake```

Add the wol_service file to /etc/init.d,

```chmod +x /etc/init.d/wol_service```

Then enable and start it with
```
/etc/init.d/wol_service enable
/etc/init.d/wol_service start
```

You can stop and query the status of the service with:
```
/etc/init.d/wol_service status
/etc/init.d/wol_service stop
```

Then simple attach your webhook to your routers IP like so: ```http://router:5050/wol?mac=ff:ff:ff:ff:ff```

To use iPhone shortcuts to wake your computer, create a shortcut that uses SSH to log into your router, then call ```curl http://localhost:5050/wol?mac=ff:ff:ff:ff:ff```
This will allow you to use Siri to call the shortcut with a command like, "Siri, boot PC", or however you name the shortcut.
