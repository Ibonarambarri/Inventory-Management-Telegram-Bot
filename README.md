# Inventory Management Telegram Bot

This Python project creates a Telegram bot that can manage inventory for products. It is capable of handling multiple functionalities like stock management, product catalog browsing, and administrative control with the help of different operational modes.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Telebot module
- OpenCV (cv2)
- argparse
- datetime

To install the required packages, use pip:

```
pip install pyTelegramBotAPI
pip install opencv-python
pip install argparse
```

### Installing

To use this bot, clone this repository to your local machine and replace `'YOUR_TELEGRAM_BOT_API_KEY'` with your actual Telegram Bot API key.

## Features

The bot operates in three modes: 'stock', 'products', and 'admin'. The functionalities of these modes are as follows:

- **Stock Mode:** In this mode, the bot can edit and display the stock of different items.

- **Products Mode:** In this mode, the bot can display product details from the catalog.

- **Admin Mode:** The admin mode is for future development.

## Commands

- `/start`,`/help`: Starts the bot.
- `/modostock`: Switches the bot to 'stock' mode.
- `/modoproductos`: Switches the bot to 'products' mode.
- `/modoadmin`: Switches the bot to 'admin' mode.
- `/stock`: Displays the current stock of all items.

## Running the Bot

To run the bot, navigate to the directory containing `main.py` and execute the following command:

```
python main.py
```

The bot will now start and will be ready to accept commands.

## Built With

- [Python](https://www.python.org/)
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)

Please note that this project is still under development and certain features might not work as expected.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

This `README.md` file provides a general understanding of the project. However, more detailed documentation with function descriptions, argument details, and return types might be beneficial for the users and developers.
