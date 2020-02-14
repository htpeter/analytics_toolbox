# Title
> summary


```python
%load_ext autoreload
%autoreload 2
```

# Welcome to `analytics_toolbox` aka `atb`

### Enabling Data Scientists to amplify their inner Data Engineer.

> A toolbox for managing data coming from multiple Postgres, Redshift & S3 data sources while performing Analytics and Research. We also have some functionality that help users build Slack Bots. 

## [Install Us](https://pypi.org/project/analytics-toolbox/)

`pip install analytics_toolbox`

## [Documentation](https://htpeter.github.io/analytics_toolbox/)

Our docs are currently useless as of 2020-02-12.

## [Vote For Change!](https://github.com/htpeter/analytics_toolbox/issues)

I'll see your comments on GitHub.

## Support Us

Coming someday, maybe?


# Do You Know About config Files?

`analytics_toolbox` is only made possible by its reliance on standardized credential storage. You wanna use us, you sadly must play by some of our rules.  

We read and build classes via the variable names in the config files you pass to our code. Trust us. Its worth it. You'll end up saving 100s of lines of code by simply passing 1 to 2 arguments when instantiating our primary classes.

[Config Files](https://en.wikipedia.org/wiki/Configuration_file) are a great way to store information. We chose this over other options like json or OS level environment variables for no clear reason. If you really want support for other credential formats, [vote with your words here](https://github.com/htpeter/analytics_toolbox/issues/1).


## Config File Format Guidelines

### Postgres + Redshift Connections

If your config file section has a `hostname`, `port`, `database` and `user` sections, then we'll parse it as a Redshift/Postgres database. You store your password in `.pgpass` (see below if this is new).

Here is an example of Postgres/Redshift entries.
`"`"
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

#### What is .pgpass?

When python's `psycopg2` or even `psql` attempt to connect to a server, they will look in a file called  `~/.pgpass`. If they find matching server information, based on the target they are connecting  to, they use that password.

`~/.pgpass`'s format is simple. Include a line in the file that follows the following format.
```
hostname:port:database:username:password
```

Ensure you limit the permissions on this file using `chmod 600 ~/.pgpass`, otherwise no tools will use it due to its insecurity.

You don't pass database passwords to `analytics_toolbox`. Instead we leverage [pgpass](https://www.postgresql.org/docs/9.3/libpq-pgpass.html). Simply paste a record for each database in a text file `~/.pgpass` with the following information.


### Slack Connections 

Our Slack APIs use [Slack Bot OAuth Tokens](https://slack.com/help/articles/215770388-Create-and-regenerate-API-tokens#bot-user-tokens). 

Create an OAuth token and save it to a variable called `bot_user_oauth_token`. You can store the token in a config section named whatever you want.

```
[company_slack]
oauth_token = 943f-1ji23ojf-43gjio3j4gio2-2fjoi23jfi23hio

[personal_slack]
oauth_token = 943f-dfase3-basf234234-fw4230kf230kf023k023
```

## Usage Examples

### Querying Multiple Databases & Moving Data

Our import is both useful and classy enough to be jammed up at the top with your`pd`s, `np`s  and `plt`s.

```python
import analytics_toolbox as atb
```

And then you simply create a database pool object with your Config File. It loads up all the goodies.

```python
db = atb.DBConnector('../atb_config_template.ini')

db
```




    {   'dev_db': <analytics_toolbox.connector.DatabaseConnection object at 0x11698bc88>,
        'prod_db': <analytics_toolbox.connector.DatabaseConnection object at 0x1169d8198>}



Now we can query any of our databasese easily!

```python
# reference with the config file keyname 
db['dev_db'].qry('select * from pg_class limit 5')
db['prod_db'].qry('select * from pg_class limit 5')

# or if config file section is pythonic, use its name just like pandas!
db.dev_db.qry('select * from pg_class limit 5')
db.prod_db.qry('select * from pg_class limit 5')
```
