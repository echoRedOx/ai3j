import os
from typing import List
import toml

def parse_directory(directory: str) -> List[str]:
    isos = []
    
    for filename in os.listdir(directory):
        if filename.endswith(".toml"):
            filepath = os.path.join(directory, filename)
            model_data = toml.load(filepath)
            
            name = model_data["iso"]["name"]
            description = model_data["iso"].get("description", "None provided...")
            from_model = model_data["iso"]["modelfile"]["from_model"]
            isos.append({"name": name, "description": description, "base_model": from_model})
            
    return isos



if __name__ == "__main__":
    list = parse_directory("src/modelhub")
    print(list)