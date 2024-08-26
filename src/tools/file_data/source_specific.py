import json
import re


def process_aesop_to_json(file_path: str, output_path: str) -> None:
    """
    Process Aesop's Fables from Gutenbert .txt download to JSON by splitting based on 3+ newlines, extracting titles, 
    and saving as: {title, text, content} with content being the title and text concatenated. Get those morality connecting brring early I guess.

    :param file_path: Path to the .txt file for Aesop's Fables
    :param output_path: Path to the output JSON file
    :return: None
    :usage:
        >>>dataset_name = 'Aesops_Fables.txt'
        >>>dataset_path = os.path.join(data_dir, dataset_name)
        >>>output_name = 'AesopsFables.json'
        >>>output_path = os.path.join(data_dir, output_name)
        >>>process_aesop_to_json(dataset_path,output_path)
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into chunks based on 3+ newlines
    chunks = re.split(r'\n{3,}', text)

    processed_data = []

    for chunk in chunks:
        # Split each chunk into lines, process and save
        lines = chunk.strip().split('\n')

        if lines:
            title = lines[0].strip()
            content = ' '.join(lines[1:]).strip()
            processed_data.append({'title': title, 'text': content, 'content': f"{title}: {content}"})

    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(processed_data, json_file, indent=4)

    print(f"Saved processed dataset to {output_path}")
