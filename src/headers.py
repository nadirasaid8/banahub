from src.agent import generate_random_user_agent

def headers():
    return {
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://banana.carv.io',
            'Referer': 'https://banana.carv.io/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'priority': 'u=1, i',
            'sec-fetch-site': 'same-site',
            'User-Agent': generate_random_user_agent(),
            'x-app-id': 'carv'
        }
    