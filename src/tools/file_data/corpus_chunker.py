import nltk
import json
import sys
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')


def chunk_text(file_path: str, max_chunk_size: int, overlap_size: int, output_path: str) -> None:
    """
    Chunk text into smaller pieces based on max_chunk_size and overlap_size and save to JSON file.

    :param file_path: Path to the .txt file to be chunked
    :param max_chunk_size: Maximum number of tokens per chunk
    :param overlap_size: Number of tokens to overlap between chunks
    :param output_path: Path to the output JSON file
    :return: None
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    tokens_in_current_chunk = 0

    for sentence in sentences:
        tokens = word_tokenize(sentence)
        new_tokens_count = len(tokens)

        if tokens_in_current_chunk + new_tokens_count > max_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap_size:]
            current_chunk.extend(tokens)
            tokens_in_current_chunk = len(current_chunk)
        else:
            current_chunk.extend(tokens)
            tokens_in_current_chunk += new_tokens_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    chunk_data = {"content": chunks}
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(chunk_data, json_file, indent=4)

    print(f"Saved chunks to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python chunk_text.py <input_file> <output_file> <max_chunk_size> <overlap_size>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    max_chunk_size = int(sys.argv[3])
    overlap_size = int(sys.argv[4])

    chunk_text(input_file, max_chunk_size, overlap_size, output_file)