import requests, subprocess

response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt")
lines = response.text.splitlines()

rule = "netsh advfirewall firewall delete rule name='BadIP'"
subprocess.run(["Powershell", "-Command", rule])

txt_file = filter(lambda x: not x.startswith("#"), lines)
for row in txt_file:
    ip = row.split()[0]
    if ip != "dst_ip":
        print("Added Rule to block:", ip)
        rule = "netsh advfirewall firewall add rule name='BadIP' Dir=Out Action=Block RemoteIP=" + ip
        subprocess.run(["Powershell", "-Command", rule])
