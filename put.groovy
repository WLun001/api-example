import groovy.json.JsonOutput
import groovy.json.JsonSlurper
import groovy.json.JsonBuilder
import io.gravitee.policy.groovy.PolicyResult.State

class Person {
   String firstName
   String lastName
   int age
   String id = UUID.randomUUID().toString()
   
}

def arr = []
def jsonSlurper = new JsonSlurper()
try {
    def response = jsonSlurper.parseText(response.content)
     if (response.firstname == null || response.lastname == null || response.age == null) {
        throw new Exception("property firstname, lastname or age not found")
    }
    arr.add(new Person(
        firstName: response.firstname, 
        lastName: response.lastname,
        age: response.age as Integer)
        )

    return JsonOutput.toJson(arr.last())
} catch (Exception e) {
    result.state = State.FAILURE;
    result.code = 400
    JsonBuilder json = new JsonBuilder()
    json error: e.message,
            code: result.code

    result.error = json.toString()
    result.contentType = 'application/json'
}

