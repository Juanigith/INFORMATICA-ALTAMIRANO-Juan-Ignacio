nota = int(input("¿Qué nota sacaste?: "))
asistencia = int(input("¿Qué porcentaje de asistencia tenés?: "))
if nota > 10:
    print("Error, las notas van del 0-10")
elif asistencia > 100:
        print("Error, el procentaje de asistencia va del 0% al 100%")
elif nota == 10:
    print("¡Sobresaliente!")
    if asistencia >= 90:
        print("¡Promocionado!")
elif nota >= 8:
    print("Muy bien")
    if asistencia >= 90:
        print("¡Promocionado!")
elif nota >= 6:
    print("Aprobado")
    if asistencia < 90:
        print("Regular")
else:
    print("Desaprobado")