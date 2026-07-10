COUNTRY_ALIASES = {
    # United States
    "usa": "US",
    "u.s.a": "US",
    "u.s.": "US",
    "us": "US",
    "america": "US",
    "united states": "US",
    "united states of america": "US",

    # United Kingdom
    "uk": "GB",
    "u.k.": "GB",
    "britain": "GB",
    "great britain": "GB",
    "england": "GB",
    "united kingdom": "GB",

    # UAE
    "uae": "AE",
    "u.a.e.": "AE",
    "emirates": "AE",
    "united arab emirates": "AE",
    "dubai": "AE",
    "abu dhabi": "AE",

    # Asia
    "india": "IN",
    "japan": "JP",
    "china": "CN",
    "south korea": "KR",
    "korea": "KR",
    "north korea": "KP",
    "singapore": "SG",
    "malaysia": "MY",
    "thailand": "TH",
    "indonesia": "ID",
    "vietnam": "VN",
    "philippines": "PH",
    "taiwan": "TW",
    "hong kong": "HK",
    "macau": "MO",
    "nepal": "NP",
    "bhutan": "BT",
    "bangladesh": "BD",
    "pakistan": "PK",
    "sri lanka": "LK",
    "myanmar": "MM",
    "cambodia": "KH",
    "laos": "LA",
    "mongolia": "MN",

    # Middle East
    "qatar": "QA",
    "saudi arabia": "SA",
    "oman": "OM",
    "kuwait": "KW",
    "bahrain": "BH",
    "israel": "IL",
    "jordan": "JO",
    "iran": "IR",
    "iraq": "IQ",
    "lebanon": "LB",

    # Europe
    "germany": "DE",
    "france": "FR",
    "italy": "IT",
    "spain": "ES",
    "portugal": "PT",
    "netherlands": "NL",
    "holland": "NL",
    "belgium": "BE",
    "switzerland": "CH",
    "austria": "AT",
    "sweden": "SE",
    "norway": "NO",
    "denmark": "DK",
    "finland": "FI",
    "poland": "PL",
    "czech republic": "CZ",
    "czechia": "CZ",
    "hungary": "HU",
    "greece": "GR",
    "ireland": "IE",
    "iceland": "IS",
    "romania": "RO",
    "bulgaria": "BG",
    "croatia": "HR",
    "serbia": "RS",
    "slovakia": "SK",
    "slovenia": "SI",
    "ukraine": "UA",
    "russia": "RU",
    "turkey": "TR",

    # North America
    "canada": "CA",
    "mexico": "MX",

    # South America
    "brazil": "BR",
    "argentina": "AR",
    "chile": "CL",
    "peru": "PE",
    "colombia": "CO",
    "ecuador": "EC",
    "uruguay": "UY",

    # Africa
    "egypt": "EG",
    "south africa": "ZA",
    "kenya": "KE",
    "morocco": "MA",
    "nigeria": "NG",
    "ethiopia": "ET",
    "tanzania": "TZ",
    "ghana": "GH",

    # Oceania
    "australia": "AU",
    "new zealand": "NZ",
    "fiji": "FJ",
}

