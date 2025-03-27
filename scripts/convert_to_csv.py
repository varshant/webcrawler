import pandas as pd
import json

# Load JSON output
with open("data/output.json", "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("data/product_urls.csv", index=False)

print("Output saved to data/product_urls.csv")
