import os
from langchain.llms import Ollama
from report_generator import generate_report
from tools.osint import run_osint
from tools.attack_simulation import adversary_simulation
from tools.exploit_generation import generate_exploit
from tools.privilege_escalation import privilege_escalation
from tools.evasion import evasion_methods
from config import TARGET

# Initialize AI Model
llm = Ollama(model="mistral")

# Define attack scenarios
tasks = {
    "OSINT": run_osint(TARGET),
    "Adversary Simulation": adversary_simulation(),
    "Exploit Generation": generate_exploit(TARGET),
    "Privilege Escalation": privilege_escalation(),
    "Evasion Techniques": evasion_methods()
}

# Generate AI-driven Red Teaming Report
generate_report(TARGET, tasks)
print("\n📄 Report Generated: security_report.pdf")
