device = {
    "name":"数控机床 CNC-850",
    "model":"CNC-850",
    "power":15.5,
}

print(device["name"])
print(device["model"])
print(device["power"])

device["power"] = 20
device["location"] = "车间 A"

print(device)
