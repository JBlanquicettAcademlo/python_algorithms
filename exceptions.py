#try
#except
#else
#finally
#raise

# try: 
#     print(1/0)
# except ZeroDivisionError:
#     print('No se puede dividir entre cero.')
# else:
#     print('No se genero exception!!')
# finally:
#     print("siempre se ejecuta")

class AcademloStudentSleepingError(Exception):

    def __init__(self) -> None:
        super().__init__("Se ejecuta cuando un estudiante de academlo se esta durmiendo")

if 5 > 8:
    print('wow')
else: 
    raise AcademloStudentSleepingError