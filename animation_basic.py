#色を対応させて円を描くアニメーション
def here_function1(th): 
    x = np.cos(th)
    y = np.sin(th)
    return x, y

start = 0 #定義域の左端
last = 2*np.pi # 定義域の右端

dx = 0.1
th = np.arange(start,last+dx, dx)
x, y = here_function1(th)

fig = plt.figure(figsize=(12,4), dpi=150) # Figureオブジェクトを作成
ax1 = fig.add_subplot(1,2,1) # figに属するAxesオブジェクトを作成 (縦,横, 自分の番号)
ax2 = fig.add_subplot(1,2,2) # figに属するAxesオブジェクトを作成 (縦,横, 自分の番号)
ax1.set_aspect('equal')
#ax2.set_aspect('equal')

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')
#ax1.axis([-1,7.0,-0.0,10.0])
ax1.axis([-1.2,1.2,-1.2,1.2])
ax1.grid() 
#ax1.set_title('base y = -(x - 3)^2 + 9') # グラフタイトル

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_position('zero')
ax2.spines['left'].set_position('zero')
ax2.grid() 

ax1.plot(x, y, label='circle', color='black') # 描画

artist_list = []
point_list_x = []
point_list_y = []
for i in range(len(th)):
    art = ax1.plot(x[i],y[i], marker='.', color='black', markersize=10, linestyle='None') # 点
    art += [ax1.add_line(lines.Line2D([0,x[i]],[0,y[i]], color='black'))]

    art += [ax1.add_line(lines.Line2D([x[i],0],[y[i],y[i]], color='blue'))]
    art += [ax1.add_line(lines.Line2D([x[i],x[i]],[y[i],0], color='red'))]
    
    
    point_list_x.append(x[i])
    point_list_y.append(y[i])
    art += ax2.plot(th[:i+1],point_list_y, marker='.', color='red', markersize=8, linestyle='None') # 点
    art += ax2.plot(th[:i+1],point_list_x, marker='.', color='blue', markersize=8, linestyle='None') # 点
    
    artist_list.append(art)

# HTML(ani.to_jshtml())
ax1.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=10) # ラベルの反映
ani = ArtistAnimation(fig, artist_list, interval = 50)

plt.close()
HTML(ani.to_jshtml())
