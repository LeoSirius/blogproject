import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'frontend/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/webpack-stats.dev.json'),
    }
}

SERVER_URL = ''
GITHUB_PAT = ''
GITHUB_REPO_URL = ''

DOC_REPO_PATH = '/Users/leo/Github/doctree/notes'
