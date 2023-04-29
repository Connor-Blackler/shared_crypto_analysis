from market.glassnode.provider import Glassnode


class GlassnodeIndicator(Glassnode):
    def get_mvrv_account_based(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/indicators/mvrv_account_based"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_sopr(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/indicators/sopr"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_entity_adjusted_nupl(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/indicators/net_unrealized_profit_loss_account_based"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_puell_multiple(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/indicators/puell_multiple"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_relative_unrealized_profit(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/indicators/unrealized_profit"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_relative_unrealized_loss(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/indicators/unrealized_loss"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_liveliness(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/indicators/liveliness"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})
