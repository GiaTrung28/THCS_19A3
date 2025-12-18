def dao_nguoc_dictionary(input_dict):
    
    dao_nguoc_dict = {}
    for key in input_dict:
        value = input_dict[key]
        dao_nguoc_dict[value] = key
        
    return dao_nguoc_dict

cap_doi = {
    'apple': 'fruit',
    'carrot': 'vegetable',
    'python': 'language'
}
inverted_dict = dao_nguoc_dictionary(cap_doi)
print(f"Dictionary gốc: {cap_doi}")
print(f"Dictionary đảo ngược: {inverted_dict}")