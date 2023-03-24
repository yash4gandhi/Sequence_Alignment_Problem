import matplotlib.pyplot as plt

ps = [96, 128, 160, 256, 320, 384, 512, 576, 640, 768, 1024, 1152, 1280, 1536, 2048]

# for basic
memory = [79.999, 154.921, 160.097, 606.705, 605.233, 1201.502, 2394.012, 1205.685, 2415.073, 4763.227, 9507.939, 4771.061, 9501.692, 18964.845, 37891.162]
time =[0.0, 0.0, 0.015, 0.057, 0.058, 0.11, 0.213, 0.144, 0.271, 0.554, 0.89, 0.61, 1.216, 2.13, 6.216]

# for dc
memory_dc = [17.204, 24.254, 19.085, 40.562, 83.886, 43.134, 71.374, 208.849, 48.229, 128.780, 130.338, 458.453, 248.168, 250.314, 245.686 ]
time_dc = [0.014, 0.028, 0.033, 0.116, 0.113, 0.226, 0.451, 0.28, 0.461, 1.079, 2.232, 1.29, 2.545, 5.021, 10.811 ]

plt.title('Memory(KB) vs Problem Size')

plt.plot(ps, memory, label = "basic", marker='o', markerfacecolor='blue', markersize=5)
plt.plot(ps, memory_dc, label = "efficient", marker='o', markerfacecolor='orange', markersize=5)

plt.xlabel("Problem Size (m+n)")
plt.ylabel("Memory usage(KB)")
plt.legend()

plt.savefig('MemoryPlot.png')
plt.show()

plt.title('CPU Time(s) vs Problem Size')

plt.plot(ps, time, label = "basic", marker='o', markerfacecolor='blue', markersize=5)
plt.plot(ps, time_dc, label = "efficient", marker='o', markerfacecolor='orange', markersize=5)

plt.xlabel("Problem Size (m+n)")
plt.ylabel("CPU Time (s)")
plt.legend()

plt.savefig('Time_ProblemSize.png')
plt.show()