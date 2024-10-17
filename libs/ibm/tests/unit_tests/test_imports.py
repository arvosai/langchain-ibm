from langchain_ibm import __all__

EXPECTED_ALL = ["WatsonxLLM", "WatsonxEmbeddings", "ChatWatsonx", "WatsonxRerank"]


def test_all_imports() -> None:
    assert sorted(EXPECTED_ALL) == sorted(__all__)
