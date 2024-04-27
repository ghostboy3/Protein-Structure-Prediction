import py3Dmol
import streamlit as st
from stmol import showmol
import requests


st.title("ESMfold protein structure prediction")

def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('#b0eeff')
    pdbview.zoomTo()
    pdbview.zoom(2, 800)
    # pdbview.spin(True)
    showmol(pdbview, height = 500,width=800)

def display_protien(sequence):
    # response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', data=sequence)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence, verify=False)
    # print(response.text)

    render_mol(response.text)

sequence="MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"
if __name__ == "__main__": 
    # display_protien(sequence)
    # Create a text box for user input
    user_input = st.sidebar.text_input("Enter Protein Sequence:", "")
    try:
        display_protien(user_input)
    except Exception:
        print("Error with sequence")
    # Display the user input