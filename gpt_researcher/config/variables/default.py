from .base import BaseConfig

DEFAULT_CONFIG: BaseConfig = {
    "RETRIEVER": "exa",
    "EMBEDDING": "openai:text-embedding-3-large",
    "SIMILARITY_THRESHOLD": 0.42,
    "FAST_LLM": "openai:chatgpt-4o-latest",
    "SMART_LLM": "openai:chatgpt-4o-latest",
    "STRATEGIC_LLM": "openai:o1-preview", # Can be used with gpt-o1
    "FAST_TOKEN_LIMIT": 4000,
    "SMART_TOKEN_LIMIT": 6000,
    "STRATEGIC_TOKEN_LIMIT": 5000,
    "BROWSE_CHUNK_MAX_LENGTH": 16384,
    "CURATE_SOURCES": False,
    "SUMMARY_TOKEN_LIMIT": 1000,
    "TEMPERATURE": 0.5,
    "LLM_TEMPERATURE": 0.7,
    "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "MAX_SEARCH_RESULTS_PER_QUERY": 5,
    "MEMORY_BACKEND": "local",
    "TOTAL_WORDS": 4000,
    "REPORT_FORMAT": "APA",
    "MAX_ITERATIONS": 4,
    "AGENT_ROLE": None,
    "SCRAPER": "browser",
    "MAX_SUBTOPICS": 5,
    "LANGUAGE": "english",
    "REPORT_SOURCE": "web",
    "DOC_PATH": "./my-docs"
}
