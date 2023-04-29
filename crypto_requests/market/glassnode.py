from market.glassnode.provider import Glassnode


class GlassnodeMarket(Glassnode):
    def get_price(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/price_usd_close"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_market_cap(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/marketcap_usd"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_realized_cap(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/marketcap_usd"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_mvrv(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/mvrv"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_mvrv_short_term(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/mvrv_less_155"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_mvrv_long_term(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/mvrv_more_155"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_mvrv_z_score(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/mvrv_z_score"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_price_drawdown(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/price_drawdown_relative"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_realized_price(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/price_realized_usd"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_realized_volatility(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/realized_volatility_all"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_realized_volatility_1_month(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/realized_volatility_1_month"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_realized_volatility_1_week(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/realized_volatility_1_week"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_realized_volatility_1_year(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/realized_volatility_1_year"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_realized_volatility_3_month(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/realized_volatility_3_months"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_realized_volatility_6_month(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/market/realized_volatility_6_months"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})
