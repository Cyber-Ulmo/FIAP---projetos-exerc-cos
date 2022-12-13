print("eai maluco digita essa porra ai")

quantia = int(input("Digite a quantia desejada ao saque: "))

ced50 = quantia // 50
quantia = quantia % 50
ced20 = quantia // 20
quantia = quantia % 20
ced10 = quantia // 10
quantia = quantia % 10
ced05 = quantia // 5
quantia = quantia % 5

print(f"quantidade de cédulas de 50: {ced50}")
print(f"quantidade de cédulas de 20: {ced20}")
print(f"quantidade de cédulas de 10: {ced10}")
print(f"quantidade de cédulas de 05: {ced05}")