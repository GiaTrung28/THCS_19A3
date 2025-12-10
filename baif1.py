def chuyen_doi_nhiet_do(do_c):
    do_f = (do_c * 9/5) + 32
    return do_f


nhiet_do_celsius = 25
nhiet_do_fahrenheit = chuyen_doi_nhiet_do(nhiet_do_celsius)
print(f"{nhiet_do_celsius} độ C tương ứng với {nhiet_do_fahrenheit} độ F")
