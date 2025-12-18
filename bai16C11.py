def dem_tan_suat_ky_tu(chuoi):
    
    tan_suat_dict = {}
    for ky_tu in chuoi:
        if ky_tu in tan_suat_dict:
            tan_suat_dict[ky_tu] += 1
        else:
            tan_suat_dict[ky_tu] = 1
            
    return tan_suat_dict

input_str_16 = "lap trinh python co ban"
freq_dict = dem_tan_suat_ky_tu(input_str_16)
print(f"Chuỗi đầu vào: '{input_str_16}'")
print(f"Tần suất ký tự: {freq_dict}")