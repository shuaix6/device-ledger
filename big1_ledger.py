devices = [{"name":"数控机床","model":"CNC-850","power":15.5,"location":"3号车间"},
           {"name":"焊接机器人","model":"WR-200","power":8.2,"location":"1号车间"},
           {"name":"传送带","model":"CV-100","power":3.0,"location":"2号车间"},
           {"name":"质检摄像头","model":"QC-50","power":0.5,"location":"4号车间"}]
for device in devices:
    print(device["name"],device["model"],device["power"],device["location"])
print(len(devices))