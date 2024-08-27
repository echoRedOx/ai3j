from isos.types import Iso
import os
from uuid import uuid4
from datetime import datetime
from messages.actions import start_new_conversation
from vdb.chdb import chroma_get_or_create_collection, chroma_upsert_to_collection
from messages.types import Message, Turn, Conversation
from tools.utils import debug_print_function_return, stream_agent_response


"""
This is a port and update from a prior package. 
TODO: build_prompt
TODO: conversations is messy
TODO: message cache management
"""

class ChatHandler:
    """
    Do docstring stuff here.
    """

    def chat_with_iso(self, iso_name: str) -> None:
        """
        Opens a chat session and starts a new conversation with the selected agent. Chroma collection is created with agent:user nomencalture to refine results. 

        :param project: The name of the project to chat about. If None, chat about all projects.
        """

        iso = Iso(f'src/modelhub/{iso_name}.toml')

        # Start a new conversation for chat logging. TODO: ability to check existing conversations and load OR new
        conversation = start_new_conversation(host=iso.name, 
                                              host_is_bot=True, 
                                              guest=os.environ.get('USER') or os.environ.get('USERNAME'), 
                                              guest_is_bot=False)
        
        collection=chroma_get_or_create_collection(f"{iso.name}-{conversation.guest}")

        try:
            while True:
                # Get the user's request
                request = input("User>> ")

                if request == 'exit' or request == 'quit':   # Check if the user wants to exit
                    print("Exiting chat...\n\n")
                    break
                elif request == '!focus':
                    input(f"Current focus: {iso.focus}. Type a new focus message or press enter to keep this one.")
                    if input == '':
                        continue
                    else:
                        iso.change_focus(input)
                        continue
                
                # Convert to Message class
                request_message = Message(
                    uuid=str(uuid4()),
                    timestamp=str(datetime.now().strftime('%Y-%m-%d @ %H:%M')),
                    role='user',
                    speaker=conversation.guest,
                    content=request
                )

                # Build the prompt
                username = os.environ.get('USER') or os.environ.get('USERNAME')
                prompt = iso.build_prompt(request_message.content, username=username, agent_agent=False)

                #####  DEBUG: PROMPT  #####
                debug_print_function_return('Prompt', prompt)
                #####  DEBUG END  #####

                # Get the response and stream it to the terminal
                response_content = iso.generate_response(prompt=prompt)

                # Convert response to message class and pull the message string
                response_message = Message(
                    uuid=str(uuid4()),
                    timestamp=str(datetime.now().strftime('%Y-%m-%d @ %H:%M')),
                    role='assistant',
                    speaker=conversation.host,
                    content=response_content
                )

                stream_agent_response(iso.name, text=response_content, delay=.05)

                # Create turn and add to chat history
                convo_turn = Turn(
                    uuid=str(uuid4()),
                    request=request_message,
                    response=response_message
                )

                iso.message_cache.add_message(convo_turn)

                # Chroma Upsert
                document = convo_turn.request.to_memory_string()
                document += convo_turn.response.to_memory_string()
                #print(f"Documents: {document}")
                chroma_upsert_to_collection(collection=collection, metadata=None, document=document, id=convo_turn.uuid)
                

                ###  DEBUG: TURN BASE DICT  ###
                #debug_print_function_return('Turn Base Dict', convo_turn.to_dict())
                ###  DEBUG END  ###

                # Add Turn to Conversation YAML
        except KeyboardInterrupt:
            print("Interrupted by user...\n")
        
        finally:
            print("Chat session ended.")