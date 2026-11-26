from pyscript import document

def check_element(event):

    symbol = document.getElementById("symbol").value

    if symbol == "H":
        result = "Hydrogen"

    elif symbol == "O":
        result = "Oxygen"

    elif symbol == "He":
        result = "Helium"

    else:
        result = "Element Not Found"

    document.getElementById("answer").innerText = result