import json
import openai
from pathlib import Path
from typing import List, Tuple

def check_text_detailed(fp: Path, max_tokens: int) -> List[Tuple[int, str]]:
    """
    Splits the text of a file into chunks based on a specified maximum token count.

    Parameters:
    - fp (Path): Path to the file to be processed.
    - max_tokens (int): Maximum number of tokens for each chunk (considering approx. 4 words per token).

    Returns:
    - List[Tuple[int, str]]: A list of tuples where each tuple contains the starting index of the chunk
      and the chunk text itself.
    """
    doc = fp.read_text(encoding='utf-8').lower()
    words = doc.split()
    chunk_size = max_tokens // 4  # Estimate words per token
    matching_chunks = []

    for start_idx in range(0, len(words), chunk_size):
        chunk = ' '.join(words[start_idx:start_idx + chunk_size])
        matching_chunks.append((start_idx, chunk))

    return matching_chunks

def check_with_openai(chunks: List[Tuple[int, str]], model: str, system_prompt: str, openai_api_key: str) -> List[Tuple[int, str, List[dict]]]:
    """
    Processes text chunks with GPT-3.5 to identify relevant documents based on the given prompt.

    Parameters:
    - chunks (List[Tuple[int, str]]): List of text chunks to be processed.
    - model (str): The OpenAI GPT model to be used.
    - system_prompt (str): The prompt to be used for querying the GPT model.
    - openai_api_key (str): The API key for OpenAI.

    Returns:
    - List[Tuple[int, str, List[dict]]]: A list of tuples where each tuple contains the starting index of the chunk,
      the chunk text, and a list of 'claims' extracted from the chunk.
    """
    client = openai.OpenAI(api_key=openai_api_key)
    relevant_documents = []

    for start_index, chunk in chunks:
        try:
            response = client.Completion.create(
                model=model,
                prompt=system_prompt + "\n\n" + chunk,
                max_tokens=150  # Adjust as necessary
            )
            as_json = json.loads(response.choices[0].text)
            if as_json.get("claims"):
                relevant_documents.append((start_index, chunk, as_json["claims"]))
        except Exception as e:
            print(f"Failed on chunk starting at {start_index} with error: {e}")
            continue

    return relevant_documents

def check_doc_with_openai(doc: str, model: str, system_prompt: str, openai_api_key: str) -> List[dict]:
    """
    Validates claims in a document using GPT-4 based on a given prompt.

    Parameters:
    - doc (str): The document text to be processed.
    - model (str): The OpenAI GPT model to be used (GPT-4).
    - system_prompt (str): The prompt to be used for querying the GPT model.
    - openai_api_key (str): The API key for OpenAI.

    Returns:
    - List[dict]: A list of 'claims' extracted from the document.
    """
    client = openai.OpenAI(api_key=openai_api_key)

    try:
        response = client.Completion.create(
            model=model,
            prompt=system_prompt + "\n\n" + doc,
            max_tokens=300  # Adjust as necessary
        )
        as_json = json.loads(response.choices[0].text)
        return as_json.get("claims", [])
    except Exception as e:
        print(f"Failed with error: {e}")
        return None
