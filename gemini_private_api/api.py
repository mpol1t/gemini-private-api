from base64 import b64encode
from hashlib import sha384
from hmac import new
from json import dumps
from time import time
from typing import Dict, Any

from requests import post

from gemini_private_api.private_endpoints import NEW_ORDER

BASE_URL: str = 'https://api.gemini.com'
BASE_SANDBOX_URL: str = 'https://api.sandbox.gemini.com'


class GeminiPrivateAPI:
    def __init__(self, gemini_api_key: str, gemini_api_secret: str):
        self.gemini_api_key: str = gemini_api_key
        self.gemini_api_secret: bytes = gemini_api_secret.encode()

    def _get_request_headers(self, encoded_payload: bytes, signature: str):
        return {
            'Content-Type':       "text/plain",
            'Content-Length':     "0",
            'X-GEMINI-APIKEY':    self.gemini_api_key,
            'X-GEMINI-PAYLOAD':   encoded_payload,
            'X-GEMINI-SIGNATURE': signature,
            'Cache-Control':      "no-cache"
        }

    @staticmethod
    def _get_nonce():
        return time()

    def _post(self, url: str, payload: Dict[str, Any]):
        encoded_payload: bytes = b64encode(dumps(payload).encode())
        signature: str = new(self.gemini_api_secret, encoded_payload, sha384).hexdigest()

        return post(
            url,
            data=None,
            headers=self._get_request_headers(
                encoded_payload,
                signature
            )
        )

    @classmethod
    def _update_options(cls, options):
        pass

    def new_order(
            self,
            symbol: str,
            amount: float,
            price: float,
            side: str,
            order_type: str,
            sandbox: bool = False,
            **kwargs
    ):
        return self._post(
            url=BASE_SANDBOX_URL if sandbox else BASE_URL,
            payload={
                'request': NEW_ORDER,
                'nonce':   self._get_nonce(),
                'symbol':  symbol,
                'amount':  str(amount),
                'price':   str(price),
                'side':    side,
                'type':    order_type,
                **kwargs
            }
        )

    def cancel_order(self):
        pass

    def wrap_order(self):
        pass

    def cancel_all_session_orders(self):
        pass

    def cancel_all_active_orders(self):
        pass

    def order_status(self):
        pass

    def get_active_orders(self):
        pass

    def get_past_trades(self):
        pass

    def get_notional_volume(self):
        pass

    def get_trade_volume(self):
        pass

    def fx_rate(self):
        pass

    def new_clearing_order(self):
        pass

    def new_broker_order(self):
        pass

    def clearing_order_status(self):
        pass

    def cancel_clearing_order(self):
        pass

    def confirm_clearing_order(self):
        pass

    def clearing_order_list(self):
        pass

    def clearing_broker_list(self):
        pass

    def clearing_trades(self):
        pass

    def get_available_balances(self):
        pass

    def get_notional_balances(self):
        pass

    def transfers(self):
        pass

    def transactions(self):
        pass

    def custody_account_fees(self):
        pass

    def get_deposit_address(self):
        pass

    def new_deposit_address(self):
        pass

    def withdraw_crypto_funds(self):
        pass

    def gas_fee_estimation(self):
        pass

    def internal_transfers(self):
        pass

    def add_bank(self):
        pass

    def add_bank_cad(self):
        pass

    def payment_methods(self):
        pass

    def sen_withdrawals(self):
        pass

    def get_earn_balances(self):
        pass

    def get_earn_rates(self):
        pass

    def get_earn_interest(self):
        pass

    def get_earn_history(self):
        pass

    def get_staking_balances(self):
        pass

    def get_staking_rates(self):
        pass

    def get_staking_rewards(self):
        pass

    def get_staking_history(self):
        pass

    def staking_deposits(self):
        pass

    def staking_withdrawals(self):
        pass

    def create_address_request(self):
        pass

    def view_approved_addresses(self):
        pass

    def remove_addresses_from_approved_address_list(self):
        pass

    def account_detail(self):
        pass

    def create_account(self):
        pass

    def rename_account(self):
        pass

    def get_accounts_in_master_group(self):
        pass

    def using_master_api_keys(self):
        pass

    def heartbeat(self):
        pass
