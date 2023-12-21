#    ______                      __
#   / ____/______  ______  _____/ /_________  ____ _____ ____
#  / /   / ___/ / / / __ \\/ ___/ __/ ___/ _ / __ `/ __ `__  /
# / /___/ /  / /_/ / /_/ (__  ) /_/ /  /  __/ /_/ / / / / / /
# \____/_/   \__, /\____/____/\__/_/   \___/\__,_/_/ /_/ /_/
#           /____/      by BCSB 2023 @ ALS @ Berkeley Labs.")
#                                          Cryostream 1000.")        
#
##########################
### Python 2.7 Edition ###
##########################

# Python 2.7 Edition.
# Remember to run with Python2.7 otherwise it will not work.
# Porting to Python3 should be straightforward.
# We are running this version for business reasons, but we could for sure use Python3.

#Authors:
#John Taylor, Berkeley National Laboratory (Email: jrtaylor_at_lbl.gov)
#Gabriel Gazolla, Berkeley National Laboratory (Email: gabrielgazolla_at_lbl.gov)

import sys
from cryostream1000 import Cryostream1000

############
### Main ###
############

#Please, Update Your IP!

BL501_Cryostream1000 = Cryostream1000(ip="130.221.79.112")

BL501_Cryostream1000.terminal_displayMenu()
