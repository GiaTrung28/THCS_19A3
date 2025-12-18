def tim_key_max_value(input_dict):
    
    max_value = None
    key_max = None

    for key in input_dict:
        current_value = input_dict[key]
        if max_value is None or current_value > max_value:
            max_value = current_value
            key_max = key
            
    return key_max, max_value

scores = {
    'An': 8.5,
    'Binh': 9.0,
    'Chau': 7.5,
    'Duc': 9.0
}
best_student, best_score = tim_key_max_value(scores)
print(f"Dictionary điểm số: {scores}")
print(f"Key có giá trị lớn nhất là: '{best_student}' với giá trị {best_score}")