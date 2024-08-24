import ollama


def get_response_generate(model_name, prompt):
    """Ollama-python api endpoint for generate (instruct-based)"""
    response = ollama.generate(model_name, prompt)
    print(response['response'])


def get_response_generate_stream(model_name, prompt):
    """Ollama-python api endpoint to stream response from generate (instuct-based)"""
    for part in ollama.generate(model_name, prompt, stream=True):
        print(part['response'], end='', flush=True)

        
def get_response_chat(model_name, prompt):
    """Ollama-python api endpoint for chat completion (GPT style messages)"""
    messages = [{
        'role': 'user',
        'content': prompt,
    }]
    
    response = ollama.chat(model_name, messages)
    print(response['message']['content'])
    

def get_response_chat_stream(model_name, prompt):
    """Ollama-python api endpoint to stream response from chat completion."""
    messages = [{
        'role': 'user',
        'content': prompt,
    }]
    
    for part in ollama.chat(model=model_name, messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)
    print()
