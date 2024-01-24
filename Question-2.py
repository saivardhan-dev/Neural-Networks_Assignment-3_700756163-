import numpy as np

random_vector = np.random.uniform(1, 20, 20)

reshaped_array = random_vector.reshape((4, 5))

reshaped_array[np.arange(4), np.argmax(reshaped_array, axis=1)] = 0

print("Original Random Vector:")
print(random_vector)
print("\nReshaped 4x5 Matrix:")
print(reshaped_array)
