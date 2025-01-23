# Project Files Overview

This project contains the implementation of a GPT-style language model using PyTorch. Below is a detailed explanation of each file and folder:

---

## **Main Files**

- **`cudo_gpt.ipynb`**  
  This is the main notebook for training and testing the GPT model.  
  - It includes the model architecture, training loop, evaluation, and text generation functionality.

- **`bigram.ipynb`**  
  A notebook for testing a simple bigram model.  
  - Serves as a baseline to understand basic language modeling before implementing the GPT architecture.

---

## **Dataset Management**

- **`download.py`**  
  A script to download the OpenWebText dataset from Hugging Face.  
  - Saves the dataset to a specified folder.  
  - Alternatively, the dataset can be cloned directly from Hugging Face using the following command:
    ```bash
    git clone https://huggingface.co/datasets/Skylion007/openwebtext
    ```

- **`extractor.py`**  
  A script to process the downloaded OpenWebText dataset.  
  - Splits the data into `train_split.txt` and `val_split.txt` files.  
  - Generates the `vocab.txt` file, which contains unique characters in the dataset.

- **`vocab.txt`**  
  A text file containing the vocabulary (unique characters) extracted from the dataset.  
  - This is used for encoding and decoding text during training and inference.

---

## **Additional Files**

- **`wizard_of_oz.txt`**  
  A text file containing the "Wizard of Oz" book.  
  - This is used as a sample dataset to train and test the bigram model in `bigram.ipynb`.

---

## **Folders**

- **`openwebtext`**  
  This folder contains the OpenWebText dataset in Arrow format.  
  - If the folder is not present, clone the dataset using the following command:
    ```bash
    git clone https://huggingface.co/datasets/Skylion007/openwebtext
    ```

---

## **Usage**

1. **Clone the Dataset**  
   - Use the following command to clone the OpenWebText dataset:  
     ```bash
     git clone https://huggingface.co/datasets/Skylion007/openwebtext
     ```

2. **Download the Dataset**  
   - Run the `download.py` script after cloning the dataset repository.

3. **Process the Dataset**  
   - Use the `extractor.py` script to split the dataset into `train_split.txt` and `val_split.txt`, and generate the `vocab.txt` file.

4. **Test the Bigram Model**  
   - Run `bigram.ipynb` to train and test a simple bigram model as a baseline.

5. **Train the GPT Model**  
   - Use `cudo_gpt.ipynb` to train the GPT model on the processed dataset.

---

## **Hyperparameters**

Due to the lack of a CUDA-enabled GPU on my local computer, the following hyperparameters were used. These should be adjusted when running on a GPU-enabled environment to achieve better performance and a lower loss function:

- **`max_iters`**: `200`  
- **`eval_iters`**: `100`

---

For any questions or additional details, feel free to reach out!
