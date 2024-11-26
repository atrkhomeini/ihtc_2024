import os
import json
#---------------------------------------------------------------------------------------------------
# read all data from the file .json
#---------------------------------------------------------------------------------------------------
def read_all_json_files(directory):
    json_files_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                json_files_data.append(data)
    return json_files_data

# read test.json
directory_path = 'ihtc2024_test_dataset'
all_json_data_test = read_all_json_files(directory_path)
all_json_data_test[0]

# read solution.json
directory_path = '../ihtc2024_test_solutions/ihtc2024_test_solutions'
all_json_data_sol = read_all_json_files(directory_path)
all_json_data_sol[0]

#-------------------------------------------------------------------------------------------
# The Objective
#-------------------------------------------------------------------------------------------
# room age mix
num_rooms = len(all_json_data_test[0]['rooms'])
# num of days
num_days = all_json_data_test[0]['days']

# Initialize room_age_mix with sets for each room and day
room_age_mix = [[set() for _ in range(num_rooms)] for _ in range(num_days)]

# Loop through each patient and add their age group to the corresponding room and day
i = 0
for patient in all_json_data_sol[0]['patients']:
    if patient['admission_day'] != 'none':
        d = int(patient['admission_day'])
        r = int(patient['room'][1:])        
        # Check if d and r are within the bounds of room_age_mix
        if d < num_days and r < num_rooms:
            age = all_json_data_test[0]['patients'][i]['age_group']
            room_age_mix[d][r].add(age)
            print(i, d, r, age)
        else:
            print(f"Index out of range: day {d}, room {r}")
    i += 1

# Print the resulting room_age_mix
print(room_age_mix)