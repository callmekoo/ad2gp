"""
Hi there, fellow programmer.
Let me guess what you're thinking looking on this peace of code: what the *heck* is this?
Let me try to explain. I pretty much understand that making dictionary out of every midi note from
GP and AD it's the best idea, but in that case, you'll be able to understand what is going on here.
I mean, if I'd made a list with mapping like this:

mapping = [
    36:
]

or if i'd just used some ranges.

This is isn't really informative, isn't it? o, that's why I have this overkill thing here.
I wrote it in case it you'd like to rid of it. Please do not!
But if you have a better idea of how to map it better, feel free to PR me!
I mean, feel free to PR anyway and have a nice day!
No passive aggression btw, I'm just Russian.
"""


class DotMap(dict):
    def __getattr__(*args):
        val = dict.get(*args)
        if type(val) is dict:
            return DotMap(val)

        return val


class Mapper(dict):
    def __getattr__(*args):
        try:
            return dict.get(*args)
        except KeyError:
            return args


# Guitar Pro midi mapping
# Please somebody tell my this mapping is so messy
__gp = {
    # Hats
    'ride': {
        'choke': 29,
        'middle': 51,
        'bell': 53,
        'edge': 59
    },
    'cymbal': {
        'reverse': 30,
    },
    'hi_hat': {
        'closed': 42,
        'pedal': 44,
        'open': 46,
    },
    'crash': {
        'high': 49,
        'medium': 57
    },
    'china': {
        'hit': 52
    },

    # Misc and percussion
    'metronome': {
        'hit': 33,
        'bell': 34
    },
    'hand': {
        'clap': 39,
    },
    'tambourine': {
        'hit': 54
    },
    'splash': {
        'hit': 55
    },
    'cowbell': {
        'medium': 56
    },
    'vibraslap': {
      'hit': 58
    },
    'conga': {
        'high_mute': 62,
        'high': 63,
        'low': 64,
    },
    'cabasa': 69,
    'left_maraca': 70,
    'whistle': {
        'high': 71,
        'low': 72
    },
    'guiro': {
        'hit': 73,
        'scarp_return': 74
    },
    'claves': 75,
    'woodblock': {
        'high': 77,
        'low': 78
    },
    'cuica': {
        'mute': 78,
        'open': 79
    },

    # Base
    'kick': {
        'hit': 35,
        'hit_low': 36
    },
    'snare': {
        'side_stick': 37,
        'hit': 38,
        'electric_hit': 40,
        'rimshot': 91
    },
    'tom': {
        'floor': {
            'low': 41,
            'high': 50
        },
        'very_low': 43,
        'low': 45,
        'mid': 47,
        'high': 48
    },
}

# Addictive Drums 2 midi mapping
__ad2 = {
    # Hats
    'ride': {
        'tip': 45,

    },
    'ride1': {
        'tip': 60,
        'bell': 61,
        'shaft': 62,
        'choke': 63
    },
    'ride2': {
        'tip': 84,
        'bell': 85,
        'shaft': 86,
        'choke': 87
    },
    'cymbal': {
        'hit': 46
    },
    'cymbal1': {
        'hit': 77,
        'choke': 78
    },
    'cymbal2': {
        'hit': 79,
        'choke': 80
    },
    'cymbal3': {
        'hit': 81,
        'choke': 82
    },
    'cymbal4': {
        'hit': 89,
        'choke': 90
    },
    'cymbal5': {
        'hit': 91,
        'choke': 92
    },
    'cymbal6': {
        'hit': 93,
        'choke': 94
    },
    'hi_hat': {
        'foot_close': 48,
        'closed_tip': 49,
        'closed_shaft': 50,
        'closed2_tip': 51,
        'closed2_shaft': 52,
        'closed_bell': 53,
        'open_a': 54,
        'open_b': 55,
        'open_c': 56,
        'open_d': 57,
        'open_bell': 58,
        'foot_splash': 59
    },
    'flexi': {
        'hit_b': 73,
        'hit_c': 74,
        'hit_d': 76
    },
    'flexi2': {
        'hit_a': 96,
        'hit_b': 97,
        'hit_c': 98,
        'hit_d': 99
    },
    'flexi3': {
        'hit_a': 100,
        'hit_b': 101,
        'hit_c': 102,
        'hit_d': 103
    },

    # Base
    'kick': 36,
    'snare': {
        'rimshot': 37,
        'open_hit': 38,
        'rimshot_dbi': 39,
        'open_hit_dbi': 40,
        'shallow_rimshot': 41,
        'side_stick': 42,
        'shallow_hit': 43,
    },
    'sicks': 75,
    'tom': {
        'very_low': {
            'hit': 65,
            'rimshot': 66
        },
        'low': {
            'hit': 67,
            'rimshot': 68
        },
        'mid': {
            'hit': 69,
            'rimshot': 70
        },
        'high': {
            'hit': 71,
            'rimshot': 72
        }
    },

}

