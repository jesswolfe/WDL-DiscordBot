player_totals_column_names = ["nick", "rat", "orat",
                              "drat", "eff", "frags",
                              "kdr", "dmg", "def",
                              "pow", "touches", "ptouches",
                              "caps", "pcaps", "points",
                              "cap%", "assists", "win%",
                              "rp", "gp"]


season_column_names = ["nick", "rat", "orat",
                       "drat", "eff", "frags",
                       "kdr", "dmg", "def",
                       "pow", "touches", "ptouches",
                       "caps", "pcaps", "points",
                       "cap%", "rp", "gp"]

alltime_playoff_column_names = ["nick", "rat", "orat",
                                "drat", "eff", "frags",
                                "kdr", "dmg", "def",
                                "pow", "touches", "ptouches",
                                "caps", "pcaps", "points",
                                "cap%", "win%", "rp", "gp"]

all_rounds_column_names = ["nick", "team", "rat",
                           "orat", "drat", "eff",
                           "frags", "deaths", "dmg",
                           "def", "pow", "touch",
                           "ptouches", "caps", "pcaps",
                           "assists", "cap%", "res",
                           "kdr", "id", "sid"]

team_stats_column_names = ["team", "rat", "orat",
                           "drat", "deaths", "eff",
                           "frags", "dmg", "kdr",
                           "pow", "touches", "ptouches",
                           "caps", "pcaps", "points",
                           "assists", "cap%", "win%",
                           "rp", "gp", "season",
                           "eff2", "def2", "spoints",
                           "wins", "losses", "ties"]

stat_dict = {"rat": "RAT",
             "orat": "oRAT",
             "drat": "dRAT",
             "frags": "Frags",
             "eff": "EFF",
             "kdr": "K/D",
             "dmg": "DMG",
             "def": "DEF",
             "pow": "POW",
             "touches": "Touches",
             "ptouches": "PTouches",
             "caps": "Caps",
             "pcaps": "PCaps",
             "points": "Points",
             "assists": "Assists",
             "cap%": "Cap%",
             "win%": "Win%",
             "season": "Season",
             "wins": "Wins",
             "losses": "Losses",
             "ties": "Ties",
             "deaths": "Deaths"
             }

team_dict = {1: "ADD 1", 2: "SUC 1", 3: "SDC 1",
             4: "TMC 1", 5: "SUP 1", 6: "SHQ 1",
             7: "SUC 2", 8: "GPS 2", 9: "WUM 2",
             10: "SDC 2", 11: "NSP 2", 12: "SSG 2",
             13: "SUC 3", 14: "SDC 3", 15: "CDC 3",
             16: "GPS 3", 17: "TDT 3", 18: "REG 3",
             19: "SUC 4", 20: "DEA 4", 21: "REG 4",
             22: "OVS 4", 23: "GPS 4", 24: "SXP 4",
             25: "SUC 5", 26: "GPS 5", 27: "SXP 5",
             28: "TDT 5", 29: "WUM 5", 30: "BST 5",
             32: "SDM 6", 33: "SUC 6", 34: "SXP 6",
             35: "CDC 6", 36: "TDT 6", 37: "GPS 6",
             38: "SUC 7", 39: "GPS 7", 40: "HYP 7",
             41: "TDT 7", 42: "HFM 7", 43: "SXP 7",
             44: "TKV 7", 45: "REG 7"
             }

team_dict_inverse = {a: b for b, a in team_dict.items()}

team_dict_two = {"!add": "Adderall Drunk Drivers",
                 "!suc": "Super Chargers",
                 "!sdc": "Stardust Crusaders",
                 "!shq": "Shaq Fu",
                 "!tmc": "The Mall Cops",
                 "!sup": "SuperBots",
                 "!wum": "Wumbologists",
                 "!gps": "Giant Pea Shooters",
                 "!nsp": "None Shall Pass",
                 "!ssg": "Sunday School Gangsters",
                 "!cdc": "Capo Dont Care",
                 "!tdt": "The Dream Team",
                 "!reg": "The Regulators",
                 "!dea": "Doom Enforcement Agency",
                 "!sxp": "Sexual Panthers",
                 "!ovs": "OverratedScumWads",
                 "!bst": "Best Ever",
                 "!sdm": "Super Dank Memes",
                 "!tkv": "Techno Vikings",
                 "!hfm": "High Friction Men",
                 "!hyp": "Hurt You Plenty"
                 }