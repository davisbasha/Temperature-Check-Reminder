temperature=int(input('Enter the Temperature: '))
print(temperature)
if temperature<59:
    print('Activate the heating system')
    print('Check again in 5 minutes')
elif temperature>=59 and temperature<=77:
    print('No action is needed, temperature is in ideal range')
    print('Check again in 15 minutes')
else:
    print('Turn on the water sprinklers')
    print('Check again in 5 minutes')