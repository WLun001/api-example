import groovy.json.JsonOutput

def res = "http://172.16.6.155:5000/get_all_item".toURL().text
return JsonOutput.toJson(res)