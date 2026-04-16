from pycoingecko import CoinGeckoAPI
import time
from datetime import datetime

# Initialize CoinGecko client
cg = CoinGeckoAPI()

def get_price(coin_id="bitcoin", vs_currency="usd"):
    """Fetch current price of a coin"""
    try:
        data = cg.get_price(ids=coin_id, vs_currencies=vs_currency)
        price = data[coin_id][vs_currency]
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {coin_id.upper():<10} → ${price:,.2f} USD")
        return price
    except Exception as e:
        print(f"Error fetching {coin_id}: {e}")
        return None

def main():
    print("🚀 Crypto Price Tracker Started!")
    print("Fetching prices every 30 seconds... (Press Ctrl + C to stop)\n")
    
    coins = ["bitcoin", "ethereum", "solana"]
    
    try:
        while True:
            for coin in coins:
                get_price(coin)
            print("-" * 60)
            time.sleep(30)  # Check every 30 seconds
    except KeyboardInterrupt:
        print("\n👋 Price tracker stopped by user. Goodbye!")

if __name__ == "__main__":
    main()
