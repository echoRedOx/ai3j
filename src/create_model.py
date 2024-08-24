import toml
from string import Template
import os
from pathlib import Path
import ollama
import sys

"""This module creates a new model and adds it to the Ollama library based on a given instructions.toml file"""

def create_ollama_model(instructions_filepath):
    output_dir = './modelhub/modelfiles'
    template_modelfile = './modelhub/templates/iso.modelfile'
    iso_config = instructions_filepath
    iso_name = os.path.splitext(os.path.basename(iso_config))[0]
    output_filepath = f'{Path(output_dir, iso_name)}.modelfile'

    with open(iso_config, 'r') as config:
        config_data = toml.load(config)

    with open(template_modelfile, 'r') as template:
        content = template.read()
        template = Template(content)

    output_content = template.substitute({
        'from_model': config_data['iso']['modelfile']['from_model'],
        'num_ctx': config_data['iso']['modelfile']['num_ctx'],
        'temperature': config_data['iso']['modelfile']['temperature'],
        'num_predict': config_data['iso']['modelfile']['num_predict'],
        'system_message': config_data['iso']['modelfile']['system_message']
    })

    os.makedirs(os.path.dirname(output_dir), exist_ok=True)

    with open(output_filepath, 'w') as output:
        output.write(output_content)

    print(f"Modelfile for ( {iso_name} ) successfully saved to: {output_filepath}")

    print("Calling Ollama's create method...")

    try:
        ollama.create(model=iso_name, modelfile=output_content)
        print("Model created successfully and added to Ollama Library.")
    except Exception as e:
        print("Model creation process unsuccessful... ", e)
        

if __name__ == "__main__":
    filepath = sys.argv[1]
    create_ollama_model(filepath)