import matplotlib.font_manager as fm

# List all fonts that matplotlib can find on your system
font_list = sorted([f.name for f in fm.fontManager.ttflist])

# print(font_list)

for font in font_list:
    print(font)

# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 
#     