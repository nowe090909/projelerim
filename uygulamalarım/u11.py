#bir dizedeki boslukları kaldıran pyton programı yazınız

def bosluklari_kaldir(dizi):
    """
    Verilen dizideki boşlukları kaldıran bir fonksiyon.
    
    Args:
    dizi (str): Boşlukları kaldırılacak dize.
    
    Returns:
    str: Boşlukları kaldırılmış dize.
    """
    return "".join(dizi.split())

# Örnek kullanım
dizi = "Bu bir örnek cümle"
print(bosluklari_kaldir(dizi))
