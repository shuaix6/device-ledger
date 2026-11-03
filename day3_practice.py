temperature = 70
threshold   = 80
if temperature > threshold:
    print("温度超限！请立即检查散热")
print("温度检查完毕")

#===== 练习2：故障次数评级=====
fault_count = 5
if fault_count == 0:
    print("健康：设备状态良好") 
elif fault_count <= 3:
    print("观察：建议加强巡检")
else:
    print("重点跟踪：建议安排专项检修")
