from runtime import RamorgaRuntime
from ramorga.api import RamorgaAPI

# Minimalna konfiguracja
config = {
    "field": {"enabled": True},
    "meniscus": {"enabled": True},
    "modules": {"C": True, "G": True, "S": True}
}

runtime = RamorgaRuntime(config)
api = RamorgaAPI(runtime)

# Minimalny krok wykonawczy
def step(user_input: str):
    return api.process({"input": user_input})

if __name__ == "__main__":
    print(step("Hello RAMORGA"))
