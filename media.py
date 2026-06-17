import json
import os
import random
from os import listdir
from os.path import isfile, join

import discord


_manifest = None


def _load_manifest():
    print("Loading manifest")
    _manifest = None
    if _manifest is not None:
        print(f"Manifest already defined, returning manifest")
        return _manifest
    print(f"Manifest doesnt exist, proceeding to read from file")
    manifest_path = os.environ.get("MEDIA_MANIFEST", "media_manifest.json")
    if not os.path.exists(manifest_path):
        print(f"Manifest file does not exist, returning empty")
        _manifest = {"fixed": {}, "random": {}}
        return _manifest

    with open(manifest_path, "r", encoding="utf-8") as manifest_file:
        read_file = manifest_file.read()
        print(f"Loading manifest file as json")
        _manifest = json.loads(read_file)
    print(f"Manifest loaded successfully")
    return _manifest


async def send_fixed_media(ctx, key, local_path):
    print("Sending fixed media called")
    media_url = _load_manifest().get("fixed", {}).get(key)
    if media_url:
        print(f"Sending media from {media_url}")
        await ctx.send(media_url)
        return
    print("Media url does not exist, using local files")
    
    if os.path.exists(local_path):
        print(f"Sending media from local files: {local_path}")
        await ctx.send(file=discord.File(local_path))
        return

    print(f"Missing media list for `{key}`.")
    await ctx.send(f"Missing media list contact @devdeve on discord.")

async def send_random_media(ctx, key, local_folder):
    print("Sending random media")
    media_urls = _load_manifest().get("random", {}).get(key, [])
    if media_urls:
        media_choice = random.randint(0, len(media_urls) - 1)
        print(f"Sending {media_urls[media_choice]} media from {media_urls}")
        await ctx.send(media_urls[media_choice])
        return
    print("Media url does not exist, using local files")
    
    if os.path.isdir(local_folder):
        local_files = [f for f in listdir(local_folder) if isfile(join(local_folder, f))]
        if local_files:
            local_choice = random.randint(0, len(local_files) - 1)
            print(f"Sending media from local files: {local_files[local_choice]}")
            await ctx.send(file=discord.File(join(local_folder, local_files[local_choice])))
            return
    print(f"Missing media list for `{key}`.")
    await ctx.send(f"Missing media list contact @devdeve on discord.")
