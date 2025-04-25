from utils.llm_config import load_llm

def get_writer_agent():
        # Simply return the loaded LLM without using the agent
        return load_llm()
