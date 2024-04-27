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
    print(response.text)

    render_mol(response.text)

def update(sequence):
    try:
        display_protien(sequence)
    except Exception:
        print("Error with sequence")
sequence="MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"
petaseSeq="MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"
antifreezeSeq="QCTGGADCTSCTGACTGCGNCPNAVTCTNSQHCVKANTCTGSTDCNTAQTCTNSKDCFEANTCTDSTNCYKATACTNSSGCPGH"
if __name__ == "__main__":   

    # display_protien(sequence)
    # Create a text box for user input
    # user_input = st.sidebar.text_input("Enter Protein Sequence:", key="user_message")
    # update(user_input)
    
    # Initialize session state variables
    # if "user_input" not in st.session_state:
    #     st.session_state.user_input = ""
    with st.form(key='my_form'):
        user_input = st.text_input("Enter Protein Sequence:")
        submit_button = st.form_submit_button("Submit")
    if submit_button:
        update(user_input)
    petase = st.sidebar.button("PETase (Plastic Degradation Protein)")
    antifreeze = st.sidebar.button("1EZG (Antifreeze Protein)")
    if petase:
        # print("HIIIII")
        update(petaseSeq)
        # st.session_state.user_input=antifreezeSeq
    if antifreeze:
        update(antifreezeSeq)
        
    # st.write(f"Input value: {st.session_state.user_input}")