import numpy as np
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(12, 3))

rand_num = np.random.rand()
rand_num_std = np.random.randn()

print(rand_num)
print(rand_num_std)

rand_array = np.random.rand(5)
print(rand_array)
rand_array_std = np.random.randn(2, 4)
print(rand_array_std)

rand_int_array = np.random.randint(10, size=10)
print(rand_int_array)
rand_int_array_with_limits = np.random.randint(10, 20, size=(2, 10))
print(rand_int_array_with_limits)

axes[0].hist(np.random.rand(10000))
axes[0].set_title('rand')
axes[1].hist(np.random.randn(10000))
axes[1].set_title('randn')
axes[2].hist(np.random.randint(low=1, high=10, size=10000), bins=9, align='left')
axes[2].set_title('randint(low=1, high=10')
plt.show()

# Using random seed
np.random.seed(123456789)
number_1 = np.random.rand()
print(number_1)
number_2 = np.random.rand()
print(number_2)
np.random.seed(123456789)
number_3 = np.random.rand()
print(number_3)

prng = np.random.RandomState(123456789)
rand_arr_1 = prng.randn(2, 3)
print(rand_arr_1)
rand_arr_2 = prng.randn(2, 3)
print(rand_arr_2)

chisquare = prng.chisquare(1, size=(2, 2))
print(chisquare)

standard_t = prng.standard_t(1, size=(2, 3))
print(standard_t)

f = prng.f(5, 2, size=(2, 4))
print(f)

binomial = prng.binomial(10, 0.5, size=10)
print(binomial)

poisson = prng.poisson(5, size=10)
print(poisson)



