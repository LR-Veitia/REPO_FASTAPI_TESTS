import nox


@nox.session
def tests(session):
    # Instalar las dependencias desde requirements.txt
    session.install("-r", "requirements.txt")

    # Ejecutar los tests con pytest
    session.run("pytest", "--html=report.html")

    # Si quieres formatear el código con black después de ejecutar los tests, puedes hacerlo así:
    session.run("black", ".")
