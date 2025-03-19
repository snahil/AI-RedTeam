from langchain.llms import Ollama

llm = Ollama(model="mistral")

def adversary_simulation():
    attack_scenario = """
    You are a Red Team operator. Plan an advanced attack simulation:
    1. Initial Access: Phishing, Weak Credentials
    2. Command & Control (C2) Setup
    3. Lateral Movement: Pass-the-Hash, SSH Key Theft
    4. Data Exfiltration: Cloud API key theft
    5. Persistence: Rootkit, Hidden Cron Jobs
    """
    return llm.invoke(attack_scenario)
