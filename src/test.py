from isos.types import Iso
from isos.actions import get_response_generate_stream

iso = Iso('src/modelhub/marvin.toml')
print(":::  Modelfile  :::")
print(iso.modelfile)
print(":::  Parameters  :::")
print(iso.parameters)
print(iso.prompt_template)

get_response_generate_stream(iso.name.lower(), "Why is the sky blue?")