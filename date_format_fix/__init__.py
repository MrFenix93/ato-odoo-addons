from . import models

def post_init_hook(env):
    env.cr.execute("""
        UPDATE res_lang
        SET date_format = '%d/%m/%Y',
            time_format = '%I:%M:%S %p'
        WHERE active = true
    """)
