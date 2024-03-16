import numpy as np
import jax.numpy as jnp
import matplotlib.pyplot as plt

from jax import random

N = 2
H = 3
T = 20

dh = jnp.ones((N, H))

# random.seed(3)
random.key(3)

# 勾配爆発
Wh = np.random.randn(H, H)
# 勾配消失
# Wh = np.random.randn(H, H) * 0.5

norm_list = []
for t in range(T):
    dh = jnp.dot(dh, Wh.T)
    norm = jnp.sqrt(jnp.sum(dh**2)) / N
    norm_list.append(norm)

print(norm_list)

plt.plot(jnp.arange(len(norm_list)), norm_list)
plt.xticks([0, 4, 9, 14, 19], [1, 5, 10, 15, 20])
plt.xlabel('time step')
plt.ylabel('norm')
plt.show()