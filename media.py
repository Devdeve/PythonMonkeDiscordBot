import json
import os
import random
from os import listdir
from os.path import isfile, join

import discord


_manifest = None


def _load_manifest():
    global _manifest
    if _manifest is not None:
        return _manifest

    manifest_path = os.environ.get("MEDIA_MANIFEST", "media_manifest.json")
    if not os.path.exists(manifest_path):
        _manifest = {"fixed": {}, "random": {}}
        return _manifest

    with open(manifest_path, "r", encoding="utf-8") as manifest_file:
        _manifest = json.load(manifest_file)
    return _manifest


async def send_fixed_media(ctx, key, local_path):
    media_url = _load_manifest().get("fixed", {}).get(key)
    if media_url:
        await ctx.send(media_url)
        return

    if os.path.exists(local_path):
        await ctx.send(file=discord.File(local_path))
        return

    await ctx.send(f"Missing media for `{key}`.")


async def send_random_media(ctx, key, local_folder):
    media_urls = _load_manifest().get("random", {}).get(key, [])
    if media_urls:
        await ctx.send(random.choice(media_urls))
        return

    if os.path.isdir(local_folder):
        local_files = [f for f in listdir(local_folder) if isfile(join(local_folder, f))]
        if local_files:
            await ctx.send(file=discord.File(join(local_folder, random.choice(local_files))))
            return

    await ctx.send(f"Missing media list for `{key}`.")
