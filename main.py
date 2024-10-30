def int_to_roman(number):
    # Liste des valeurs et symboles romains, du plus grand au plus petit
    val_to_roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roman_numeral = ""
    # Pour chaque valeur et symbole romain dans la liste
    for value, symbol in val_to_roman:
        # Tant que le nombre est supérieur ou égal à la valeur actuelle
        while number >= value:
            roman_numeral += symbol
            number -= value
    
    return roman_numeral
