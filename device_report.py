device_name  = "数控机床 CNC-850"
fault_code   = "E02"
fault_count  = 3
current_temp = 92

print("==== 设备健康评估 =====")
print("设备:" + device_name)

if fault_code == "E01":
    print("[一级故障] 立即停机，通知维修班组")
elif fault_code == "E02":
    print("[二级故障] 限速运行，2 小时内安排检修")
else:
    print("[普通故障] 登记备案")

if fault_count == 0:
    print("[健康] 设备状态良好")
elif fault_count <= 3:
    print("[观察] 建议加强巡检")
else:
    print("[重点跟踪] 建议安排专项检修")

if current_temp > 90:
    print("[高温警告] 请检查散热系统")
else:
    print("[温度正常]")

print("===== 评估完成 =====")