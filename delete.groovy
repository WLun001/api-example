import groovy.json.JsonOutput
import groovy.json.JsonSlurper
import groovy.json.JsonBuilder
import io.gravitee.policy.groovy.PolicyResult.State

class Person {
   String firstName;
   String lastName;
   int age;
   String id;
}

def arr = [
    new Person(firstName: "wong", lastName: "a", age: 11, id: "1"), 
    new Person(firstName: "wong", lastName: "b", age: 11, id: "2"), 
    new Person(firstName: "wong", lastName: "c", age: 11, id: "3")
    ]

def jsonSlurper = new JsonSlurper()
try {
    def response = jsonSlurper.parseText(response.content)
    if (response.id == null) {
        throw new Exception("property id not found")
    }
    def found = arr.find{it.id == response.id}
    def removed = arr.remove(found)
    if (removed) {
        def res = [firstname: found.firstName]
        res << [lastname: found.firstName]
        res << [age: found.age]
        res << [id: found.id]
        res << [message: "Successfully deleted"]
        return JsonOutput.toJson(res)
    } else {
        result.state = State.FAILURE;
        result.code = 404
        result.error = '{"error":"User not found","code": "404"}'
        result.contentType = 'application/json'
    }
} catch(Exception e) {
     result.state = State.FAILURE;
        result.code = 400
        JsonBuilder json = new JsonBuilder()
        json error: e.message,
              code: result.code

        result.error = json.toString()
        result.contentType = 'application/json'
}