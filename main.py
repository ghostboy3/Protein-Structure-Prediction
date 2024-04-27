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


if __name__ == "__main__":
    response = requests.get('https://files.rcsb.org/download/1AK4.pdb')
    pdb_string = response.content.decode('utf-8')
    render_mol(pdb_string)