from datasets import Dataset
import os
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
import concurrent.futures

def process_arrow_file(args):
    directory, filename, output_file, vocab = args
    file_path = os.path.join(directory, filename)

    try:
        # Preload dataset
        dataset = Dataset.from_file(file_path)
        characters = set()
        with open(output_file, "a", encoding="utf-8") as outfile:
            for item in dataset:
                text = item["text"]  # Extract text field
                if text:
                    outfile.write(text + "\n")
                    characters.update(text)
        return characters
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return set()

def arrow_files_in_dir(directory):
    return [
        filename
        for filename in os.listdir(directory)
        if filename.endswith(".arrow") and os.path.isfile(os.path.join(directory, filename))
    ]

def process_files_in_parallel(files, folder_path, output_file):
    vocab = set()
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        args = [(folder_path, filename, output_file, vocab) for filename in files]
        for characters in tqdm(executor.map(process_arrow_file, args), total=len(files)):
            vocab.update(characters)
    return vocab

if __name__ == "__main__":
    folder_path = "C:/Users/Username/.cache\huggingface/datasets/openwebtext/plain_text/1.0.0/6f68e85c16ccc770c0dd489f4008852ea9633604995addd0cd76e293aed9e521"  # Path to directory containing Arrow files
    output_file_train = "train_split.txt"
    output_file_val = "val_split.txt"
    vocab_file = "vocab.txt"

    # Get Arrow files
    files = arrow_files_in_dir(folder_path)
    total_files = len(files)
    split_index = int(total_files * 0.9)
    files_train = files[:split_index]
    files_val = files[split_index:]

    # Clear output files
    open(output_file_train, "w").close()
    open(output_file_val, "w").close()

    # Process training files
    print("Processing training files...")
    vocab_train = process_files_in_parallel(files_train, folder_path, output_file_train)

    # Process validation files
    print("Processing validation files...")
    vocab_val = process_files_in_parallel(files_val, folder_path, output_file_val)

    # Combine vocabularies and save
    vocab = vocab_train.union(vocab_val)
    with open(vocab_file, "w", encoding="utf-8") as vfile:
        for char in sorted(vocab):
            vfile.write(char + "\n")

    print("Processing complete.")
