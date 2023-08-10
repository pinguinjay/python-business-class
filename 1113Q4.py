#輸入區
n = int(input())
assemble_time = list(map(int,input().split(',')))
package_time = list(map(int,input().split(',')))

#創建list
assemble_finish_time = [0] *n #組裝時間
idle_time = [0]*n   #閒置時間
package_finish_time = [0]*n  #包裝完成時間
#計算
def PackageFinishTimeCal(x) :
    time= package_finish_time[x-1] + idle_time[x] + package_time[x]
    return time
for i in range(n) : #先得到所有組裝時間列
    if i == 0 :
        assemble_finish_time[i] = assemble_time[i]
    else :
        assemble_finish_time[i] = assemble_finish_time[i-1] + assemble_time[i]
idle_time[0] = assemble_finish_time[0]
package_finish_time[0] = idle_time[0] + package_time[0]
for i in range(1,n) :
    if package_finish_time[i-1] < assemble_finish_time[i]:
        idle_time[i] = assemble_finish_time[i] - package_finish_time[i-1]
        package_finish_time[i] = PackageFinishTimeCal(i)
    elif package_finish_time [i-1]>= assemble_finish_time[i] :
        idle_time[i] = 0
        package_finish_time[i] = PackageFinishTimeCal(i)

#輸出區
result = ",".join(str(item) for item in package_finish_time)
total_idle_time = sum(idle_time)
print(result + "," + str(total_idle_time))
