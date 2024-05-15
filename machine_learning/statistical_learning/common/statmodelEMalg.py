import numpy as np

class EMmixBernoulli:

    def __init__(self, K=5, maxitr=1000, tol=1e-5, succ=3):
        self.K = K
        self.maxitr = maxitr
        self.tol = tol
        self.succ = succ

    def fit(self, x):
        K = self.K
        maxitr = self.maxitr
        tol = self.tol
        succ = self.succ
        n, d = x.shape
        eps = np.finfo(float).eps
        mu = np.mean(x)
        p = np.random.beta(mu, 1-mu, size=K*d).reshape(K, d)
        q = np.repeat(1/K,K)
        ul = np.inf
        converge_ = False
        succ_dec = np.repeat(False, succ)
        for itr in np.arange(maxitr):
            mp = (np.exp(np.dot(np.log(p), x.T) + np.dot(np.log(1-p), 1-x.T)).T * q).T
            gmm = np.clip(mp/np.sum(mp, 0), eps, 1-eps)
            q = np.clip(np.sum(gmm, 1)/n, eps, 1-eps)
            p = np.clip((np.dot(gmm, x).T/(n*q)).T, eps, 1-eps)
            lp = np.dot(np.log(p), x.T) + np.dot(np.log(1-p), 1-x.T)
            uln = -np.sum(gmm*((lp.T + np.log(q)).T-np.log(gmm)))
            succ_dec = np.append((ul-uln>0) and (ul-uln<tol), succ_dec)[:succ]
            if all(succ_dec):
                converge_ = True
                break
            ul = uln
        BIC = ul+0.5*(d*K+(K-1))*np.log(n)
        self.p = p
        self.q = q
        self.BIC = BIC
        self.gmm = gmm
        self.converge_ = converge_
        self.itr = itr
        return self
    
    def predict_proba(self, newx):
        p = self.p
        q = self.q
        jp = np.exp(np.dot(np.log(p), newx.T) + np.dot(np.log(1-p), 1-newx.T)).T * q
        mp = np.sum(jp, 1)
        cp = (jp.T/mp).T
        return cp
    
    def predict(self, newx):
        cp = self.predict_proba(newx)
        cl = np.argmax(cp, axis=1)
        return cl