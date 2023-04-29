from market.glassnode.provider import Glassnode


class GlassnodeBlockchain(Glassnode):
    def get_block_count(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/blockchain/block_count"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_block_height(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/blockchain/block_height"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_block_interval_mean(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/blockchain/block_interval_mean"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_block_interval_median(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/blockchain/block_interval_median"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_block_size_mean(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/blockchain/block_size_mean"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})

    def get_block_size_total(self, asset: str, start_date: int, end_date: int):
        url = "v1/metrics/blockchain/block_size_sum"

        return self.send_api_request("GET", url, {"a": asset, "s": start_date, "u": end_date})
