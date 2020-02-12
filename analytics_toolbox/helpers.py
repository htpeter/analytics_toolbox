#AUTOGENERATED! DO NOT EDIT! File to edit: dev/99_helpers.ipynb (unless otherwise specified).

__all__ = ['get_str_var_names', 'open_and_run']

#Cell

import _string

def get_str_var_names(yourstring):
    return [fname for _, fname, _, _ in _string.formatter_parser(yourstring) if fname]


def open_and_run(sql_file, db_obj, commit = False):
    if hasattr(db_obj, 'qry'):
        with open(sql_file, 'r') as f:
            sql = f.read()
            return getattr(db_obj, 'qry')(sql, commit)
    else:
        raise Exception(f"Did not pass database object when running {sql_file}")