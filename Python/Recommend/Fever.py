"""Fever"""
def fever(cell):
    """Fever"""
    n_fever = 36 <= cell < 38
    m_fever = 38 <= cell < 39
    h_fever = 39 <= cell < 40
    vh_fever = cell >= 40
    termo = {n_fever : "No Fever", m_fever : "Mild Fever",
             h_fever : "High Fever", vh_fever : "Very High Fever"}
    print(termo[True in termo])
fever(float(input()))
