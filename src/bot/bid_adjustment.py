from bidding import BiddingBot

def adjust_bid(nft_id, user_max_bid):
    """
    Adjusts the user's bid for an NFT based on the current top bid.

    :param nft_id: str, The ID of the NFT to adjust the bid for.
    :param user_max_bid: float, The maximum amount the user is willing to bid.
    :return: float, The adjusted bid amount.
    """
    bot = BiddingBot()
    top_bid = bot.get_top_bid(nft_id)
    
    # Define the bid increment strategy
    increment = 1.0  # This can be adjusted based on strategy
    
    # Calculate the adjusted bid
    if top_bid + increment <= user_max_bid:
        adjusted_bid = top_bid + increment
        print(f"Adjusted bid for NFT {nft_id} is {adjusted_bid} SOL.")
        return adjusted_bid
    else:
        print(f"Cannot place bid. Top bid of {top_bid} SOL is too close to or exceeds user's max bid of {user_max_bid} SOL.")
        return None

# Example usage
if __name__ == "__main__":
    nft_id = "NFT123"
    user_max_bid = 105.0  # The user's maximum bid amount
    adjusted_bid = adjust_bid(nft_id, user_max_bid)
    if adjusted_bid:
        print(f"Placing adjusted bid of {adjusted_bid} SOL on {nft_id}.")
    else:
        print("Adjusted bid not placed due to max bid constraints.")
