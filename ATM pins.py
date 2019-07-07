def validate_pin(pin):
    if((len(pin) == 4)|(len(pin) == 6)) & ((pin.isdigit())):
        return(True)
    
    return(False)
print(validate_pin("1111"))
