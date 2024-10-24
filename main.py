import sys
import json
from colorama import *
from src.core import Banana, config
from requests.exceptions import RequestException
from src.deeplchain import log, log_error, countdown_timer, mrh, htm, bru, kng, pth, hju, _banner, _clear, load_config
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError, Timeout, ProxyError, HTTPError

init(autoreset=True)
config = load_config()

def load_tokens():
    try:
        with open('tokens.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_tokens(tokens):
    with open('tokens.json', 'w') as file:
        json.dump(tokens, file, indent=4)

def main():
    _clear()
    _banner()
    banana = Banana()

    try:
        with open('data.txt', 'r') as file:
            queries = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        log(mrh + "No data.txt file found.")
        return

    total_accounts = len(queries)
    tokens = load_tokens()

    while True:
        for current_index, query in enumerate(queries):
            try:
                user_id = banana.extract_user_id(query)
                existing_token = tokens.get(user_id, [])

                if existing_token:
                    token_to_use = existing_token[0]
                else:
                    new_token = banana.login(query)
                    if new_token:
                        tokens[user_id] = tokens.get(user_id, []) + [new_token]
                        save_tokens(tokens)
                        token_to_use = new_token
                    else:
                        log(f"Failed to get token for user ID {user_id}")
                        continue

                use_proxy = config.get('use_proxy', False)
                if use_proxy and banana.proxies:
                    banana.proxy_index = (banana.proxy_index + 1) % len(banana.proxies)
                    proxy = banana.get_current_proxy()
                    if proxy:
                        proxy_url = proxy.get('http', '')
                        host_port = proxy_url.split('@')[-1] if '@' in proxy_url else proxy_url.split('//')[-1]
                    else:
                        host_port = 'No proxy'
                else:
                    host_port = 'No proxy'

                user_info = banana.get_user_info(token_to_use)
                data = user_info['data']
                if isinstance(data, str):
                    data = json.loads(data)

                username = data.get('username', 'Unknown')
                total_usdt = data.get('usdt', 0)
                total_peel = data.get('peel', 0)
                click_count = data.get('max_click_count', 0)
                speedup_count = data.get('speedup_count', 0)
                total_banana = data.get('banana_count', 0)

                log(hju + f"Account: {pth}{current_index + 1}/{total_accounts}")
                log(hju + f"Using proxy: {pth}{host_port}")
                log(htm + "~" * 38)

                log(bru + f"Logged in as {pth}{username}")
                log(hju + f"Balance: {pth}{total_peel} {kng}PEEL {hju}| {pth}{total_usdt} {hju}USDT")
                log(hju + f"Click limit: {pth}{click_count} {hju}| BaBoost: {pth}{speedup_count}")
                log(hju + f"You have a total {pth}{total_banana} {kng}Banana")

                banana.get_lottery(token_to_use)
                banana.banana_list(token_to_use)
                banana.do_speedup(token_to_use)

                log(htm + "~" * 38)
                countdown_timer(config["delay_account"])

            except (HTTPError, IndexError, JSONDecodeError, ConnectionError, Timeout, ProxyError, RequestException, Exception) as e:
                log(mrh + f"Error processing account {current_index + 1} check last.log")
                log_error(f"{str(e)}")
                continue 

        countdown_timer(config["countdown_loop"])

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            log(mrh + "Progress terminated by user")
            sys.exit(0)


