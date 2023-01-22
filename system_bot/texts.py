
start_msg = """
<b>Welcome</b>

You are in an anonymous payment bot.
Want to hide income? Or send money without a trace?
This bot allows you to make instant payments anywhere in the world, encrypted with double encryption.
The wallet number can be changed at any time.

💳 <b>Balance:</b> <code>{balance}</code>$
🏦 <b>Wallet address:</b> <code>{wallet_id}</code>
Filling and withdrawing from the account - in Bitcoin only.

<b>Already with us:</b> {fake_peoples_num} people
"""

add_money_msg = """
<b>Balance top-up</b>

💳 Your current balance: {balance}$

<b>Send the desired amount to the following bitcoin wallet:</b>
<code>{btc_address}</code>

<b>Pay attention!</b>
For security reasons, with each top-up the address of the Bitcoin wallet to top up the account changes.
In no case do not set up automatic payment for any of the addresses, otherwise you risk losing your money.
"""

payment_done_msg = """
<b>Payment completed successfully</b>

Your payment has been received and the money is credited.
You can send the /start command to the bot and verify that the amount added to your account is correct
"""

send_money_amount_msg = """
<b>Sending money</b>

⚠️ Enter your preferred amount to transfer.

Attention!
Due to the large number of mixers in use and referrals to different wallets (this is how the system disrupts data), the network fee is 4-6%.
Keep this in mind when entering the amount to transfer

"""

send_money_address_msg = """
<b>Sending money</b>

⚠️ Specify the address of the AnonymousBank account to which you want to send this money.

Attention!
Transfer is possible only between anonymous bank accounts.

"""

error_only_num_msg = """
<b>Error</b>

Only numbers are allowed at this time.
"""


error_big_num_msg = """
<b>Error</b>

You are trying to send more than you actually have
"""


money_sended_msg = """
<b>The money has been sent successfully</b>

The money has been sent successfully, and in a few seconds it will appear in the recipient's account.

Send the /start command to the bot to return to the main menu
"""

error_only_wallet_msg = """
<b>Error</b>

Invalid recipient address format
"""

insert_output_withrow_mount_msg = """
<b>Withdrawals</b>

⚠️ Specify the amount to withdraw (in dollars)

"""


value_to_withrow_msg = """
<b>Withdrawals</b>

⚠️ Specify the address of the bitcoin wallet to withdraw
"""

money_withrow_sended_msg = """
<b>Withdrawals</b>

The money is sent to the specified bitcoin wallet.

<b>Transaction code:</b>
<code>{tr_id}</code>
"""

message_id_changed_msg = "Wallet ID successfully changed"


admin_panel_msg = """
<b>Management panel</b>

Total balance: {total_admin_balance}$
Actual number of users: {subs_num}
"""


#### BUTTONS ####
send_money_btn = "💸 Send"
add_money_btn = "📥 Deposit"
withrow_btn = "📤 Сash out"
change_wallet_id_btn = "🛡️ Change Wallet ID"