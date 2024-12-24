import matplotlib.pyplot as plt
import numpy as np

# Data
bar_one = {
    "std::stable_sort (kv)": 10000 / 9.66e+05,
    "std::sort (kv)": 10000 / 8.51e+05,
}

simd_four = {
    "Proposed SIMD (kv)": 10000 / 5.27e+05,
    "Bramas SIMD (kv)": 10000 / 1.19e+06,
}

simd_sixteen = {
    "Proposed SIMD (kv)": 10000 / 1.26e+05,
    "Bramas SIMD (kv)": 10000 / 4.76e+05,
}

# Normalize data to have the same length
categories = ['Scalar', 'SIMD 4', 'SIMD 16']

# Values for each category
bar_one_values = [bar_one["std::stable_sort (kv)"], bar_one["std::sort (kv)"]]
simd_four_values = [simd_four["Proposed SIMD (kv)"], simd_four["Bramas SIMD (kv)"]]
simd_sixteen_values = [simd_sixteen["Proposed SIMD (kv)"], simd_sixteen["Bramas SIMD (kv)"]]

# Combine values into a single list, ensuring alignment
values = np.array([
    [bar_one_values[0], 0, 0],  # std::stable_sort
    [bar_one_values[1], 0, 0],  # std::sort
    [0, simd_four_values[0], 0],  # Proposed SIMD (SIMD 4)
    [0, simd_four_values[1], 0],  # Bramas SIMD (SIMD 4)
    [0, 0, simd_sixteen_values[0]],  # Proposed SIMD (SIMD 16)
    [0, 0, simd_sixteen_values[1]]   # Bramas SIMD (SIMD 16)
])

# Plotting
fig, ax = plt.subplots()

# Stacked bars
ax.bar(categories, values[0], label='std::stable_sort', color='#1f77b4')
ax.bar(categories, values[1], bottom=values[0], label='std::sort', color='#aec7e8')
ax.bar(categories, values[2], bottom=values[0] + values[1], label='Proposed SIMD (SIMD 4)', color='#ff7f0e')
ax.bar(categories, values[3], bottom=values[0] + values[1] + values[2], label='Bramas SIMD (SIMD 4)', color='#ffbb78')
ax.bar(categories, values[4], bottom=values[0] + values[1] + values[2] + values[3], label='Proposed SIMD (SIMD 16)', color='#2ca02c')
ax.bar(categories, values[5], bottom=values[0] + values[1] + values[2] + values[3] + values[4], label='Bramas SIMD (SIMD 16)', color='#98df8a')

# Add labels, title, and legend
ax.set_xlabel('Implementation')
ax.set_ylabel('Throughput (tuples/ns)')
ax.set_title('Throughput by Implementation and Algorithm')
ax.set_xticks(np.arange(len(categories)))
ax.set_xticklabels(categories)
ax.legend()

# Enhance layout
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

