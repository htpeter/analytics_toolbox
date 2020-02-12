# analytics_toolbox
> A toolbox for Analytics and Research.


## Install

`pip install analytics_toolbox`

## [Documentation](https://htpeter.github.io/analytics_toolbox/)


## Help With Postges Connection Setup

### Step 1. Formatting Your Database Config Files

For example, you have the following `config.ini` file.
```
[dev_db]
hostname = dev.yourhost.com
port = 5432
database = dbname 
user = htpeter

[prod_db]
hostname = prod.yourhost.com
port = 5432
database = dbname 
user = htpeter
```

### Step 2. Ensuring you have .pgpass setup

You don't pass passwords to `analytics_toolbox` in its current form. Instead it leverages [pgpass](https://www.postgresql.org/docs/9.3/libpq-pgpass.html). Simply paste a record for each database in a text file `~/.pgpass` with the following information.

```
hostname:port:database:username:password
```

When `psycopg2` or even `psql` attempt to connect to a server, it will look in this file and if it finds matching server information, it will use that password.

Ensure you limit the permissions on this file using `chmod 600 ~/.pgpass`

## Usage Examples

```python
import analytics_toolbox as atb
```
