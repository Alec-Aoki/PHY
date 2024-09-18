# Python

## Tipos de Dados
-> não é fortemente tipada (podemos declarar variáveis sem tipo e a linguagem a converterá automaticamente)
- int
- float
- str
- bool
- none
```python
variavel: float = 10.10 #float = não define o tipo da variável, apenas torna o tipo explícito
```

## I/O
### Output
```python
print("Toda string precisa estar entre aspas")

nome: str = "Alec"
print(f"Ola {nome}") #f significa format, e define que qualquer coisa entre chaves não é texto, mas uma variável
print(nome)

print("Como printar sem espaco?", end=" ")
print("Usando o end")
```
### Input
```python
numeroInteiro: int(input()) #por padrão, todo input() será tratado como uma string!
#é preciso usar um cast
```

## Estruturas de Decisão
```python
numero = int(input())

if(x>10):
    print("numero>10")
else:
    print("numero<10")

print("A indentacao importa!!!")
```

## Estruturas de Repetição
- while
```python
i: int = 10
while(i > 0):
    print(i, end=" ")
    i = i - 1
    time.sleep(1)
```
- for
```python
a = 1
b = 11
c = 1
for j in range(a, b, c): #j começando em a, até b (não inclusivo), de c em c; por padrão, a=0 e c=1
    print(j, end=" ")

for k in range(10, 0, -1):
    print(j, end=" ")
```
- break: sai do laço imediatamente
- continue: para a execução, atualiza o contador e volta para o início do laço

## Estrutura de Dados
- lista
```python
lista = [10, "Alec", True, 3.14]
print(lista[0])
print(lista[1])
print(lista[-1])

lista.append("Poggers")
lista.remove(10) #remove o valor 10
print(lista)
lista.pop(2) #remove o index (inteiro)
print(lista)
print(len(lista)) #len() retorna o tamanho
lista.sort() #parâmetro: reverse=False ou reverse=True

#slicing: "cortar" uma lista
lista[a:b:c] #começa no index a, vai até o index b (não incluso), pulando de c em c; por padrão, a=0, b=strlen(lista), c=1
```
- set(): elimina elementos repetidos
- tupla: não pode ter seus valores alterados
- dicionário: hash/senha -> cada valor é acessado por uma senha
    - cada chave contém um valor (qualquer tipo de dado)
    - o valor da chave não pode mudar
```python
dicionario = {}
dicionario[1] = "1" #"1" é a chave
dicionario["1"] = 1
dicionario["lista"] = [1, 2, 3]
print(dicionario)

#1: "1"
#"1": 1
#"lista" = [1, 2, 3]
```