#!/usr/bin/python
import getopt
import os
import sys
from itertools import groupby
from .api import RickAndMortyClient


def help():
    # TO DO: Add help for creating a venv
    print('Fax, scan and print the internet!\n')
    print('Virtualenv Setup:')
    print('1. Ensure virtualenv is installed: pip install virtualenv')
    print('2. Create a virtualenv environment: virtualenv <project-name>')
    print('3. Activate the environment: source <project-name>/bin/activate')
    print('- (optional) when finished deactivate: deactivate\n')
    return


def fetch_episodes():
    client = RickAndMortyClient()
    episodes = client.fetch_and_sort_episodes()
    return episodes


def create_html_content(episodes):
    out = '<html><head></head><body>{}</body></html>'
    sections = []
    for key, season_episodes in groupby(episodes, key=lambda x: x['air_date'][-4:]):
        header = '<h2>{}.<h2>\n'.format('Episodes {}'.format(key))
        content = '<ul>'
        for se in season_episodes:
            content += '<li><strong>Name</strong>: {}, <strong>Air-Date</strong>: {}</li>\n'.format(
                se['name'], se['air_date'])
        content += '</ul>'
        section = '{}{}'.format(header, content)
        sections.append(section)
    return out.format('\n'.join(sections))


def create_html_file(dest, html_content):
    with open(dest, 'w+') as f:
        f.write(html_content)


class RickAndMortyHtmlFile:

    @staticmethod
    def create(target_filepath='./test.html'):
        print('Creating the html file: test.html.')
        episodes = fetch_episodes()
        html_content = create_html_content(episodes)
        create_html_file(target_filepath, html_content)


def cleanup(file):
    try:
        os.remove(file)
    except OSError:
        print('File ' + file + ' doesn\'t exist.')
        return 'Error'
    print('File ' + file + ' has been removed.')
    return 'Done'


if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(
            argv,
            "h",
            ["help", "cleanup="],
        )
    except getopt.GetoptError:
        print('Invalid options.')
        sys.exit(2)
    if opts:
        for opt, arg in opts:
            if opt in ['-h', '--help']:
                help()
                sys.exit()
            elif opt == '--cleanup':
                cleanup(arg)
                sys.exit()
    else:
        rmf = RickAndMortyHtmlFile()
        rmf.create()
