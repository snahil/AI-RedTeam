import requests
from langchain.llms import Ollama
from config import SHODAN_API_KEY, HAVEIBEENPWNED_API_KEY

llm = Ollama(model="mistral")

def run_osint(target):
    print(f"\n🔹 Running OSINT on {target}...")

    # Shodan API lookup
    shodan_url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={target}"
    shodan_response = requests.get(shodan_url).json()

    # Check breached credentials
    hibp_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{target}"
    hibp_response = requests.get(hibp_url, headers={"hibp-api-key": HAVEIBEENPWNED_API_KEY}).json()

    osint_results = {
        "Shodan Data": shodan_response,
        "Breached Credentials": hibp_response
    }

    return llm.invoke(f"Analyze OSINT data for {target}: {osint_results}")
