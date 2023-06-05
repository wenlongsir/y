import matplotlib.pyplot as plt
import numpy as np

# 创建画布和子图
fig, ax = plt.subplots()

# 设置画布大小和背景颜色
fig.set_size_inches(5, 5)
ax.set_facecolor('black')

# 计算五角星的顶点坐标
theta = np.linspace(0, 2*np.pi, 6)
x = np.sin(theta)
y = np.cos(theta)

# 绘制五角星
ax.plot(x, y, color='red', linewidth=5, linestyle='-', zorder=1)
ax.fill(x, y, color='yellow', zorder=0)

# 设置坐标轴范围和刻度
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xticks([])
ax.set_yticks([])

# 显示图形
plt.show()
