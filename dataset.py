import pandas as pd
import random

n = 100

data = []

for i in range(n):
    name = f"Personne_{i}"
    age = random.randint(15, 60)

    data.append([i, name, age])

df = pd.DataFrame(data, columns=["id", "name", "age"])
df.to_csv("dataset_people.csv", index=False)

print("Dataset généré ✔")