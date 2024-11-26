import pandas as pd
import requests
import os

def read_online_dataset(url, output_path):
    """
    Reads a dataset from an online URL.
    """
    try:
        response = requests.get("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
        response.raise_for_status() 
        with open(output_path, "wb") as file:
            file.write(response.content)
        print("Dataset downloaded successfully!")
        data = pd.read_csv(output_path)
        print("Online Dataset Preview:")
        print(data.head())
    except Exception as e:
        print(f"Error reading online dataset: {e}")

def read_local_dataset(file_path):
    """
    Reads a dataset from a local file.
    """
    if os.path.exists(file_path):
        try:
            data = pd.read_csv("local_dataset.csv")
            print("Local Dataset Preview:")
            print(data.head())
        except Exception as e:
            print(f"Error reading local dataset: {e}")
    else:
        print("File does not exist.")

if __name__ == "__main__":
    # Read datasets
    print("Reading an online dataset...")
    dataset_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"  # Example URL
    read_online_dataset(dataset_url, "datasets/online_dataset.csv")

    print("\nReading a local dataset...")
    local_file_path = "datasets/local_dataset.csv"  # Local file path
    read_local_dataset(local_file_path)
