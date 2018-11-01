import groovy.json.JsonOutput
import groovy.json.JsonBuilder
import io.gravitee.policy.groovy.PolicyResult.State

class Person {
   String firstName
   String lastName
   int age
   String id
}
def arr = [
    new Person(firstName: "wong", lastName: "a", age: 11, id: "1"), 
    new Person(firstName: "wong", lastName: "b", age: 11, id: "2"), 
    new Person(firstName: "wong", lastName: "c", age: 11, id: "3")
    ]

try {
    if (arr.size() < 1) {
        throw new Exception("No user found")
    }
    return JsonOutput.toJson(arr)
} catch (Exception e) {
    result.state = State.FAILURE;
    result.code = 400
    JsonBuilder json = new JsonBuilder()
    json error: e.message,
         code: result.code

    result.error = json.toString()
    result.contentType = 'application/json'
}
