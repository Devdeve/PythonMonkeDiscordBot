# To Start:
1. Clone the repo
2. Set the token in configuration.json, or set DISCORD_TOKEN in your environment
3. Create a python virtual environment (python -m venv MonkeEnvironment)
4. Activate the virtual environment (./PythonMonkeDiscordBot/MonkeEnvironment/Scripts/Activate.ps1)
5. Import required modules (pip install -r .\requirements.txt)
6. Run the bot (python .\main.py)

For Railway and free hosting notes, see HOSTING.md.

# Hosted media

The bot reads `media_manifest.json` for hosted media URLs. Enable GitHub Pages for this repo from the `main` branch root so media is available under:

`https://devdeve.github.io/PythonMonkeDiscordBot/`

Random commands use `random.monkeys` and `random.borzoi`. Fixed commands use keys like `fixed.wednesday`, `fixed.foog`, and `fixed.fff`.
