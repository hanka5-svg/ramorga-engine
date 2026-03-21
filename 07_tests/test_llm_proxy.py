from ramorga.integration.llm_proxy import LLMProxy

class MockLLM:
    def generate(self, prompt):
        return f"MOCK_RESPONSE: {prompt}"

def test_llm_proxy():
    proxy = LLMProxy(llm=MockLLM())
    out = proxy.send("Hello")
    assert "MOCK_RESPONSE" in out
