# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:32:21 2016

@author: Alexis Eidelman
"""

## correction
# TODO: have a test on upper case for first letter of each word.
#for table in [equipement, revenu, population, population12]:
#    table['LIBCOM'] = table['LIBCOM'].str.replace(' - ', '-')
#    table['LIBGEO'] = table['LIBGEO'].str.replace('CENTRE VILLE', 'Centre Ville')
#
#for table in [equipement, population, population12]:
#    table['LIBGEO'] = table['LIBGEO'].str.replace('CENTRE VILLE', 'Centre Ville')

def fillna_with_other_table(tab1, tab2, var, columns=None):
    ''' replace unfilled values of data by values of the other tab if filled '''
    if columns is None:
        columns = [x for x in tab1.columns if x in tab2.columns]
        columns.remove(var)

    data = tab1.merge(tab2[columns + [var]], on=var, how='left', suffixes=('','_temp'))
    for col in columns:
        to_replace = data[col].isnull() & data[col + '_temp'].notnull()
        data.loc[to_replace, col] = data.loc[to_replace, col + '_temp']
        del data[col + '_temp']
    return data


def compare_var(tab1, tab2, var):
    assert max(tab1[var].value_counts()) == 1
    assert max(tab2[var].value_counts()) == 1
    cond_1_in_2 = tab1[var].isin(tab2.IRIS)
    cond_2_in_1 = tab2[var].isin(tab1.IRIS)
    in_1_not_in_2 = tab1[var][~cond_1_in_2]
    in_2_not_in_1 = tab2[var][~cond_2_in_1]
    print("il y a " + str(len(in_1_not_in_2)) + " " + var + " dans 1 et pas dans 2")
    print("il y a " + str(len(in_2_not_in_1)) + " " + var + " dans 2 et pas dans 1")


def compare_inner(tab1, tab2, var, common_cols=None):
    if common_cols is None:
        commun_col = [x for x in tab1.columns if x in tab2.columns]
        commun_col.remove(var)
    merge_tab = tab1.merge(tab2, on=var, how='inner')
    tab1_commun = merge_tab[[x + '_x' for x in commun_col] + [var]]
    tab1_commun.columns = commun_col+ [var]
    tab2_commun = merge_tab[[x + '_y' for x in commun_col] + [var]]
    tab2_commun.columns = commun_col+ [var]

    return tab1_commun, tab2_commun

# une table de comparaison
def compare_geo(tab1, tab2, var='IRIS', debug=False):
    compare_var(tab1, tab2, var)
    tab1_commun, tab2_commun = compare_inner(tab1, tab2, var)

    commun_col = [x for x in tab1.columns if x in tab2.columns]
    commun_col.remove(var)

    if all((tab1_commun != tab2_commun).sum() == 0):
        print("Pas de problème sur les données communes, on peut faire le merge")
        return

    # parfois on a des différences sur LIBCOM uniquement pour les arrondissements
    if all(tab1_commun['DEP'] == tab2_commun['DEP']):
        commun_col_special = [x for x in commun_col if x not in ['LIBCOM', 'COM']]
        diff_special = tab1_commun[commun_col_special] != tab2_commun[commun_col_special]
        hors_arrondissement = ~tab1_commun['DEP'].isin(['13','69','75'])
        diff = tab1_commun[hors_arrondissement] != tab2_commun[hors_arrondissement]
        if all(diff.sum() == 0) and all(diff_special.sum() == 0):
            print(u"les différences concernent uniquement les villes à arrondissements" +
                  u" pour LIBCOM et COM")
            return

    col_diff = ['IRIS']
    for col in commun_col:
        diff = tab1_commun[col] != tab2_commun[col]
        if diff.sum() == 0:
            print(u"aucune différence sur " + col)
        else:
            count = diff.sum()
            print(u"[WARNING] Il y a " + str(count) + u" problèmes pour " + col)
            col_diff += [col]

    if debug:
        if 'DEP' not in col_diff:
            col_diff += ['DEP']

        diff = tab1_commun != tab2_commun
        tab1_pb = tab1_commun.loc[diff.any(axis=1), col_diff]
        tab2_pb = tab2_commun.loc[diff.any(axis=1), col_diff]
        pb = tab1_pb.merge(tab2_pb, on=var, suffixes=('_1', '_2'))
        pb.sort_index(axis=1, inplace=True)

        hors_arrondissement = ~pb['DEP_1'].isin(['13','69','75'])
        pb_hors_arrondissement = pb[hors_arrondissement]
        import pdb; pdb.set_trace()

