#花の曲線を描く - CinderellaJapan:https://sites.google.com/site/cinderellajapan/huanocg/huano-qu-xianの図の再現実装
def pcf_to_graph3(pcf, last, ax):
    start = 0 #定義域の左端
    #last = 2*np.pi # 定義域の右端 # コメントアウト
    
    def here_function1(f, th): 
        r = f(th)
        x = r * np.cos(th) # 極座標からの変換(x座標の抽出)
        y = r * np.sin(th) # 極座標からの変換(y座標の抽出)
        return x, y

    th = np.arange(start,last, 0.01)
    x, y = here_function1(pcf, th)

#   fig = plt.figure(figsize=(5,5)) # サイズを均等に
#   ax = fig.add_subplot(1,1,1) 
    ax.set_aspect('equal')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    #ax.axis([-1.2,1.2,-1.2,1.2]) # コメントアウト
    #ax.grid() # グラフにグリッドを追加

    ax.plot(x, y) # 描画
    
last = 2 * np.pi # 周期の定義
fig = plt.figure(figsize=(15,15)) # サイズを均等に

for i in range(1,6):
    for j in range(1,6):
        ax = fig.add_subplot(5,5,(i-1)*5+j)
        pcf_to_graph3(lambda th: np.sin((j/i)*th), last, ax)
        ax.axis([-1.2,1.2,-1.2,1.2])
    last += 2 * np.pi # 周期の定義

#svgで保存
#fig.savefig('5_2.svg',facecolor="azure")
