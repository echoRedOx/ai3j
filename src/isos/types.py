import toml


class Iso:
    name: str
    description: str
    iso_config: str
    instructions: dict
    modelfile: dict
    parameters: dict
    
    from_model: str
    num_ctx: int
    num_predict: int
    temperature: float
    system_message: str
    
    focus: str
    prompt_template: str
    
    def __init__(self, iso_config):
        """On init, loads from config toml file to establish local vars for fine-tuning."""
        self.iso_config = iso_config
        
        with open(self.iso_config, 'r') as config:
            self.instructions = toml.load(config)
        
        self.modelfile = self.instructions['iso']['modelfile']
        self.parameters = self.instructions['iso']['parameters']
        
        self.name = self.instructions['iso']['name']
        self.from_model = self.instructions['iso']['modelfile']['from_model']
        self.num_ctx = self.instructions['iso']['modelfile']['num_ctx']
        self.num_predict = self.instructions['iso']['modelfile']['num_predict']
        self.temperature = self.instructions['iso']['modelfile']['temperature']
        self.system_message = self.instructions['iso']['modelfile']['system_message']
        self.focus = self.instructions['iso']['focus']
        self.prompt_template = self.instructions['iso']['prompt_template']

    def update_system_message(self, new_system_message):
        """Reads in the instructions.toml file, updates the system message and writes back to file. This will allow hot-reloading of model messages to possibly add a method for self-correction/learning."""
        self.system_message = new_system_message
        
        with open(self.iso_config, 'r') as config:
            config_data = toml.load(config)
        
        config_data['iso']['modelfile']['system_message'] = self.system_message
        
        with open(self.iso_config, 'w') as file:
            toml.dump(config_data, file)
        
        print(f"{self.name}'s system message has been updated to: {self.system_message}")
        
    
    def change_focus(self, new_focus):
        """Reads in the instructions.toml file, updates the model's and writes back to file."""
        self.focus = new_focus
        
        with open(self.iso_config, 'r') as config:
            config_data = toml.load(config)
        
        config_data['iso']['focus'] = self.focus
        
        with open(self.iso_config, 'w') as file:
            toml.dump(config_data, file)
        
        print(f"{self.name}'s focus has been updated to: {self.system_message}")
    
    def change_temperature(self):
        pass