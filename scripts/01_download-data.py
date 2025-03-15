"""
This script is used to download data from Synapse using the provided Synapse token.
The data is downloaded to the specified path.
"""
#%% Authentification and import libraries

import os
import synapseclient
import synapseutils
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')  # This reads the environment variables inside .env
SYNAPSE_TOKEN = os.getenv('SYNAPSE_TOKEN')
syn = synapseclient.Synapse()
syn = syn.login(authToken=SYNAPSE_TOKEN)

#%% Download data

files = synapseutils.syncFromSynapse(
    syn, 'syn51549340', path='/Volumes/T7/BrainLat')

# %%
