# ChemQuery: Learn Molecules Easily

[**ChemQuery**](https://huggingface.co/spaces/Rezuwan/ChemQuery) is a free, student-focused chemistry assistant that lets you explore molecular structures by simply entering a chemical name.

Powered by [PubChem](https://pubchem.ncbi.nlm.nih.gov/) and [PubChemPy](https://github.com/mcs07/pubchempy), this app gives you:
- IUPAC name
- Synonyms
- Molecular formula and weights
- Atom and bond structure
- A downloadable `.txt` summary

Hosted live on [Hugging Face Spaces](https://huggingface.co/spaces/Rezuwan/ChemQuery) using Gradio.

---

## Live Demo

 [Try ChemQuery on Hugging Face Spaces](https://huggingface.co/spaces/Rezuwan/ChemQuery)

---

## Screenshot

![ChemQuery Screenshot](screenshot.png)

---

## Features

- Search chemical compounds by name
- View atomic and bonding structure
- Download full chemical info as a `.txt` file
- Perfect for students, educators, and hobbyists

---

## How It Works

1. You enter a compound name (e.g. "methane").
2. The app fetches data using `pubchempy`.
3. Output is displayed and optionally downloadable.

---

## Run Locally:

1. Clone the repository

```
git clone https://github.com/RezuwanHassan262/ChemQuery
```

2. Go to the project directory

```
cd ChemQuery
```

3. Initialize and activate Virtual Environment

```
virtualenv --no-site-packages  venv
source venv/bin/activate
```

4. Install dependencies

```
pip install -r requirements.txt
```
