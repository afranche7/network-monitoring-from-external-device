import asyncio
import speedtest
from dataclasses import dataclass
from ping3 import ping
from concurrent.futures import ThreadPoolExecutor


class NetworkMonitor(object):
    def __init__(self):
        self.ping_count = 3
        self.sites = ["google.com", "facebook.com", "twitter.com", "youtube.com", "amazon.com"]

        self.speed_metrics = None
        self.ping_metrics = None

    async def analyze(self):
        await asyncio.gather(
            self.__get_ping_stats(),
            self.__get_speed_stats()
        )

    async def __get_ping_stats(self):
        results = await asyncio.gather(
            *(self.__ping_site(site) for site in self.sites)
        )

        latencies = [rtt for site_latencies, _ in results for rtt in site_latencies]
        loss_count = sum(loss for _, loss in results)

        if latencies:
            latency = sum(latencies) / len(latencies)
            jitter = max(latencies) - min(latencies)
        else:
            latency = jitter = 0

        packet_loss = (loss_count / (self.ping_count * len(self.sites)) * 100)

        self.ping_metrics = PingMetrics(
            avg_latency=latency,
            avg_jitter=jitter,
            avg_packet_loss=packet_loss,
        )

    async def __ping_site(self, site: str):
        latencies = []
        loss_count = 0

        for _ in range(self.ping_count):
            rtt = ping(site)
            if rtt is None:
                loss_count += 1
            else:
                latencies.append(rtt)
        return latencies, loss_count

    async def __get_speed_stats(self):
        loop = asyncio.get_running_loop()
        with ThreadPoolExecutor() as executor:
            self.speed_metrics = await loop.run_in_executor(executor, self.__speed_test)

    def __speed_test(self):
        st = speedtest.Speedtest()

        st.get_best_server()

        # Convert to Mbps
        return SpeedMetrics(
            download_speed=st.download() / 1_000_000,
            upload_speed=st.upload() / 1_000_000,
        )


@dataclass
class SpeedMetrics:
    download_speed: float
    upload_speed: float


@dataclass
class PingMetrics:
    avg_latency: float
    avg_packet_loss: float
    avg_jitter: float
