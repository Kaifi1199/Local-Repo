import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_chart(file_path):
    """
    Reads data from a CSV file and plots a bar chart.
    """
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        
        # Check if the required columns exist
        if 'Name' in data.columns and 'Age' in data.columns:
            # Plotting a bar chart
            plt.figure(figsize=(8, 6))
            plt.bar(data['Name'], data['Age'], color='skyblue')
            plt.xlabel('Name')
            plt.ylabel('Age')
            plt.title('Age of Individuals')
            plt.tight_layout()
            plt.show()
        else:
            print("Error: Required columns ('Name', 'Age') are missing in the dataset.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the local dataset
    file_path = "datasets/local_dataset.csv"
    plot_chart(file_path)
