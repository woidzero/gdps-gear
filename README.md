# GDPSGear

Discord bot for managing Geometry Dash IOCore based private servers

! This project is **NOT** maintained and will no longer be relevant after October 2023.
! This project is not finished


## Running
```bash
git clone https://github.com/woidzero/gdps-gear.git
cd gdps-gear
python -m pip install -r requirements.txt
python bot.py
```

## Setup
1. Go to [Discord Developers](https://discord.com/developers/applications) and create new app
2. Go to Bot and create it then copy the token
3. Copy your Discord ID ([tutorial](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-))
3. Edit and rename .env.example to .env
3. Invite the bot to your server


## Usage
### Bot commands
- `profile <nickname>` : View GDPS user profile.
- `level <id>` : View the level information.
- `leaders <query>` : View the GDPS leaderboard.
- `weekly` : Weekly level info.
- `daily` : Daily level info.
- `ping` : Discord WebSocket latency.
- `help` : Commands list.
- `account help` : Account linking.


## Support

For support, email <a href="mailto://woidzerov@gmail.com">woidzerov@gmail.com</a>

## License

`gdps-gear` is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
