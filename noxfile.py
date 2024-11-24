import nox  


# Instalar dependencias desde requirements.txt
@nox.session
def install_from_requirements(session):
    """
    Instala las dependencias definidas en requirements.txt.
    """
    session.run("pip", "install", "-r", "requirements.txt")


# Ejecutar todas las pruebas
@nox.session
def run_tests(session):
    """
    Ejecuta las pruebas con pytest y genera un reporte HTML.
    """
    # Ejecutar pruebas con pytest
    session.run("pytest", "--html=report.html")


# Linting y formateo del código con black
@nox.session
def lint_and_format(session):
    """
    Realiza el formateo y linting del código con black.
    """
    session.run("black", ".")


# Probar distintas versiones de Python
@nox.session(python=["3.8", "3.9", "3.10"])
def tests_on_versions(session):
    """
    Ejecuta pruebas en diferentes versiones de Python.
    """
    session.run("pytest")



