bill = float(input('Quanto deu a conta? R$'))
tip = int(input('Quanto de gorjeta você quer dar? 10%, 12% ou 15?'))
people = int(input('Com quantas pessoas você quer dividir a  conta?'))
pay = (bill / people) * (tip / 100 + 1)
pay = round(pay, 2)
print(f'Cada pessoa deve pagar R$ {pay}')