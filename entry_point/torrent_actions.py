from transmission_rpc import client


class TorrentActions:
    def __init__(self, username=None, password=None, host="127.0.0.1", download_dir=None) -> None:
        self.client = client.Client(username=username, password=password, host=host)
        self.download_dir = download_dir

    def add_torrent(self, magnet, download_dir=None, **kwargs) -> None:
        if not download_dir:
            download_dir = self.download_dir
        print(kwargs)
        self.client.add_torrent(magnet, download_dir=download_dir)
