# Free Hosting Plan

## Recommended setup

Run the Python bot as a free background worker, and host the images/videos separately as public URLs.

The bot process is tiny. The painful part is the media: this repo is about 324 MB, and most commands send local files with `discord.File(...)`. That works locally, but it makes free app deployments slower and more fragile.

## Bot host

If you have Railway trial credit, try Railway first:

1. Push the repo to GitHub.
2. In Railway, create a new project from the GitHub repo.
3. Railway will read `railway.json`.
4. Set these variables:
   - `DISCORD_TOKEN`
   - `DISCORD_OWNER_ID`
   - optional `DISCORD_PREFIX`, default `!`
5. Deploy.

`railway.json` sets the start command to `python main.py` and restarts the service if it exits. This is important because the bot is a long-running worker, not a web server.

`.python-version` pins Railway to Python 3.12 because this version of `discord.py` imports `audioop`, which is not available in Python 3.13.

Render is the no-card fallback if the Railway trial runs out:

1. Push the repo to GitHub.
2. On Render, create a new Blueprint from the repo.
3. Render will read `render.yaml`.
4. Set these environment variables:
   - `DISCORD_TOKEN`
   - `DISCORD_OWNER_ID`
   - optional `DISCORD_PREFIX`, default `!`
5. Deploy.

The bot now reads secrets from environment variables, so `configuration.json` can stay local and should not contain the production token in GitHub.

## Media host

If Cloudflare R2 is available, a public R2 bucket is the cleanest media option.

R2's free tier is enough for the current asset size, and egress is free. Upload folders like `monkeys/`, `days/`, `borzoi/`, `gator/`, and `foog/`, then change bot commands to send the public object URL instead of uploading the file.

Example:

```py
await ctx.send("https://media.example.com/monkeys/cooling_off.webm")
```

This keeps the app deployment small and avoids Discord upload trouble.

If R2 is not available, enable GitHub Pages for this public repo from the `main` branch root. The bot can then post URLs from `media_manifest.json`, which points at `https://devdeve.github.io/PythonMonkeDiscordBot/...`.

## Simple migration path

1. Upload all media to R2 with matching paths.
2. Create JSON lists of URLs for random folders, for example `monkeys.json` and `borzoi.json`.
3. Update random commands to choose a URL and `ctx.send(url)`.
4. Update fixed commands like Wednesday/Tuesday/Foog to send a single URL.
5. Remove media folders from the deployed branch or add them to `.gitignore` after they are hosted.

## Backup options

Oracle Cloud Always Free is the most capable zero-dollar VM option if you are comfortable managing Linux and systemd yourself.

Google Cloud can also work with an always-free `e2-micro` VM in eligible US regions, but free egress is much tighter.

Fly.io is less attractive for this use now because its old free allowances are legacy-only.
