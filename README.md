halo
Berikut adalah contoh file README yang menarik untuk proyek bot Telegram Anda. Pastikan untuk menambahkan gambar yang relevan di direktori proyek Anda dan mengubah nama file gambar sesuai kebutuhan.

```markdown
# YouTube Downloader Bot

![YouTube Downloader Bot](images/banner.png)

Welcome to the **YouTube Downloader Bot**! This bot allows users to download YouTube videos in MP3 or MP4 format directly from Telegram. It's simple to use and integrates with a channel membership check to ensure users are subscribed before downloading.

## Features

- **Download YouTube Videos**: Get your favorite YouTube videos in MP4 format.
- **Download YouTube Audios**: Extract and download the audio from YouTube videos in MP3 format.
- **Channel Membership Check**: Ensure users are subscribed to your Telegram channel before they can download content.

## How to Use

1. **Start the Bot**: Send the `/start` command to the bot.
2. **Join the Channel**: Follow the link to join the specified Telegram channel.
3. **Refresh**: Click the 'Refresh' button after joining the channel.
4. **Download Content**: Enter the YouTube link and choose whether to download as MP3 or MP4.

## Screenshots

### Welcome Message
![Welcome Message](images/welcome_message.png)

### Main Menu
![Main Menu](images/main_menu.png)

### Download MP3
![Download MP3](images/download_mp3.png)

### Download MP4
![Download MP4](images/download_mp4.png)

## Requirements

- Python 3.7 or higher
- `python-telegram-bot==13.14`
- `pytube==15.0.0`
- `pydub==0.25.1`

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Replace the placeholder values for `BOT_TOKEN` and `CHANNEL_USERNAME` in `main.py` with your actual bot token and channel username.

```python
# Replace with your bot token and channel username
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_USERNAME = "@your_channel_username"
```

## Running the Bot

Run the bot with the following command:

```bash
python main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements.

---

Made with ❤️ by [Your Name](https://github.com/yourusername)
```

### Adding Images

To include images in your README:

1. Create an `images` directory in your project root.
2. Add your images (e.g., `banner.png`, `welcome_message.png`, `main_menu.png`, `download_mp3.png`, `download_mp4.png`) into the `images` directory.
3. Adjust the image paths in the README to match your image filenames.

### Notes

- Replace `yourusername` and `your-repo-name` with your actual GitHub username and repository name.
- Customize the text to better fit your specific bot and use case.
- Ensure you have the necessary permissions and rights to use and share the images included in your README.
