NODES = [
    {"id": "Akam", "type": "domain"},
    {"id": "Thinai", "type": "concept"},

    {"id": "Kurinji"},
    {"id": "Mullai"},
    {"id": "Marutham"},
    {"id": "Neithal"},
    {"id": "Paalai"},

    {"id": "Mountain"},
    {"id": "Union"},
    {"id": "Night"},

    {"id": "Forest"},
    {"id": "Waiting"},
    {"id": "Evening"},

    {"id": "Farmland"},
    {"id": "Quarrel"},
    {"id": "Day"},

    {"id": "Sea"},
    {"id": "Separation"},

    {"id": "Desert"},
    {"id": "Hardship"},
]

LINKS = [

    # CORE
    {"source": "Akam", "target": "Thinai", "relation": "hasTheme"},

    {"source": "Thinai", "target": "Kurinji", "relation": "includes"},
    {"source": "Thinai", "target": "Mullai", "relation": "includes"},
    {"source": "Thinai", "target": "Marutham", "relation": "includes"},
    {"source": "Thinai", "target": "Neithal", "relation": "includes"},
    {"source": "Thinai", "target": "Paalai", "relation": "includes"},


    # KURINJI
    {"source": "Kurinji", "target": "Mountain", "relation": "associatedWith"},
    {"source": "Kurinji", "target": "Union", "relation": "emotion"},
    {"source": "Kurinji", "target": "Night", "relation": "time"},


    # MULLAI
    {"source": "Mullai", "target": "Forest", "relation": "associatedWith"},
    {"source": "Mullai", "target": "Waiting", "relation": "emotion"},
    {"source": "Mullai", "target": "Evening", "relation": "time"},


    # MARUTHAM
    {"source": "Marutham", "target": "Farmland", "relation": "associatedWith"},
    {"source": "Marutham", "target": "Quarrel", "relation": "emotion"},
    {"source": "Marutham", "target": "Day", "relation": "time"},


    # NEITHAL
    {"source": "Neithal", "target": "Sea", "relation": "associatedWith"},
    {"source": "Neithal", "target": "Separation", "relation": "emotion"},


    # PAALAI
    {"source": "Paalai", "target": "Desert", "relation": "associatedWith"},
    {"source": "Paalai", "target": "Hardship", "relation": "emotion"},
]
