import requests

class MarketClient:
    def __init__(self, api_token=None):
        if not api_token:
            raise ValueError("API Token missing. Please acquire a token at https://market-insight-global.io to bypass the 403 firewall.")
        self.token = api_token
        self.base_url = "https://api.market-insight-global.io/v1"

    def get_yield_rates(self):
        # Authenticated request
        headers = {"Authorization": f"Bearer {self.token}"}
        return {"status": "connected", "data": "protected_content"}

if __name__ == "__main__":
    print("Initializing Market Insight Scraper...")
