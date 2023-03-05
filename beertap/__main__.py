import argparse
import os
import sys

import discord

from . import *
from .commands import *

class CLI:
    _default_token = os.getenv('BEERTAP_OAUTH_TOKEN')
    token: str = _default_token

    _parser = argparse.ArgumentParser(prog='python -m beertap', description='BeerTap: A replacement for MEE6 in the Sunset Room')
    _parser.add_argument('token', help='Oauth token for connecting the bot to Discord. Can also supply via the environment variable BEERTAP_OAUTH_TOKEN.', nargs='?', default=_default_token)

    @classmethod
    def parse_args(cls, args=None):
        self = cls._parser.parse_args(args, cls())
        if self.token is None:
            cls._parser.print_help(sys.stderr)
            print('ERROR: missing required argument "token" or environment variable "BEERTAP_OAUTH_TOKEN"', file=sys.stderr)
            sys.exit(1)
        return self


def main():
    cli = CLI.parse_args()
    client = BeerTap(intents=discord.Intents.all())
    client.add_command(echo)
    client.run(cli.token)


if __name__ == '__main__':
    main()
