import gradio as gr
import pubchempy as pcp

def get_chemical_info(chemical_name):
    try:
        compound = pcp.get_compounds(chemical_name, 'name')[0]

        output = []
        output.append(f"IUPAC Name: {compound.iupac_name}")
        output.append(f"Common Name: {compound.synonyms[0]}")
        output.append(f"Synonyms: {', '.join(compound.synonyms[:4])}")
        output.append(f"Formula: {compound.molecular_formula}")
        output.append(f"Molecular Weight: {compound.molecular_weight}")
        output.append(f"Exact Molecular Weight: {compound.exact_mass}")
        output.append(f"Isotope Atom Count: {compound.isotope_atom_count}")
        output.append(f"Charge: {compound.charge}")

        # Atoms
        output.append("\nAtoms:")
        atom_dict = {i + 1: atom.element for i, atom in enumerate(compound.atoms)}
        for idx, element in atom_dict.items():
            output.append(f"  Atom {idx}: Element = {element}")

        # Bonds
        output.append("\nBonds:")
        for bond in compound.bonds:
            atom1 = atom_dict.get(bond.aid1, f"Atom {bond.aid1}")
            atom2 = atom_dict.get(bond.aid2, f"Atom {bond.aid2}")
            output.append(f"  Bond between {atom1} and {atom2}, Order: {bond.order}")

        final_text = "\n".join(output)

        # Save to a file
        file_path = f"/tmp/{chemical_name.replace(' ', '_')}_info.txt"
        with open(file_path, "w") as f:
            f.write(final_text)

        return final_text, file_path

    except IndexError:
        return f"No information found for '{chemical_name}'. Please try a more precise name.", None


# Gradio UI
with gr.Blocks(title="ChemQuery: Learn Molecules Easily") as demo:
    gr.Markdown("## ChemQuery: Learn Molecules Easily")
    gr.Markdown(
        """Enter a chemical name to get formula, synonyms, atomic structure, and more.Powered by PubChem & PubChemPy. Designed for student use in chemistry learning.
        Please leave a heart (❤️) and spread this among your friends."""
    )

    with gr.Row():
        chemical_input = gr.Textbox(label="Enter Chemical Name", lines=1, scale=5)
        submit_btn = gr.Button("Submit", scale=1, elem_id="submit-btn")

    gr.Markdown(
        """
        <style>
        #submit-btn button {
            background-color: #48CAE4 !important;
            height: 48px !important;
            font-weight: bold;
        }
        </style>
        """
    )

    output_text = gr.Textbox(label="Compound Information", lines=25)
    download_file = gr.File(label="Download as TXT")

    submit_btn.click(get_chemical_info, inputs=chemical_input, outputs=[output_text, download_file])

demo.launch()