class Aeolian:
    """
    Class for Aeolian mode
    """
    name = "Aeolian"
    majorPos = 6
    minorPos = 1

    # List of possible notes for each iteration

    logic = [
	# 00 one1
	["thr1", "fiv1", "six1", "sev1", "one2", "two2", "thr2", "for2", "fiv2"],
	# 01 two1
	["fiv1", "sev1"],
	# 02 thr1
	["one1", "for1", "fiv1", "six1", "sev1", "one2", "fiv2"],
	# 03 for1
	["fiv1", "six1", "sev1", "one2", "thr2"],
	# 04 fiv1
	["thr1", "six1", "sev1", "one2", "two2", "thr2", "for2", "fiv2"],
	# 05 six1
	["one1", "fiv1", "sev1", "one2", "thr2", "fiv2"],
	# 06 sev1
	["fiv1", "six1", "one2", "two2", "thr2"],
	# 07 one2
	["one1", "thr1", "for1", "fiv1", "six1", "sev1", "two2", "thr2", "for2", "fiv2", "six2", "sev2", "one3", "two3", "thr3", "for3", "fiv3"],
	# 08 two2
	["fiv1", "sev1", "one2", "thr2", "fiv2", "sev2", "two3"],
	# 09 thr2
	["fiv1", "six1", "sev1", "one2", "fiv2", "six2", "sev2", "one3"],
	# 10 for2
	["thr2", "fiv2", "six2", "sev2", "two3", "six1"],
	# 11 fiv2
	["thr1", "fiv1", "six1", "sev1", "one2", "two2", "thr2", "for2", "six2", "sev2", "one3", "two3"],
	# 12 six2
	["for1", "fiv2", "sev2", "one3", "thr3"],
	# 13 sev2
	["fiv2", "six2", "one3", "two3", "thr3"],
	# 14 one3
	["one1", "for1", "fiv1", "six1", "one2", "thr2", "fiv2", "six2", "sev2", "two3", "thr3", "for3", "fiv3", "six3", "one4"],
	# 15 two3
	["two2", "fiv2", "sev2", "one3", "thr3", "fiv3", "sev3"],
	# 16 thr3
	["fiv2", "six2", "sev2", "one3", "two3", "for3", "fiv3", "six3", "sev3", "one4"],
	# 17 for3
	["six2", "thr3", "fiv3", "six3", "sev3"],
	# 18 fiv3
	["thr2", "fiv2", "six2", "sev2", "one3", "two3", "thr3", "for3", "six3", "sev3", "one4"],
	# 19 six3
	["for2", "for3", "fiv3", "sev3", "one4"],
	# 20 sev3
	["sev2", "fiv3", "six3", "one4"],
	# 21 one4
	["six2", "one3", "thr3", "for3", "fiv3", "six3", "sev3"],
	# 22 else
	["one1", "one2", "one3"] ]

    # List of possible chords
    chords = [
            ["one1", "thr1", "fiv1"],
	    ["one1", "thr1", "sev1"],
	    ["one1", "fiv1", "one2"],
	    ["one1", "fiv1", "thr2"],
	    ["one1", "fiv1", "fiv2"],
	    ["one1", "thr2", "sev2"],
	    ["thr1", "one2", "fiv2"],
	    ["thr1", "fiv1", "one2"],
	    ["fiv1", "one2", "thr2"],
            ["one1", "fiv1", "thr2", "sev2"] ]


