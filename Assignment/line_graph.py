from turtle import color
from matplotlib import axes
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
 
# Dataset
x = np.array([20, 40, 60, 80,100])

#  Time information(y,z,p,w).
y = ([      1.0159768556293689e-05,             
            0.00014805480053550318,
            0.0005764898500944439,
            0.0010692019211618524,
            0.0018414265231082314
])

z = ([    
            1.28909916121633429e-059,             
            0.0001291112246262399779,
            0.000939800532692357129,
            0.001929259673570331779,
            0.00298945968798587199
])

p = ([    
            0.0001038996796858938,             
            0.0008290253187480726,
            0.0027048468589782717,
            0.0076168449301468695,
            0.014516206164109079
])

w = ([      
            0.00014167835837916324,             
            0.0016436281957124409,
            0.005125548337635241,
            0.012524782983880293,
            0.024595910624453897
])


#  Length information(y,z,p,w).
# y = ([      11.0,             
#             86.21052631578948,
#             288.7894736842105,
#             681.8947368421053,
#             1328.6842105263158
# ])

# z = ([    
#             11.321052631578947,             
#             90.77368421052631,
#             294.7894736842105,
#             712.9973684210527,
#             1467.9605263157894
# ])

# p = ([    
#             4.936842105263158,             
#             17.96578947368421,
#             42.10263157894737,
#             80.55,
#             122.78947368421052
# ])

# w = ([      
#             4.94736842105263,             
#             20.74736842105263,
#             50.4315789473684,
#             92.88421052631578,
#             146.00263157894736
# ])

# smoothing connections.

x_sm = np.linspace(x.min(),x.max(),1000)
X_Y_Spline = make_interp_spline(x, y)
X_Z_Spline = make_interp_spline(x, z)
X_W_Spline = make_interp_spline(x, w)
X_P_Spline = make_interp_spline(x, p)

X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
Z_ = X_Z_Spline(X_)

P_ = X_P_Spline(X_)
W_ = X_W_Spline(X_)

plt.plot(X_, Y_,color="green")
plt.plot(X_, Z_,color="blue")
plt.plot(X_, P_,color="black")
plt.plot(X_, W_,color="red")


# plot solution time graph
plt.xlabel("Numbers of Nodes in the graph. ")
plt.ylabel("Average Solution Time(sec).")
plt.text(35, 0.024595910624453897/1.4, '@A*', style='italic',color="red")
plt.text(35, 0.024595910624453897/1.6, "@Dijkstra'", style='italic',color="black")
plt.text(35, 0.024595910624453897/1.8, '@DFS', style='italic',color="blue")
plt.text(35, 0.024595910624453897/2, '@BFS', style='italic',color="green")

plt.text(17, -0.001, '(1X)', style='italic')
plt.text(37, -0.001, "(2X)", style='italic')
plt.text(57, -0.001, '(3X)', style='italic')
plt.text(77, -0.001, '(4X)', style='italic')
plt.text(97, -0.001, '(5X)', style='italic')

plt.title("Solution time comparison between BFS, DFS, Dijkstra's, and A* Algorisms.")
  
  
# plot solution Length graph.
  
# plt.xlabel("Numbers of Nodes in the graph. ")
# plt.ylabel("Average Solution Length(Nodes).")
# plt.text(35, 600, '@A*', style='italic',color="red")
# plt.text(35, 720, "@Dijkstra'", style='italic',color="black")
# plt.text(35, 840, '@DFS', style='italic',color="blue")
# plt.text(35, 960, '@BFS', style='italic',color="green")

# plt.text(17, -60, '(1X)', style='italic')
# plt.text(37, -60, "(2X)", style='italic')
# plt.text(57, -60, '(3X)', style='italic')
# plt.text(77, -60, '(4X)', style='italic')
# plt.text(97, -60, '(5X)', style='italic')

# plt.title("Solution time comparison between BFS, DFS, Dijkstra's, and A* Algorisms.")
  
  
  
  

plt.show()