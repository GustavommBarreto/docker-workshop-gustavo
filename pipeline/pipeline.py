import sys

import pandas as pd

print("arguments", sys.argv)

day = int(sys.argv[1])

df = pd.DataFrame({"mes": [1, 2], "num_passengers": [3, 4]})
df["day"] = day
print(df.head())

df.to_parquet(f"/tmp/pipeline_day_{day}.parquet", index=False)

print(f"Running pipeline for day {day}")