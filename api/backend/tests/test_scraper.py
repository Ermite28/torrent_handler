from apis.torrent_handler.scraping import Scrapper

class TestScrapper():
    torrents_query = {
            "adult": False,
            "backdrop_path": "/nNmJRkg8wWnRmzQDe2FwKbPIsJV.jpg",
            "genre_ids": [
                878,
                28,
                12
            ],
            "id": 24428,
            "original_language": "en",
            "original_title": "The Avengers",
            "overview": "When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!",
            "popularity": 250.896,
            "poster_path": "/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
            "release_date": "2012-04-25",
            "title": "The Avengers",
            "video": False,
            "vote_average": 7.7,
            "vote_count": 26872
        }
    torrents_good_reponse = {
      "url": "https://yts.mx/movies/the-avengers-2012",
      "name": "The Avengers",
      "date": "2012",
      "genre": [
        "Action ",
        " Adventure ",
        " Sci-Fi ",
        " Thriller"
      ],
      "rating": "8",
      "poster": "https://img.yts.mx/assets/images/movies/The_Avengers_2012/large-cover.jpg",
      "description": "S.H.I.E.L.D. has located the mysterious Tesseract device and the Army's super soldier Captain America. The Tesseract is actually a gateway to an entirely new world called Asgard. A mysterious being known as Loki arrives on earth and immediately assumes that he can rule all human beings. But that irks S.H.I.E.L.D. director Nick Fury the wrong way. As Loki escapes with the Tesseract, Nick Fury believes this is an act of war against Earth. His only hope is to assemble an actual team of super heroes. Dr. Bruce Banner, who turns into an enormous green rage monster known as the Hulk. Tony Stark and his venerable Iron Man armor. Captain America, the Stark Enterprises created super soldier. Thor, the god of thunder, protector of Earth and his home planet of Asgard, and Loki's brother. Master assassins Hawkeye and Natasha Romanoff. Together they will become a team to take on an attack that will call them to become the greatest of all time.",
      "runtime": "2 hr 23 min",
      "screenshot": [
        "https://img.yts.mx/assets/images/movies/The_Avengers_2012/large-screenshot1.jpg",
        "https://img.yts.mx/assets/images/movies/The_Avengers_2012/large-screenshot2.jpg",
        "https://img.yts.mx/assets/images/movies/The_Avengers_2012/large-screenshot3.jpg"
      ],
      "torrents": [
        {
          "quality": "3D",
          "type": "BluRay",
          "size": "2.30 GB",
          "torrent": "https://yts.mx/torrent/download/37CEF1CEF6F1526FE78611C01B7665BDF007F582",
          "magnet": "magnet:?xt=urn:btih:37CEF1CEF6F1526FE78611C01B7665BDF007F582&dn=The+Avengers+%282012%29+%5B3D%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337",
          "hash": "37CEF1CEF6F1526FE78611C01B7665BDF007F582"
        },
        {
          "quality": "720p",
          "type": "BluRay",
          "size": "1023.32 MB",
          "torrent": "https://yts.mx/torrent/download/0BBCA7584749D4E741747E32E6EB588AEA03E40F",
          "magnet": "magnet:?xt=urn:btih:0BBCA7584749D4E741747E32E6EB588AEA03E40F&dn=The+Avengers+%282012%29+%5B720p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337",
          "hash": "0BBCA7584749D4E741747E32E6EB588AEA03E40F"
        },
        {
          "quality": "1080p",
          "type": "BluRay",
          "size": "2.20 GB",
          "torrent": "https://yts.mx/torrent/download/E9F759B6A26113F3745311DAD4BD332B4612EB60",
          "magnet": "magnet:?xt=urn:btih:E9F759B6A26113F3745311DAD4BD332B4612EB60&dn=The+Avengers+%282012%29+%5B1080p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337",
          "hash": "E9F759B6A26113F3745311DAD4BD332B4612EB60"
        },
        {
          "quality": "2160p",
          "type": "BluRay",
          "size": "6.56 GB",
          "torrent": "https://yts.mx/torrent/download/86F2F3368399E4262C18FDAFA15509270BA32333",
          "magnet": "magnet:?xt=urn:btih:86F2F3368399E4262C18FDAFA15509270BA32333&dn=The+Avengers+%282012%29+%5B2160p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce",
          "hash": "86F2F3368399E4262C18FDAFA15509270BA32333"
        }
      ]
    }
    torrents_medium_response = {
      "url": "https://yts.mx/movies/captain-america-the-first-avenger-2011",
      "name": "Captain America: The First Avenger",
      "date": "2011",
      "genre": [
        "Action ",
        " Adventure ",
        " Sci-Fi"
      ],
      "rating": "6.9",
      "poster": "https://img.yts.mx/assets/images/movies/Captain_America_The_First_Avenger_2011/large-cover.jpg",
      "description": "During World War 2, Steve Rogers tries to enlist but is repeatedly rejected for his frail and sickly condition, however a scientist notes his determination and allows him to be accepted. What Steve doesn't know is that this scientist is in charge of a government project to create super soldiers, in which Steve is to be the first, but the colonel in charge of the project can't see what the scientist does in this scrawny runt - a strong inner character. Meanwhile, Johann Schmidt, head of a German science division known as HYDRA, knows this scientist and fears the success of his project in America. It could mean trouble for the Germans, so he sends a man to infiltrate and see if it's a success, and \"take care\" of the scientist if it is. It is, and he does, but not without Steve and his new abilities chasing him down. With the doctor dead, no more American supermen will be forthcoming, and Steve quickly becomes a mere U.S. war drive propaganda tool called \"Captain America.\" His role is useful, if undignified, but he soldiers on with it dutifully till hearing of his best friend's unit's capture, for which he promptly heads out to rescue them. During this rescue, he meets the diabolical Schmidt, and the two become each other's arch nemesis.",
      "runtime": "2 hr 4 min",
      "screenshot": [
        "https://img.yts.mx/assets/images/movies/Captain_America_The_First_Avenger_2011/large-screenshot1.jpg",
        "https://img.yts.mx/assets/images/movies/Captain_America_The_First_Avenger_2011/large-screenshot2.jpg",
        "https://img.yts.mx/assets/images/movies/Captain_America_The_First_Avenger_2011/large-screenshot3.jpg"
      ],
      "torrents": [
        {
          "quality": "3D",
          "type": "BluRay",
          "size": "1.80 GB",
          "torrent": "https://yts.mx/torrent/download/D19276E444F84EB8889F1C15145C3F1C245263E7",
          "magnet": "magnet:?xt=urn:btih:D19276E444F84EB8889F1C15145C3F1C245263E7&dn=Captain+America%3A+The+First+Avenger+%282011%29+%5B3D%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337",
          "hash": "D19276E444F84EB8889F1C15145C3F1C245263E7"
        },
        {
          "quality": "720p",
          "type": "BluRay",
          "size": "756.52 MB",
          "torrent": "https://yts.mx/torrent/download/907C44FABBB0A57A169B6FF465579ED69EEC71FF",
          "magnet": "magnet:?xt=urn:btih:907C44FABBB0A57A169B6FF465579ED69EEC71FF&dn=Captain+America%3A+The+First+Avenger+%282011%29+%5B720p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337",
          "hash": "907C44FABBB0A57A169B6FF465579ED69EEC71FF"
        },
        {
          "quality": "1080p",
          "type": "BluRay",
          "size": "1.60 GB",
          "torrent": "https://yts.mx/torrent/download/25AA732E39DB228AA7989EE66CC487C914AEBF40",
          "magnet": "magnet:?xt=urn:btih:25AA732E39DB228AA7989EE66CC487C914AEBF40&dn=Captain+America%3A+The+First+Avenger+%282011%29+%5B1080p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337",
          "hash": "25AA732E39DB228AA7989EE66CC487C914AEBF40"
        },
        {
          "quality": "2160p",
          "type": "BluRay",
          "size": "6.45 GB",
          "torrent": "https://yts.mx/torrent/download/8D921398C2D0E6BE52E4547E337F9E8CF4269460",
          "magnet": "magnet:?xt=urn:btih:8D921398C2D0E6BE52E4547E337F9E8CF4269460&dn=Captain+America%3A+The+First+Avenger+%282011%29+%5B2160p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce",
          "hash": "8D921398C2D0E6BE52E4547E337F9E8CF4269460"
        }
      ]
    }
    torrents_bad_response = {
            "url": "https://yts.mx/movies/knives-of-the-avenger-1966",
            "name": "Knives of the Avenger",
            "date": "1966 [ITALIAN]",
            "genre": [
                "Adventure"
            ],
            "rating": "5.7",
            "poster": "https://img.yts.mx/assets/images/movies/knives_of_the_avenger_1966/large-cover.jpg",
            "description": "In the ancient times, the savage and cruel warrior Hagen is chasing Queen Karin and her son Moki to marry her and usurp the kingdom of her husband, King Arald. Karin and Moki are hidden in a cottage in the woods, living like peasants. They are protected by a stranger, the warrior Helmut, a knives expert. Moki grows close to Helmut who teaches him how to hunt and fight. Later Karin discloses to him that three years ago, her husband traveled in a ship overseas to seek grains for his starving people. The vessel was wrecked on the coast of Britain and since then they have heard nothing about Arald. Furthermore she tells him that Hagen was responsible for the starvation since braking the truce between the kingdoms of Arald and King Rurik and killed his wife and son. Thirsty for revenge, King Rurik had invaded her kingdom with his warriors, killed the people and raped the women including her on her honeymoon, but spared the life of Arald.",
            "runtime": "1 hr 24 min",
            "screenshot": [
                "https://img.yts.mx/assets/images/movies/knives_of_the_avenger_1966/large-screenshot1.jpg",
                "https://img.yts.mx/assets/images/movies/knives_of_the_avenger_1966/large-screenshot2.jpg",
                "https://img.yts.mx/assets/images/movies/knives_of_the_avenger_1966/large-screenshot3.jpg"
            ],
            "torrents": [
                {
                    "quality": "720p",
                    "type": "BluRay",
                    "size": "775.2 MB",
                    "torrent": "https://yts.mx/torrent/download/02A600CAC4773B5309F20B487B632709A541AAB7",
                    "magnet": "magnet:?xt=urn:btih:02A600CAC4773B5309F20B487B632709A541AAB7&dn=Knives+of+the+Avenger+%281966%29+%5B720p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce",
                    "hash": "02A600CAC4773B5309F20B487B632709A541AAB7"
                },
                {
                    "quality": "1080p",
                    "type": "BluRay",
                    "size": "1.4 GB",
                    "torrent": "https://yts.mx/torrent/download/47DFE937B64A155E1078E5E3C4A92FDE6B1A2F7A",
                    "magnet": "magnet:?xt=urn:btih:47DFE937B64A155E1078E5E3C4A92FDE6B1A2F7A&dn=Knives+of+the+Avenger+%281966%29+%5B1080p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce",
                    "hash": "47DFE937B64A155E1078E5E3C4A92FDE6B1A2F7A"
                }
            ]
        }
    
    def test_bad_score(self):
        assert 0 < Scrapper().get_score(self.torrents_query, self.torrents_bad_response) < 0.1
    
    def test_medium_score(self):
        assert 0.1 < Scrapper().get_score(self.torrents_query, self.torrents_bad_response) < 0.2
    
    def test_good_score(self):
        assert 0.9 < Scrapper().get_score(self.torrents_query, self.torrents_bad_response) < 1