# Preferred main airport for country-level searches
COUNTRY_MAIN_AIRPORT = {
    # South Asia
    "BD": "DAC",   # Bangladesh - Dhaka
    "IN": "DEL",   # India - Delhi
    "PK": "ISB",   # Pakistan - Islamabad
    "NP": "KTM",   # Nepal - Kathmandu
    "BT": "PBH",   # Bhutan - Paro
    "LK": "CMB",   # Sri Lanka - Colombo

    # East Asia
    "JP": "NRT",   # Japan - Tokyo Narita
    "CN": "PEK",   # China - Beijing
    "KR": "ICN",   # South Korea - Seoul Incheon
    "KP": "FNJ",   # North Korea - Pyongyang
    "TW": "TPE",   # Taiwan - Taipei
    "HK": "HKG",   # Hong Kong
    "MO": "MFM",   # Macau
    "MN": "UBN",   # Mongolia - Ulaanbaatar

    # Southeast Asia
    "SG": "SIN",   # Singapore
    "MY": "KUL",   # Malaysia
    "TH": "BKK",   # Thailand
    "ID": "CGK",   # Indonesia
    "VN": "SGN",   # Vietnam (Ho Chi Minh City)
    "PH": "MNL",   # Philippines
    "KH": "PNH",   # Cambodia
    "LA": "VTE",   # Laos
    "MM": "RGN",   # Myanmar

    # Middle East
    "AE": "DXB",   # UAE - Dubai
    "QA": "DOH",   # Qatar
    "SA": "JED",   # Saudi Arabia
    "OM": "MCT",   # Oman
    "KW": "KWI",   # Kuwait
    "BH": "BAH",   # Bahrain
    "IL": "TLV",   # Israel
    "JO": "AMM",   # Jordan
    "IR": "IKA",   # Iran
    "IQ": "BGW",   # Iraq
    "LB": "BEY",   # Lebanon

    # Europe
    "GB": "LHR",   # United Kingdom
    "FR": "CDG",   # France
    "DE": "FRA",   # Germany
    "IT": "FCO",   # Italy
    "ES": "MAD",   # Spain
    "PT": "LIS",   # Portugal
    "NL": "AMS",   # Netherlands
    "BE": "BRU",   # Belgium
    "CH": "ZRH",   # Switzerland
    "AT": "VIE",   # Austria
    "SE": "ARN",   # Sweden
    "NO": "OSL",   # Norway
    "DK": "CPH",   # Denmark
    "FI": "HEL",   # Finland
    "PL": "WAW",   # Poland
    "CZ": "PRG",   # Czech Republic
    "HU": "BUD",   # Hungary
    "GR": "ATH",   # Greece
    "IE": "DUB",   # Ireland
    "IS": "KEF",   # Iceland
    "RO": "OTP",   # Romania
    "BG": "SOF",   # Bulgaria
    "HR": "ZAG",   # Croatia
    "RS": "BEG",   # Serbia
    "SK": "BTS",   # Slovakia
    "SI": "LJU",   # Slovenia
    "UA": "KBP",   # Ukraine
    "RU": "SVO",   # Russia
    "TR": "IST",   # Turkey

    # North America
    "US": "JFK",   # United States
    "CA": "YYZ",   # Canada
    "MX": "MEX",   # Mexico

    # South America
    "BR": "GRU",   # Brazil
    "AR": "EZE",   # Argentina
    "CL": "SCL",   # Chile
    "PE": "LIM",   # Peru
    "CO": "BOG",   # Colombia
    "EC": "UIO",   # Ecuador
    "UY": "MVD",   # Uruguay

    # Africa
    "EG": "CAI",   # Egypt
    "ZA": "JNB",   # South Africa
    "KE": "NBO",   # Kenya
    "MA": "CMN",   # Morocco
    "NG": "LOS",   # Nigeria
    "ET": "ADD",   # Ethiopia
    "TZ": "DAR",   # Tanzania
    "GH": "ACC",   # Ghana

    # Oceania
    "AU": "SYD",   # Australia
    "NZ": "AKL",   # New Zealand
    "FJ": "NAN",   # Fiji
}

CITY_MAIN_AIRPORT = {
    "dhaka": "DAC",
    "delhi": "DEL",
    "new delhi": "DEL",
    "mumbai": "BOM",
    "kolkata": "CCU",
    "chennai": "MAA",
    "bangalore": "BLR",
    "bengaluru": "BLR",
    "tokyo": "NRT",
    "osaka": "KIX",
    "kyoto": "KIX",
    "new york": "JFK",
    "london": "LHR",
    "dubai": "DXB",
    "singapore": "SIN",
    "kuala lumpur": "KUL",
    "bangkok": "BKK",
    "doha": "DOH",
    "istanbul": "IST",
    "toronto": "YYZ",
    "sydney": "SYD",
    "paris": "CDG",
    "rome": "FCO",
    "madrid": "MAD",
    "frankfurt": "FRA",
}

STOP_WORDS = [
    "flight",
    "flights",
    "ticket",
    "tickets",
    "trip",
    "travel",
    "including",
    "plan",
    "complete",
    "day",
    "days",
    "including",
    "hotel",
    "hotels",
    "sightseeing",
    "under",
    "budget",
    "info",
    "information",
]