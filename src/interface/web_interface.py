from flask import Flask, render_template, request, redirect, url_for
from bot.bidding import BiddingBot
from bot.listing import ListingBot
from bot.bid_adjustment import adjust_bid

app = Flask(__name__)

# Initialize the bots
bidding_bot = BiddingBot()
listing_bot = ListingBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list-nft', methods=['GET', 'POST'])
def list_nft():
    if request.method == 'POST':
        nft_id = request.form.get('nft_id')
        price = float(request.form.get('price'))
        seller_wallet = request.form.get('seller_wallet')
        listing_bot.list_nft(nft_id, price, seller_wallet)
        return redirect(url_for('index'))
    return render_template('list_nft.html')

@app.route('/place-bid', methods=['GET', 'POST'])
def place_bid():
    if request.method == 'POST':
        nft_id = request.form.get('nft_id')
        bid_amount = float(request.form.get('bid_amount'))
        bidding_bot.place_bid(nft_id, bid_amount)
        return redirect(url_for('index'))
    return render_template('place_bid.html')

@app.route('/adjust-bid', methods=['GET', 'POST'])
def adjust_bid_route():
    if request.method == 'POST':
        nft_id = request.form.get('nft_id')
        user_max_bid = float(request.form.get('user_max_bid'))
        adjusted_bid = adjust_bid(nft_id, user_max_bid)
        if adjusted_bid is not None:
            bidding_bot.place_bid(nft_id, adjusted_bid)
        return redirect(url_for('index'))
    return render_template('adjust_bid.html')

if __name__ == '__main__':
    app.run(debug=True)
