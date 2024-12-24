import matplotlib.pyplot as plt
import numpy as np

# 操作名称
operations = [
    "Set-Union", "Set-Intersection", "Set-XOR", "Set-Diff", 
    "Join-Full-Outer", "Join-Inner", "Join-Outer-Excluding", 
    "Join-Left-Excluding", "Join-Left"
]

# 用于存储不同SIMD配置的数据
data = {
    "Scalar": [0.15267175572519084,0.15267175572519084, 0.15384615384615385, 0.15625, 0.12658227848101267, 0.1388888888888889, 0.13071895424836602, 0.14705882352941177, 0.1360544217687075],
    "SIMD 4": [0.29411764705882354,0.3656307129798903,0.3401360544217687, 0.35714285714285715, 0.21299254526091588, 0.31695721077654515, 0.2680965147453083, 0.29895366218236175, 0.2994011976047904],
    "SIMD 16": [1.2195121951219512, 1.36986301369863, 1.1976047904191616, 1.3333333333333333, 0.8097165991902834, 1.1363636363636365, 0.9216589861751152, 1.075268817204301, 1.0810810810810811],
}

# 设置柱的宽度
bar_width = 0.1

# 设置x轴位置
r = np.arange(len(operations))

# 绘制每组柱状图
plt.bar(r, data["Scalar"], color='white', edgecolor='black', hatch='//', width=bar_width, label='Scalar')
plt.bar(r + bar_width, data["SIMD 4"], color='purple', width=bar_width, label='SIMD 4')
plt.bar(r + 3*bar_width, data["SIMD 16"], color='brown', width=bar_width, label='SIMD 16')

# 添加图例和标签
plt.xlabel('Operation')
plt.ylabel('Throughput (tuples/ns)')
plt.xticks(r + 2.5*bar_width, operations, rotation=45, ha='right')
plt.legend()

# 显示图表
plt.tight_layout()
plt.show()

