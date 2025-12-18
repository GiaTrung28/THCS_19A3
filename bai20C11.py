def loc_dictionary_theo_dieu_kien(input_dict, nguong_gia_tri):
    
    dict_loc = {}
    for key, value in input_dict.items():
        if value > nguong_gia_tri:
            dict_loc[key] = value
            
    return dict_loc

data_values = {
    'item1': 45,
    'item2': 60,
    'item3': 12,
    'item4': 75
}
threshold = 50
filtered_dict = loc_dictionary_theo_dieu_kien(data_values, threshold)
print(f"Dictionary gốc: {data_values}")
print(f"Dictionary sau khi lọc (giá trị > {threshold}): {filtered_dict}")