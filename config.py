import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '34.72.195.140',
            'DB_NAME': 'retail_db',
            'DB_USER': 'retail_user',
            'DB_PASS': 'sidbigdata'
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '34.72.195.140',
            'DB_NAME': 'retail_dw',
            'DB_USER': os.environ.get('TARGET_DB_USER'),
            'DB_PASS': os.environ.get('TARGET_DB_PASS')
        }
    }
}