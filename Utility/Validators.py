from wtforms.validators import ValidationError

"""Integer validator
   -----------------
   Its a form validator. Checks if a form value is an integer."""
def integerValidator(form, field):
    errorMsg = 'Das Feld muss eine Ganzzahl enthalten.'
    try:
        intVal = int(field.data)
        floatVal = float(field.data)
    except ValueError:
        raise ValueError(errorMsg)
    difference = floatVal - intVal
    if not difference == 0:
        raise ValidationError(errorMsg)
