'''
Created on 2020. 8. 20.

@author: GDJ24
'''
from matplotlib import ft2font
import matplotlib.pyplot as plt # pip install ggplot

plt.style.use("ggplot")
subjects = ["Java","Jsp","Spring","Hadoop","Python"]
print(range(len(subjects)))
subjects_index = range(len(subjects))
print(type(subjects))
scores = [65, 90, 85, 60, 95] # 수치 데이터
fig = plt.figure() # 그래프 출력 # 그래프 그릴 공간, 도화지
axl = fig.add_subplot(1,1,1) # 도화지 분리. 1개의 도화지에 여러개의 그림이 가능
# 현재 프로그램은 1개의 그림만 그림
# 1행 1열 분리 -> 그림의 한계
# 1 -> 1번째 그림
axl.bar(subjects_index, scores, align="center", color="darkblue") # 막대 그래프

axl.xaxis.set_ticks_position("bottom")
axl.yaxis.set_ticks_position("left")

plt.xticks(subjects_index, subjects, rotation=0, fontsize="small")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Class Score")
#그래프를 img 파일로 저장
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")
plt.show()