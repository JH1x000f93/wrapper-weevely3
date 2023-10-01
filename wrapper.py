import io
import sys
from core.sessions import SessionURL, SessionFile
from core.terminal import Terminal
from core import modules
from core import generate

class WeevelyWrapper:
    def __init__(self, url=None, password=None, session_path=None):
        self.url = url
        self.password = password
        self.session_path = session_path

    def generate_agent(self, password, path, obfuscator='phar', agent='obfpost_php'):
        obfuscated = generate.generate(
            password=password,
            obfuscator=obfuscator,
            agent=agent
        )
        generate.save_generated(obfuscated, path)

        return path  # Opcionalmente, puedes retornar la ruta donde se guardó el agente.


    def run_command(self, url, password, cmd):
        session = SessionURL(url=url, password=password)
        modules.load_modules(session)

        # Capturar la salida estándar
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            terminal = Terminal(session)
            terminal.onecmd(cmd)
            result = new_stdout.getvalue().strip()
        finally:
            sys.stdout = old_stdout

        return result
