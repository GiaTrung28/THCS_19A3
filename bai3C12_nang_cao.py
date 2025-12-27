import math

def luy_thua(co_so, so_mu):
    return co_so ** so_mu

def can_bac_hai(so):
    if so >= 0:
        return math.sqrt(so)
    else:
        return "Số không hợp lệ (căn bậc hai số âm)"