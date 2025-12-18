def tach_tuple_chan_le(input_tuple):
    
    tuple_chan = ()
    tuple_le = ()
    tong_chan = 0
    tong_le = 0

    for so in input_tuple:
        if so % 2 == 0:
            tuple_chan = tuple_chan + (so,) 
            tong_chan += so
        else:
            tuple_le = tuple_le + (so,)
            tong_le += so
            
    return tuple_chan, tuple_le, tong_chan, tong_le

data_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
chan, le, sum_chan, sum_le = tach_tuple_chan_le(data_tuple)
print(f"Tuple gốc: {data_tuple}")
print(f"Tuple chẵn: {chan}, Tổng chẵn: {sum_chan}") 
print(f"Tuple lẻ: {le}, Tổng lẻ: {sum_le}") 