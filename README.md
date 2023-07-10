# Botnet Blocklist 
This script adds an outbound block rule to your windows firewall. It uses the feodo tracker list that gets updated every 5 minutes.

## How-to
Powershell needs to be run as admin:
```
py ip_blocker.py
```

## Blocking inbound traffic
You can also add this rule to the code to block inbound traffic:
```
...
if ip != "dst_ip":
        print("Added Outbound Rule to block:", ip)
        outbound_rule = "netsh advfirewall firewall add rule name='BadIP' Dir=Out Action=Block RemoteIP=" + ip
        subprocess.run(["Powershell", "-Command", outbound_rule])
        
        print("Added Inbound Rule to block:", ip)
        inbound_rule = "netsh advfirewall firewall add rule name='BadIP' Dir=In Action=Block RemoteIP=" + ip
        subprocess.run(["Powershell", "-Command", inbound_rule])
```

## Credits
- Idea came from [The PC Security Channel](https://www.youtube.com/watch?v=7UWFJGeix_E), but had some modification in the code, such as using the plain-text the website provides rather than csv.
- [Feodo tracker list](https://feodotracker.abuse.ch/blocklist/)
- Thanks to [Abuse](https://abuse.ch/) for compiling this list.
