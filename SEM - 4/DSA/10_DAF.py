import os

def insert_record(file_path, record):
    with open(file_path, 'a') as file:
        file.write(record + '\n')
    print("Record inserted successfully.")

def delete_record(file_path, record):
    temp_file_path = file_path + '.temp'

    with open(file_path, 'r') as file, open(temp_file_path, 'w') as temp_file:
        for line in file:
            if line.strip() != record:
                temp_file.write(line)

    os.remove(file_path)
    os.rename(temp_file_path, file_path)

    print("Record deleted successfully.")

# Example usage
file_path = '10DAFdb.txt'

# Insert records
insert_record(file_path, "Record 1")
insert_record(file_path, "Record 2")
insert_record(file_path, "Record 3")

# Delete a record
delete_record(file_path, "Record 2")
