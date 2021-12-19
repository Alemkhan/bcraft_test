# Test statistics service for BCraft

### Installation
#### Build a project:
```
docker-compose up -d --build
```
#### Migrate tables
```
docker-compose exec web python manage.py migrate --noinput
```

### API documentation
### Statistics creation API
```
POST <host>/api/v0/statistics/created
Creates a statistic based on several inputs
> Views, clicks and cost are optional fields
```
#### JSON Body 
```json
{
    "date": "YYYY-MM-dd",
    "views": 2500,
    "clicks": 1200,
    "cost": 2500
}
```
### Statistics List API
```
Shows all statistics based on search parameters or all statistics 
if no parameters given
GET <host>/api/v0/statistics?from_date=YYYY-MM-dd&to_date=YYYY-MM-dd&sort=<one_param: cpc>
```
#### JSON Body 
```json
[
  {
    "date": "2021-12-17",
    "views": 1222,
    "clicks": 500,
    "cost": "3000.00",
    "cpc": 6.0,
    "cpm": 2454.991816693944
  },
  {
    "date": "2021-12-20",
    "views": 2222,
    "clicks": 1200,
    "cost": "3300.00",
    "cpc": 2.75,
    "cpm": 1485.148514851485
  }
]
```
#### Statistics Reset API
```
<host>/api/v0/statistics/reset
Set all statistics to is_deleted, so it will not be seen further
but could be backuped
```
