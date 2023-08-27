# Twitter Bot - COVID Vaccine Appointment Notifier

![Twitter Bot Logo](your-logo-image-url-here)

## Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Features](#features)
- [Impact](#impact)
- [Setup](#setup)
- [Usage](#usage)
- [Contributions](#contributions)
- [License](#license)

## Introduction

This project is aimed at developing a Twitter bot that notifies low-income families in small agricultural communities about available COVID-19 vaccine appointments. It uses web scraping techniques to collect real-time vaccine appointment availability and posts updates on Twitter.

## Technologies

- Language: Python
- Libraries: Selenium
- APIs: Twitter API
- Other Tools: HTML

## Features

- **Real-time Notifications**: Provides real-time updates on vaccine appointment availability.
- **Automated Form Filling**: Uses Selenium to fill out California vaccine forms automatically.
- **Targeted Information**: Specifically caters to agricultural communities in the Imperial County.

## Impact

- **Equitable Access**: Ensured vaccine access for 50 essential workers and senior community members in the Imperial County.
- **Community Service**: Fills a critical gap by providing a real-time vaccine appointment notifier where none previously existed for these communities.

## Setup

To run this project, install the required packages:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

Add your Twitter API keys to a `.env` file:

\`\`\`env
TWITTER_API_KEY=your-api-key-here
TWITTER_API_SECRET_KEY=your-secret-key-here
\`\`\`

## Usage

Run the main Python script to start the bot:

\`\`\`bash
python main.py
\`\`\`

## Contributions

Feel free to fork this project, open a pull request, or submit issues through [GitHub](https://github.com/acramire/iv-vaccine-bot).

## License

This project is open-source, available under [MIT License](LICENSE).
