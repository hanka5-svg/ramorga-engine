from ramorga.runtime import RamorgaRuntime
from ramorga.api import RamorgaAPI

# Minimalna konfiguracja
config = {
    "field": {"enabled": True},
    "meniscus": {"enabled": True},
    "modules": {"C": True, "G": True, "S": True}
}

# Inicjalizacja runtime i API
runtime = RamorgaRuntime(config)
api = RamorgaAPI(runtime)

# Minimalny krok wykonawczy
def step(user_input: str):
    """
    Minimalny krok przetwarzania:
    - opakowuje wejście użytkownika w payload
    - przekazuje do API.process()
    - zwraca wynik
    """
    payload = {"input": user_input}
    return api.process(payload)

if __name__ == "__main__":
    print(step("Hello RAMORGA"))
