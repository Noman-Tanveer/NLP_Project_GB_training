
import json

with open('valid_freq.json') as json_file:
    val_data = json.load(json_file)

print(type(val_data))
print(val_data["t_57f631fa-c4a2-44e3-aa8e-bda438649e03"])
