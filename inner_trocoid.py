def circle(x, y, r, th):
    x1 = np.cos(th)
    y1 = np.sin(th)
    return x1 *  r + x, y1 * r + y

def rotation(x0,y0, th):
    A = np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
    vec = np.array([x0,y0])
    return np.dot(A,vec)

def trocoid(th):
    x = (rc - rm )*np.cos(th) + rd*np.cos(((rc-rm)/rm)*th)
    y = (rc - rm )*np.sin(th) - rd*np.sin(((rc-rm)/rm)*th)
    return x, y

start = 0 #定義域の左端
last = 14*np.pi # 定義域の右端
rc = 6
rm = 2.8
rd = 2.8
dx = 0.1
th = np.arange(start,last+dx, dx)
x, y = circle(0,0,rc,th)

fig = plt.figure(figsize=(4,4)) # サイズを均等に
ax = fig.add_subplot(1,1,1) 
ax.set_aspect('equal')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
# ax.axis([-1.2,1.2,-1.2,1.2])
#ax.grid() # グラフにグリッドを追加

ax.plot(x, y, label='circle', color='blue') # 描画
x0 = rc - rm
y0 = 0

artist_list = []
point_list_x = []
point_list_y = []
for i in range(len(th)):
    x_cir, y_cir= circle(x0,y0,rm,th)
    art = ax.plot(x_cir,y_cir, color='black') # 点
    point_x, point_y = trocoid(th[i])
    point_list_x.append(point_x)
    point_list_y.append(point_y)
    art += ax.plot(point_list_x, point_list_y, color='red')
    art += [ax.add_line(lines.Line2D([x0, point_x],[y0, point_y], color='black'))]
    art += ax.plot(x0, y0, color='black', marker='.', markersize=10)
    art += ax.plot(point_x, point_y, color='red', marker='.', markersize=10)
    artist_list.append(art)
    x0,y0 = rotation(x0,y0,dx)


ax.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=10) # ラベルの反映
ani = ArtistAnimation(fig, artist_list, interval = 50)

plt.close()
HTML(ani.to_jshtml())

#ani.save('./anime3.mp4', writer="ffmpeg") # mp4で保存
