curl -X GET http://motorway:8000/weilun/get-all-users | json_pp 

curl -X POST http://motorway:8000/weilun/get-user-info -d '{"id":"1"}' -v | json_pp 

curl -X POST http://motorway:8000/weilun/add-user -d '{"firstname":"kevin","lastname":"wong","age":"12"}' -v -H "Content-Type: application/json" | json_pp

curl -X POST http://motorway:8000/weilun/delete -d '{"id": "1"}' -v -H "Content-Type: application/json" | json_pp

