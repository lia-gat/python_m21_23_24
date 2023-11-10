def number_in_english(number):
    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    decades = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if number < 10:
        return units[number]
    elif number < 20:
        return tens[number % 10]
    elif number < 100:
        return decades[number // 10] + ' ' + units[number % 10]
    elif number < 1000:
        if number % 100 == 0:
            return units[number // 100] + ' hundred'
        else:
            return units[number // 100] + ' hundred and ' + number_in_english(number % 100)
    
    
print(number_in_english(3))

print(number_in_english(78))

print(number_in_english(115))

print(number_in_english(729))    

print(number_in_english(0).lower())

print(number_in_english(1).lower())