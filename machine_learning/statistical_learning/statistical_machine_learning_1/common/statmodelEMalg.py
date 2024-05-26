import numpy as np

class EMmixBernoulli:
    """
    混合ベルヌーイ分布のEMアルゴリズム
    
    Parameters:
    ---
    x: data matrix
    K: number of components
        
    Returns: 
    ---
    p: likelihood of each component
    q: mixing probability
    BIC: Bayesian information criterion
    gmm: auxiliary parameter in EM algorithm
    """
    def __init__(self, K=5, maxitr=1000, tol=1e-5, succ=3):
        # コンポーネント数
        self.K = K
        # EMアルゴリズムの最大反復数
        self.maxitr = maxitr
        # 収束判定パラメータ
        self.tol = tol
        self.succ = succ

    # EMアルゴリズムでパラメータ推定
    def fit(self, x):
        K = self.K
        maxitr = self.maxitr
        tol = self.tol
        succ = self.succ
        # データ数nと次元d
        n, d = x.shape
        # コンポーネント初期設定
        eps = np.finfo(float).eps
        mu = np.mean(x)
        p = np.random.beta(mu, 1-mu, size=K*d).reshape(K, d)
        # 混合確率
        q = np.repeat(1/K,K)
        ul = np.inf
        converge_ = False
        succ_dec = np.repeat(False, succ)
        # EMアルゴリズム
        for itr in np.arange(maxitr):
            # 多次元ベルヌーイ分布の確率を計算
            mp = (np.exp(np.dot(np.log(p), x.T) + np.dot(np.log(1-p), 1-x.T)).T * q).T
            # gmm, q, p 更新
            # pmin, qmaxで発散を防ぐ
            gmm = np.clip(mp/np.sum(mp, 0), eps, 1-eps)
            q = np.clip(np.sum(gmm, 1)/n, eps, 1-eps)
            p = np.clip((np.dot(gmm, x).T/(n*q)).T, eps, 1-eps)
            # 負の対数尤度の上界
            lp = np.dot(np.log(p), x.T) + np.dot(np.log(1-p), 1-x.T)
            uln = -np.sum(gmm*((lp.T + np.log(q)).T-np.log(gmm)))
            succ_dec = np.append((ul-uln>0) and (ul-uln<tol), succ_dec)[:succ]
            # 停止条件：減少量が連続succ回tol未満
            if all(succ_dec):
                converge_ = True
                break
            ul = uln
        # ベイズ情報量基準
        BIC = ul+0.5*(d*K+(K-1))*np.log(n)
        self.p = p
        self.q = q
        self.BIC = BIC
        self.gmm = gmm
        self.converge_ = converge_
        self.itr = itr
        return self
    
    def predict_proba(self, newx):
        """
        各クラスタへのnewxの所属確率
        """
        p = self.p
        q = self.q
        # 同時確率
        jp = np.exp(np.dot(np.log(p), newx.T) + np.dot(np.log(1-p), 1-newx.T)).T * q
        # 周辺確率
        mp = np.sum(jp, 1)
        # 条件付き確率
        cp = (jp.T/mp).T
        return cp
    
    def predict(self, newx):
        """
        newxのクラスタリング
        """
        # 条件付き確率の計算
        cp = self.predict_proba(newx)
        # クラスタ予測
        cl = np.argmax(cp, axis=1)
        return cl