gp = DotMap(__gp)
ad2 = DotMap(__ad2)

__mapping = {
    # Kicks
    ad2.kick: gp.kick.hit,

    # Snares
    ad2.snare.rimshot: gp.snare.rimshot,
    ad2.snare.open_hit: gp.snare.hit,
    ad2.snare.rimshot_dbi: gp.snare.rimshot,
    ad2.snare.open_hit_dbi: gp.snare.hit,
    ad2.snare.shallow_rimshot: gp.snare.rimshot,
    ad2.snare.side_stick: gp.snare.side_stick,
    ad2.snare.shallow_hit: gp.snare.side_stick,

    # Hi-hats
    ad2.hi_hat.foot_close: gp.hi_hat.pedal,
    ad2.hi_hat.closed_tip: gp.hi_hat.closed,
    ad2.hi_hat.closed_shaft: gp.hi_hat.closed,
    ad2.hi_hat.closed2_tip: gp.hi_hat.closed,
    ad2.hi_hat.closed2_shaft: gp.hi_hat.closed,
    ad2.hi_hat.closed_bell: gp.hi_hat.closed,
    ad2.hi_hat.open_a: gp.hi_hat.open,
    ad2.hi_hat.open_b: gp.hi_hat.open,
    ad2.hi_hat.open_c: gp.hi_hat.open,
    ad2.hi_hat.open_d: gp.hi_hat.open,
    ad2.hi_hat.open_bell: gp.hi_hat.open,
    ad2.hi_hat.foot_splash: gp.hi_hat.open,

    # Toms
    ad2.tom.very_low.hit: gp.tom.very_low,
    ad2.tom.very_low.rimshot: gp.tom.very_low,
    ad2.tom.low.hit: gp.tom.low,
    ad2.tom.low.rimshot: gp.tom.low,
    ad2.tom.mid.hit: gp.tom.mid,
    ad2.tom.mid.rimshot: gp.tom.mid,
    ad2.tom.high.hit: gp.tom.high,
    ad2.tom.high.rimshot: gp.tom.high,

    # Rides
    ad2.ride.tip: gp.ride.middle,
    ad2.ride1.tip: gp.ride.middle,
    ad2.ride1.bell: gp.ride.bell,
    ad2.ride1.shaft: gp.ride.edge,
    ad2.ride1.choke: gp.ride.choke,
    ad2.ride2.tip: gp.ride.middle,
    ad2.ride2.bell: gp.ride.bell,
    ad2.ride2.shaft: gp.ride.edge,
    ad2.ride2.choke: gp.ride.choke,

    # Cymbals
    # I didn't find any in GP mapping, so
    ad2.cymbal.hit: gp.crash.high,
    ad2.cymbal1.hit: gp.crash.high,
    ad2.cymbal1.choke: gp.crash.high,
    ad2.cymbal2.hit: gp.crash.medium,
    ad2.cymbal2.choke: gp.crash.medium,
    ad2.cymbal3.hit: gp.ride.middle,
    ad2.cymbal3.choke: gp.ride.choke,
    ad2.cymbal4.hit: gp.ride.middle,
    ad2.cymbal4.choke: gp.ride.choke,
    ad2.cymbal5.hit: gp.ride.middle,
    ad2.cymbal5.choke: gp.ride.choke,
    ad2.cymbal6.hit: gp.ride.middle,
    ad2.cymbal6.choke: gp.ride.choke,

    # Flexi
    # No idea here neither
    ad2.flexi.hit_b: gp.woodblock.low,
    ad2.flexi.hit_c: gp.woodblock.low,
    ad2.flexi.hit_d: gp.woodblock.low,
    ad2.flexi2.hit_a: gp.woodblock.low,
    ad2.flexi2.hit_b: gp.woodblock.low,
    ad2.flexi2.hit_c: gp.woodblock.low,
    ad2.flexi2.hit_d: gp.woodblock.low,
    ad2.flexi3.hit_b: gp.woodblock.low,
    ad2.flexi3.hit_a: gp.woodblock.low,
    ad2.flexi3.hit_c: gp.woodblock.low,
    ad2.flexi3.hit_d: gp.woodblock.low,

    # Sticks
    ad2.sticks: gp.snare.side_stick
}

mapping = Mapper(__mapping)
