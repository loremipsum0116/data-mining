import pandas as pd

data = {
    "MacBook Pro 16": ["CPU", "GPU", "RAM", "SSD"],
    "사양": ["18-core CPU", "20-core GPU", "48GB Unified Memory", "1TB SSD"],
    "비교제품군": [
        "Intel Core Ultra 9",
        "NVIDIA GeForce RTX 5070",
        "48GB LPDDR5X",
        "1TB NVMe SSD",
    ],
}

matrix = pd.DataFrame(data)
print(matrix)
print()
print(matrix["MacBook Pro 16"])
print()
print(matrix.head(2))
