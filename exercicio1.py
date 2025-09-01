preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o valor do desconto (0-100%): '))
desconto = preco * (percentual / 100)
final = preco - desconto

print(f' O preço do produto é {preco}. E o desconto é de {percentual}%')
print(f' E o preço do produto com desconto é de {final}')