from nicegui import ui
import yfinance as yf



def get_ticker():
    ticker = text_input.value.upper()
    ui.notify(f"Ticker: {ticker}")
    stock_value = yf.Ticker(ticker)
    stock_value = stock_value.info
    company_name.set_text(stock_value['longName'])
    country.set_text(stock_value['country'])
    industry.set_text(stock_value['industry'])
    market.set_content(f"Market info (currently {stock_value['marketState']})")
    currency.set_text(stock_value['currency'])
    current_value.set_text(stock_value['regularMarketPrice'])
    day_high.set_text(stock_value['dayHigh'])
    day_low.set_text(stock_value['dayLow'])
    change.set_text(f"{stock_value['regularMarketChangePercent']}%")
    if stock_value['regularMarketChangePercent'] > 0:
        change.style('color: green')
    elif stock_value['regularMarketChangePercent'] < 0:
        change.style('color: red')
    market_cap.set_text(f'$ {stock_value['marketCap']}')
    div_yeld.set_text(f'{stock_value['dividendYield']}%')
    




    #ticker_label.set_text(stock_value['currentPrice'])



with ui.header(elevated=True).style('background-color: black'):
    ui.label('🎉 Welcome to Metriqo - Free for a limited time!')

dark = ui.dark_mode()
ui.switch('Dark mode').bind_value(dark)

with ui.card():
    ui.markdown("Welcome to Metriqo 🚀 ").style("font-weight: bold; font-size: 200%")

    with ui.row():
        text_input = ui.input(placeholder='Enter your ticker').props('autofocus')
        ui.button("Search", on_click=get_ticker)

ui.markdown("Company Info").style("font-weight: bold; font-size: 120%")


with ui.row():
    with ui.card():
        ui.label('Company name: ').style("font-weight: bold")
        company_name = ui.label('-')    
    with ui.card():
        ui.label('Country: ').style("font-weight: bold")
        country = ui.label('-')
    with ui.card():
        ui.label('Industry: ').style("font-weight: bold")
        industry = ui.label('-')
    with ui.card():
        ui.label('Currency: ').style("font-weight: bold")
        currency = ui.label('-')

market = ui.markdown("Market info").style("font-weight: bold; font-size: 120%")

with ui.row():
    with ui.card():
        with ui.row():
            with ui.column():
                ui.label('Current value: ').style("font-weight: bold")
                current_value = ui.label('-')
            with ui.column():
                with ui.row():
                    ui.label('Day High')
                    day_high = ui.label('-')
                with ui.row():
                    ui.label('Day Low')
                    day_low = ui.label('-')
    with ui.card():
        ui.label('Change: ').style("font-weight: bold")
        change = ui.label('-')

    with ui.card():
        ui.label('Market Cap: ').style("font-weight: bold")
        market_cap = ui.label('-')

    with ui.card():
        ui.label('Dividend Yeld: ').style("font-weight: bold")
        div_yeld = ui.label('-')

ui.label("The stock data is provided for free by Yahoo! Finance, using the library yfinance.")
ui.label("Metriqo is not affiliated, endorsed, or vetted by Yahoo, Inc nor by yfinance.")


ui.run(title='Metriqo', favicon='🚀')




