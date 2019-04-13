# Metrics

## Build

How to build the project.

### With Docker Compose

```
$ docker-compose up
```

### With Docker

You can build the service using only `Docker`.

```
$ docker build . -t metrics
$ docker run -it -p 4000:4000 metrics
```

GET Example: `http://127.0.0.1:4000/api/v1/metrics?date_to=2017-06-01&sort_by=clicks&order=desc&group_by=channel,country`

### Database

It is just a SQLite =( `metrics.sqlite3`. 

### Testing Service

`404` There is no unittests or behaviroual tests, that's a shame.

## License

```
/*
 * "THE BARBECUE-WARE LICENSE" (Revision 1):
 *
 * <benatto@gmail.com> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can make me a brazilian barbecue, including beers
 * and caipirinha in return to Paulo Leonardo Benatto.
 *
 * The quality of the barbecue depends on the amount of beer that has been
 * purchased.
 */
 ```

## Bug Reports

If you see something wrong just send me a message, and I will fix it as soon as possible.

## Contact

```
$ echo "moc.liamg@ottaneb" | rev
```