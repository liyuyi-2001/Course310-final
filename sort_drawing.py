import matplotlib.pyplot as plt
import numpy as np

# 数据
bar_one = {
    "std::stable_sort": 10000 / 9.66e+05,
    "std::sort": 10000 / 8.51e+05,
}

simd_four = {
    "Proposed SIMD (4)": 10000 / 5.27e+05,
    "Bramas SIMD (4)": 10000 / 1.19e+06,
}

simd_sixteen = {
    "Proposed SIMD (16)": 10000 / 1.26e+05,
    "Bramas SIMD (16)": 10000 / 4.76e+05,
}

# 计算吞吐量
labels = [
    "std::stable_sort", 
    "std::sort", 
    "Proposed SIMD (4)", 
    "Bramas SIMD (4)", 
    "Proposed SIMD (16)", 
    "Bramas SIMD (16)"
]

values = [
    bar_one["std::stable_sort"],
    bar_one["std::sort"],
    simd_four["Proposed SIMD (4)"],
    simd_four["Bramas SIMD (4)"],
    simd_sixteen["Proposed SIMD (16)"],
    simd_sixteen["Bramas SIMD (16)"]
]

x = np.arange(len(labels))  # 标签位置
width = 0.5  # 柱状图宽度

# 定义稍深的莫兰蒂色系
colors = ['#b08ea2', '#8f7d7d', '#a1b0a1', '#c49ca8', '#8a9db0', '#a0a0a0']

# 绘制柱状图
fig, ax = plt.subplots(figsize=(12, 6))
rects = ax.bar(x, values, width, color=colors, edgecolor='black')

# 添加标签和标题
ax.set_ylabel('Throughput (tuples/ns)', fontsize=12)
ax.set_title('Throughput by Implementation and Algorithm', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)

# 添加图例
ax.legend(labels)

# 自动添加数据标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # 5 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10, color='black')

autolabel(rects)

plt.tight_layout()
plt.show()

