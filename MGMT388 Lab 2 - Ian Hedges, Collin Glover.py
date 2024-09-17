# Ian Hedges and Collin Glover
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:32:07 2024

@author: ianhedges
"""
# Function for adding an asset

def add_asset(portfolio, name, quantity, purchase_price, current_price):
    portfolio[name] = {
        'quantity': quantity,
        'purchase_price': purchase_price,
        'current_price': current_price
    }
    
    
    
# Function to update asset price
def update_price(portfolio, name, price):
    portfolio[name]['current_price'] = price
    print('Market price for', name, 'has been changed to $', portfolio[name]['current_price'])
    
# Function to print portfolio summary

def print_portfolio(portfolio):
    print("Portfolio:")
    for asset, details in portfolio.items():
        print(f"{asset}: \n Quantity: {details['quantity']} \n Purchase Price: ${details['purchase_price']} \n Current Price: ${details['current_price']} \n Asset Value:", '$' + str(float(details['current_price'])*float(details['quantity'])), '\n')
    print()
    
    
    
# Function to make new line more readable

def line():
    print('\n')
    
    
    
    
# Function to call add asset prompt

def add_asset_prompt():
    print('You have chosen to add an asset to your portfolio', '\n'*2)
    
    print('Enter asset name:', '\n')

    AssetName = input()

    line()


    print('Enter asset quantity:', '\n')

    AssetQuantity = input()

    line()

    print('Enter purchase price of the asset:', '\n')

    AssetPurPrice = input ()

    line()

    print('Enter current market price of the asset:', '\n')

    AssetMktPrice = input()

    line()

    try:
        add_asset(portfolio, AssetName, AssetQuantity, AssetPurPrice, AssetMktPrice)
    except ValueError:
        print('Value error: There may be non-numeric values in numeric categories')
    
    
    
# Function to calculate the total portfolio value

def portfolio_value():
    global total_value
    total_value = 0
    for asset in portfolio.keys():
           asset_value = float(portfolio[asset]['current_price']) * float(portfolio[asset]['quantity'])
           total_value = total_value + asset_value

        
    
    
    
# Function for return on investment

def roi():
    purchase_value = 0
    current_value = 0
    for asset in portfolio.keys():
        purchase_value = purchase_value + float(portfolio[asset]['purchase_price']) * float(portfolio[asset]['quantity'])
        current_value = current_value + float(portfolio[asset]['current_price']) * float(portfolio[asset]['quantity'])
    roi = ((current_value - purchase_value) / purchase_value) * 100
    print('Return on Investment (ROI) = %', round(roi,ndigits=2))
    

# Function for asset allocation percentage
    
def asset_allocation():
    print('Asset allocation:')
    total_value = 0
    for asset in portfolio.keys():
        asset_value = float(portfolio[asset]['current_price']) * float(portfolio[asset]['quantity'])
        total_value = total_value + asset_value
    for asset in portfolio.keys():
        asset_allocation = ((float(portfolio[asset]['current_price']) * float(portfolio[asset]['quantity'])) / total_value) * 100
        print(f" {asset}:", str(round(asset_allocation, ndigits=2)) + '%')
        
        
        
        
# Function for assist optimization

def asset_value(portfolio, name, current_value):
    global optimal_portfolio
    optimal_portfolio[name] = current_value

# Function for portfolio optimization

def optimization():
    print('The top contributors to portfolio value are: \n')
    portfolio_value()
    global total_value
    global optimal_portfolio
    current_value = 0
    cum_percentage = 0
    selected_assets = {}
    
    for asset in portfolio.keys():
        current_value = float(portfolio[asset]['current_price']) * float(portfolio[asset]['quantity'])
        asset_value(portfolio, asset, current_value)
    
    
    optimal_portfolio = dict(sorted(optimal_portfolio.items(),key=lambda item: item[1], reverse = True))
    
    
    current_value = 0
    
    for asset in optimal_portfolio.keys():
        current_value = current_value + float(optimal_portfolio[asset])
        cum_percentage =  float(current_value) / float(total_value)
        single_percentage = float(optimal_portfolio[asset]) / float(total_value)
        if cum_percentage >= 0.50:
            print(f'{asset}:', round(single_percentage *100, ndigits=2), '%')
            print('\n These assets make up the top', round(cum_percentage * 100, ndigits=2),'% of the portfolio')
            break
        else:
            selected_assets[asset] = single_percentage * 100
            print(f'{asset}:',  round(single_percentage * 100, ndigits=2), '%')
            
            
    
        



portfolio = {}
optimal_portfolio = {}
    
add_asset(portfolio, 'Stock A', quantity=100, purchase_price=50, current_price=60)
add_asset(portfolio, 'Stock B', quantity=200, purchase_price=30, current_price=35)
add_asset(portfolio, 'Stock C', quantity=150, purchase_price=45, current_price=40)
add_asset(portfolio, 'Stock D', quantity=300, purchase_price=25, current_price=50)

view_portfolio = "1"


while view_portfolio == '1':
    
    print('What action do you want to perform?', '\n', 'Please enter the corresponding number for your choice', '\n')
    
    print('(1) View portfolio', '\n', '(2) Add asset to portfolio', '\n', '(3) Update asset prices', '\n', '(4) View portfolio metrics', '\n', '(5) Show portfolio optimization', '\n', '(6) Error help')

    line()
    
    portfolio_action = input()
    
    line()
    
    if portfolio_action == "1":
        
        print('You have chosen to view your portfolio', '\n'*2)
        
        print_portfolio(portfolio)

        
    elif portfolio_action == "2":
        
        add_asset_prompt()
        
        
    elif portfolio_action == "3":
    
        print('Update the current market price of an asset', '\n')
        print('Enter asset name:')
        name = input()
        line()
        print('Enter new price:')
        price = input()
        line()
        try: 
            update_price(portfolio, name, price)
        except KeyError:
            print('Key error - Asset entered does not exist')
        
    elif portfolio_action == "4":
        
        print('You have chosen to view your portfolio metrics', '\n')
        
        try:
            portfolio_value()
            print('Total value: $', total_value)
        except ValueError:
            print('Portfolio Value unavailable - Value error encountered')
        try: 
            roi()
        except ValueError:
            print('ROI unavailable - Value error encountered')
        try: 
            asset_allocation()
        except ValueError:
            print('Asset allocation - Value error encountered')
        
        
    elif portfolio_action == "5":
    
        print('You have chosen to view your portfolio optimization', '\n'*2)
        
        try:
            optimization()
        except ValueError:
            print('\n Value error - unable to compute', '\n'*2, 'Asset may have non-numeric data causing an error')
    
    elif portfolio_action == "6":
        print('"Value Error" - If a value rror is encountered, you most likely have a letter/character or word in a numeric variable \n To fix this, use the add asset option (2) and enter the asset name and enter the correct values')
        print('\n','"Key Error" - The asset name entered does not exist in the portfolio \n To fix, check spelling and if spelling is correct, you may need to add the asset using the add asset (2) option')
        
    else:
        print('You have entered an invalid selection, please follow the prompt to return to the menu.')

    
    line()
    
    print('Would you like to continue viewing your portfolio?', '\n'*2, 'Type "1" to continue viewing or type anything else to exit', '\n')
    
    view_portfolio = input()
    
    line()
    
print('You have exited your portfolio.')
          
          
          
          
          
          
          
          
