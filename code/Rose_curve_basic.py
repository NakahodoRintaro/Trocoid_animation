#これでバラ曲線が描ける
last = 2 * np.pi # 周期の定義

n = 4
k = 1

def rose(th):
    r = np.sin((n/k)*th)
    return r
pcf_to_graph2(rose, last)
