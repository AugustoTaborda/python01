pessoa = {
    "nome": "surdidinha",
    "idade": 1000000000000000000000000,
    "cidade": "surdinha"
    
}

print(pessoa)

print(f"nome:  {pessoa["nome"]}\nCidade: {pessoa["cidade"]}")

pessoa["email"] = "augu@gmail.com"
print(pessoa)


del pessoa["idade"]
print(pessoa)