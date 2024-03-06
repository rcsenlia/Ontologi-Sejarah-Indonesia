import requests

api_url = 'http://localhost:7200/repositories/pizza-example?query=PREFIX%20pizza%3A%20%3Chttp%3A%2F%2Fwww.semanticweb.org%2Fpizzatutorial%2Fontologies%2F2020%2FPizzaTutorial%23%3E%20select%20*%20where%20%7B%20%20%20%20%20%3Fx%20a%20pizza%3APizzaTopping%20.%20%20%20%20%20%3Fx%20a%20%3Fy%20%7D&limit=5'
headers = {"Content-Type":"application/json", "Accept":"application/sparql-results+json"}
response = requests.get(api_url, headers=headers)
print(response.json())

#%%
