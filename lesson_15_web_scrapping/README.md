# Web Scrapping project

## Run application

Run command script:

```shell
python main.py
```

List of available parameters:

- *--pages*: int value. Enter web site's pages count for scrapping and storing news into csv file.
- *--parser* string value. Enter parser name for scrapping web site. Default value: `dounewsparser`.

Examples:

- Run script for downloading 2 pages:

```shell
python main.py --pages=2
```

- Run script to download 3 pages and use particular parser:

```shell
python main.py --parser=dounewsparser --pages=3
```