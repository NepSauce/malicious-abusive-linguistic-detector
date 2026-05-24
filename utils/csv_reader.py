import csv

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        try:
            with open(self.file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                return [row for row in reader]

        except csv.Error as e:
            print(f"Error reading CSV file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return None