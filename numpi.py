#~~~~~~~~~~~~
# from numpy import random
# import matplotlib.pyplot as plt
# x = random.randint(100,1000,5)
# def func(s,d):
#     t = int(round(s/100.*sum(d)))
#     return f'{s:.1f}%\n( {t}m1 )'

# plt.pie(x,
#         radius=1.5,
#         textprops={'color':'w','weight':'bold','size':12},
#         pctdistance=0.7,
#         autopct=lambda i:func(i,x),
#         wedgeprops={'linewidth':3,'edgecolor':'w'})

# plt.show()
#-------------------------------------------------------------------------------
# import matplotlib
# import matplotlib.pyplot as plt

# from matplotlib.font_manager import FontProperties

# category = ['非常滿意','滿意','普通','不滿意','非常不滿意']
# expend = [65,97,103,45,51]
# color = ['#ff0000', '#d200d2', '#66b3ff', '#28ff28', '#ffff37']


# plt.figure(figsize=(12,8))
# separeted = (0,0,0,0,0)

# pictures,category_text,percent_text = plt.pie(
#     expend,
#     colors=color,
#     labels=category,
#     autopct="%0.2f%%",
#     explode=separeted,
#     pctdistance=0.65,
#     radius=0.7,
#     center=(-10,0),
#     shadow=False)


# for t in category_text:
#     t.set_fontproperties(myFont)
# for t in percent_text:
#     t.set_fontproperties(myFont)

# plt.legend(loc = "center right",prop=myFont)
# plt.title("範例",fontproperties=myFont,x=0.5,y=1.03)

# plt.show()
#-------------------------------------------------------------------------------


import matplotlib.pyplot as plt

election_data = {'biden':65,'滿意':97,'普通':103,'不滿意':45,'非常不滿意':51}
candidate = [key for key in election_data]
votes = [value for value in election_data.values()]
plt.figure(figsize=(10,10),dpi=100)
plt.pie(votes,labels=candidate,autopct="%1.2f%%",textprops={'fontsize':24},labeldistance=1.05)
# plt.legend(fontsi)
plt.show()