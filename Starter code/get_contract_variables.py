#0x669Ee7f0BfA6BC3D0F932aB22c107FCC7cB9e288

import os
import json
from web3 import Web3
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
os.chdir('/Users/michaeldionne/Documents/GitHub/Group Projects/Group Project # 3_Rock_Paper_scissors/Starter code/')
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545/'))

@st.cache(allow_output_mutation=True)
def load_contract():

    with open(Path('coinflip_abi.json')) as f:
        contract_abi = json.load(f)

    contract_address = os.getenv('CURRENT_CONTRACT_ADDRESS')

    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi,
    )
    return contract 

contract = load_contract()

# create the coinflip game in streamlit
st.title('Coinflip')
st.write('Welcome to the coinflip game.The rules are simple. You can choose to bet on heads or tails. If you win, you get double your bet. If you lose, you lose your bet. Good luck!')

st.write('Please select your bet amount in ether.')
st.write('The minimum bet is 1 and the maximum bet is 100')
bet_amount = st.number_input('Bet Amount', value=0, step=1)

bet_min = contract.functions.BET_MIN().call()
bet_max = contract.functions.BET_MAX().call()




if bet_amount < bet_min:
    st.write('Bet amount is too low. Please bet at least 1 ether.')
elif bet_amount > bet_max:
    st.write('Bet amount is too high. Please bet at most 100 ether.')
else:
    st.write('Please select heads or tails.')
    bet_choice = st.selectbox('Bet Choice', options=['Heads', 'Tails'])
    if st.button('Place Bet'):
        if bet_choice == 'Heads':
            bet_choice = 0
        else:
            bet_choice = 1
        contract.functions.initialBet(bet_choice).transact({"from": w3.eth.accounts[0], "gasPrice": w3.eth.gas_price, "value": w3.toWei(bet_amount, "ether")})  
        st.write('Bet placed. Please wait for the result.')
        st.write('The result is: ', contract.functions.result().call())
        st.write('The winning side is: ', contract.functions.winningSide().call())
        st.write('The winning amount is: ', contract.functions.winningAmount().call())
        st.write('The losing amount is: ', contract.functions.losingAmount().call())
        st.write('The contract balance is: ', contract.functions.getContractBalance().call())
    


contract_balance = contract.functions.getContractBalance().call()
initial_bet = contract.functions.initialBet().call()
house_played = contract.functions.housePlayed().call()
player_played = contract.functions.playerPlayed().call()
player_choice = contract.functions.playerChoice().call()
random_number = contract.functions.randomNum().call()
outcome = contract.functions.outcome().call()
paid = contract.functions.paid().call()



print('------------------------------')

print(f'minimum bet: {bet_min}')
print(f'maximum bet: {bet_max}')
print(f'initial bet: {initial_bet}')
print(f'contract balance: {contract_balance}')
print(f'house played status: {house_played}')
print(f'player played status: {player_played}')
print(f'player choice: {player_choice}')
print(f'random number: {random_number}')
print(f'outcome : {outcome}')
print(f'winner was paid: {paid}')

