import re

def extract_data(text):
    data = {}

    # Regular expressions for each field
    patterns = {
        'SYMBOL': r"\$\s?([A-Z0-9]{3,10})",
        'NAME': r"\?\? (.+?) \|",
        'TRADING_VOLUME': r"Trading volume: \$(\d{1,3}(?:,\d{3})*(?:\.\d+)?)",
        'LIQUIDITY': r"Lp: \$(\d{1,3}(?:,\d{3})*(?:\.\d+)?)",
        'DEV_WALLET': r"Dev Wallet: (\d+)%",
        'HOLDERS': r"Holders: (\d+)",
        'MARKETCAP': r"Marketcap: \$(\d{1,3}(?:,\d{3})*(?:\.\d+)?)",
        'AGE': r"Age: (\d+h:\d+m)",
        'TOP_10_HOLD': r"T/10 hold: (\d+\.\d+%)",
        'MINT': r"Mint: ([A-Za-z0-9]{44})",
        'CA': r"([A-Za-z0-9]{44})",
    }

    # Process of extracting data
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            data[key] = match.group(1)

    # Calculate liquidity and trading volume ratio to market capitalization
    if 'liquidity' in data and 'marketcap' in data:
        liquidity = float(data['liquidity'].replace(',', '').replace('$', ''))
        marketcap = float(data['marketcap'].replace(',', '').replace('$', ''))
        data['liquidity_to_marketcap_ratio'] = liquidity / marketcap
        data['trading_volume_to_marketcap_ratio'] = float(
            data['trading_volume'].replace(',', '').replace('$', '')) / marketcap

    return data
