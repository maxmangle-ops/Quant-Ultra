from risk.risk_manager import calculate_position
from paper.paper_trader import PaperTrader

trade = calculate_position(
    entry_price=1094.20,
    atr=1.74
)

paper = PaperTrader()

paper.buy(
    symbol="INFY",
    entry=trade["Entry"],
    stop_loss=trade["StopLoss"],
    target=trade["Target"],
    quantity=trade["Quantity"]
)