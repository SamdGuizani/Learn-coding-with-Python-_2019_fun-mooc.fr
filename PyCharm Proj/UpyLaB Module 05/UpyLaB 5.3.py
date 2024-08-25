def duree(debut, fin):
    (h_deb, m_deb) = debut
    (h_fin, m_fin) = fin
    h_duree = h_fin - h_deb
    m_duree = m_fin - m_deb
    if h_duree < 0 and m_duree < 0:
        h_duree = h_duree + 23
        m_duree = m_duree + 60
    elif h_duree < 0 and m_duree >= 0:
        h_duree = h_duree + 24
    elif h_duree >= 0 and m_duree < 0:
        h_duree = h_duree - 1
        m_duree = m_duree + 60
    res = (h_duree, m_duree)
    return res


print(duree ((14, 39), (18, 45)))
print(duree ((6, 0), (5, 15)))