from isos.types import Iso

iso = Iso('src/modelhub/marvin.toml')
print(":::  Modelfile  :::")
print(iso.modelfile)
print(":::  Parameters  :::")
print(iso.parameters)
print(iso.prompt_template)
