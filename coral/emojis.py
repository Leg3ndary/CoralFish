import enum

class FishE(enum.Enum):
    """
    Emojis
    """
    BREAM = 737975203023290418
    GUDEGON = 728531524470833173
    CARP = 728529853363650610
    LOACH = 737983153699946538
    BASS = 728529467856912414
    PIRANHA = 738001191841169460
    KOI = 738013119628181596
    RAINBOW = 738013772500959242
    SHARK = 960182957820219462

    def __str__(self):
        """
        String format for return
        """
        emoji_dict = {
            "737975203023290418": "Bream",
            "728531524470833173": "Gudgeon",
            "728529853363650610": "Carp",
            "737983153699946538": "Loach",
            "728529467856912414": "Bass",
            "738001191841169460": "Piranha",
            "738013119628181596": "Koi",
            "738013772500959242": "Rainbow",
            "960182957820219462": "Shark",
        }
        emoji = f"<:{emoji_dict.get(str(self.value))}:{self.value}>"
        return emoji