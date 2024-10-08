try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos problemas com os dados digitados, revise-os e tente novamente.')
except ZeroDivisionError:
    print("Não é possível dividir um valor por 0")
except KeyboardInterrupt:
    print("\nNão foi digitado nenhum valor.")
except Exception as erro:
    print(f"Não foi possível realizar os calculos. Erro {erro.__cause__}")
else:
    print(f"O resultado é {r:.2f}")
finally:
    print("Volte sempre! Muito obrigado!")



