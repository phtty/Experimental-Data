import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

# 创建画布
fig = plt.figure(figsize=(8, 8))
# 使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)  
# 将绘图区对象添加到画布中
fig.add_axes(ax)
#通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
#ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0,0)
#给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
#添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
#设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

Br = np.array([0, 0, 0.000784, 0.000448])
Hc = np.array([1, 0.443, 0, 0])

Bm = np.array([0.0016, 0.00158, -0.0016, -0.00158])
Hm = np.array([4, 4, -4, -4])

plt.plot(Hc, Br, 'b.')
plt.plot(Hm, Bm, 'r.')
plt.xticks(np.arange(-5, 5.5, 1), fontsize = 7)

plt.yticks(np.arange(-0.002, 0.0021, 0.0006), fontsize = 7)
plt.show()
