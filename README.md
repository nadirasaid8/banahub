# B4n4n4 Script for B4n4n4 by C4rv Protocol (FORCE RUN)

This repository contains a Python script designed to automate interactions with the B4n4n4 API provided by Carv. The script logs into multiple accounts, performs various actions like clicking, claiming lotteries, equipping bananas, selling them, and speeding up processes based on the configurations set in `config.json`.

[TELEGRAM CHANNEL](https://t.me/Deeplchain) | [CONTACT](https://t.me/imspecials)

## Registrations
 - Open and start [ [B4N4N4 BOT](https://t.me/OfficialBananaBot/banana?startapp=referral=4FA3K91) ]
 - Do tap And Claim lottery
 - Collect PEEL also USDT
 - Withdraw USDT Instant

### What's new in this update?
change requests to api using cloudscraper, for this you must first install it by `pip installing cloudscraper` or just `pip install -r requirements.txt`.

- Proxy Support : format `username:pass@ip:port` file `proxies.txt`
- Improved the function to sell bananas.
- Added a new function to complete all available quest.
- Added a new configuration option to enable or disable the script's ability to complete quest.
- Added a new function to claiming bananas quest reward.
- Improved the lottery claiming process.
- Enhanced the script's logging capabilities.

## Features

- **Multi-account Support:** Automate actions across multiple accounts.
- **Lottery Operations:** Automatically handle lottery claims and clicks.
- **Banana Management:** Equip, sell, and manage your banana inventory.
- **Auto Complete Task** Automaticaly perform available quest
- **Auto Claim Quest Reward** After completing quest bot claim banana reward
- **Speed Up:** Automatically perform speed-up operations if enabled.
- **Configurable Settings:** Control various aspects of the script via a `config.json` file.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jawikas/banana-bot.git
   cd banana-bot
   
Create and activate a virtual environment:

   ```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
Install the required dependencies:

   ```bash
pip install -r requirements.txt
   ```

## Configuration
Create a config.json file in the root directory with the following structure:
   ```json
{
    "use_proxy": false,
    "auto_sell": false,
    "auto_speedup": false,
    "auto_task": false,
    "delay_account": 5,
    "cycle_delay": 3800
}
   ```
`use_proxy`: Enable it with `true` to activate proxy usage 

`auto_sell`: Automatically sell bananas if set to true (if banana > 1)

`auto_speedup`: Enable the speed-up (BaBoost) operation if set to true.

`auto_task`: Enable the auto-task (auto-task) operation if set to true.

`delay_account`: Delay between processing different accounts (in seconds).

`cycle_delay`: Delay between different cycles of operations (in seconds).

## Fill data.txt
Add a data.txt file containing the login information (e.g., tokens or other necessary data). Each line should represent a separate account.
1. Use PC/Laptop or Use USB Debugging Phone
2. open the `Banana bot miniapp`
3. Inspect Element `(F12)` on the keyboard
4. at the top of the choose "`Application`" 
5. then select "`Session Storage`" 
6. Select the links "`Banana`" and "`tgWebAppData`"
7. Take the value part of "`tgWebAppData`"
8. take the part that looks like this: 

```txt 
query_id=xxxxxxxxx-Rxxxxuj&
```
9. add it to `data.txt` file or create it if you dont have one


You can add more and run the accounts in turn by entering a query id in new line like this:
```txt
query_id=xxxxxxxxx-Rxxxxujhash=cxxx
query_id=xxxxxxxxx-Rxxxxujhash=cxxxx
```

after that run the Banana bot by writing the command

## Usage
To run the script, simply execute:

   ```bash
python main.py
   ```
The script will start processing each account listed in data.txt, performing all configured operations.


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or issues, please open an issue on GitHub or contact me at [ https://t.me/deeplchain ]