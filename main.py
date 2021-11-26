#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import codecs
from scipy import stats
import nltk
from nltk.probability import FreqDist
# #############
# # Partie 1 ##
# #############


def registry(file_name):  # Enregistrement des mots vers des listes
    tmp = codecs.open(f"{file_name}", "r", "utf-8")
    file = tmp.read().lower()
    stack = []
    cursor = 0
    i = 0
    while(i < len(file)):
        if(not file[i].isalpha()):
            stack[len(stack):] = [file[cursor:i]]
            a = i
            while(a < len(file) and not file[a].isalpha()):
                a += 1
            i = a
            cursor = i
        else:
            i += 1
    tmp.close()
    return stack


def comparaison(fa, fb):  # Recherche de similitudes dans les deux fichiers
    tableau = {}
    for i in range(len(fa)):
        compteur = 0
        for r in range(len(fb)):
            if(fa[i] == fb[r]):
                compteur += 1
            else:
                pass
        if(compteur > 0):
            to_add = {fa[i]: compteur}
            tableau.update(to_add)
        else:
            pass
    return tableau


def part1_affichage(dico):
    print("partie 1 :\n\nMots clés présents dans le zen :")
    nbr_kw = 0
    a = 0
    for c in dico.values():
        nbr_kw += c
    dico = sorted(dico.items(), key=lambda x: x[1])
    dico.reverse()
    while(a < len(dico)):
        print(f"{dico[a][0]}\t: {dico[a][1]}")
        a += 1
    print(f"Nombre total de mots clés présents dans le Zen : {nbr_kw}\n\n\n")

# #############
# # Partie 2 ##
# #############


def part2_affichage(jim_rep, jim_total):
    print("partie 2:\nNombre d'apparitions de chaque mot plus d'une fois dans le texte:\n\tmot\t: nb : \t% app\n")
    total_length = len(jim_total)
    jim_sorted = sorted(jim_rep.items(), key=lambda t: t[1])  # Jim deviens une liste
    jim_sorted.reverse()
    for x, y in jim_sorted:
        pourcentage_app = int(y)*100/int(total_length)
        if(len(x) >= 8):
            print(f"{x}\t: {y} :\t {round(pourcentage_app,2)} %")
        else:
            print(f"{x}\t\t: {y} :\t {round(pourcentage_app,2)} %")
    print(f"\nNombre total de mots présents dans le texte : {total_length}")
    mots_serie = 0
    for x, y in jim_sorted:
        mots_serie += y
    print(f"total mots de la série {mots_serie} ; moyenne {round(mots_serie/len(jim_sorted),2)} ; max {jim_sorted[0][1]} ; min {jim_sorted[len(jim_sorted)-1][1]}")
    print("Options statistiques descriptives")
    l_value = []
    for foo, v in jim_sorted:
        l_value.append(v)
    mode = stats.mode(l_value)
    ecarttype = np.std(l_value)
    mediane = np.median(l_value)
    q1 = np.percentile(l_value, 25)
    q3 = np.percentile(l_value, 75)
    d9 = np.percentile(l_value, 90)
    print(f"Ecart-type {round(ecarttype,2)} ; Mode {mode[0][0]} ; Q1 {q1} ; Médiane {mediane} ; Q3 {q3} ; D9 {d9} ")
    print("\n\n")
    return jim_sorted


def p2_stats_globales(fichier):
    tableau = {}
    for i in range(len(fichier)):
        compteur = 0
        comp_value = fichier[i]
        for a in fichier:
            if(comp_value == a):
                compteur += 1
            else:
                pass
        if(compteur > 1):
            add_tableau = {fichier[i]: compteur}
            tableau.update(add_tableau)
        else:
            pass
    return tableau

# #############
# # Partie 3 ##
# #############


def graphique(tab):
    l_value = []
    l_key = []
    tab.sort(key=lambda x: x[0])
    for a, b in tab:
        l_key.append(a)
        l_value.append(b)
    plt.ylabel("nombre d'occurences")
    plt.bar(l_key, l_value, color="orange")
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.title("Mots apparaissant plus d'une fois dans le texte")
    plt.show()

# #############
# # Partie 4 ##
# #############


def get_parite(lst):
    if(len(lst) % 2 == 0):
        return "pair"
    else:
        return "impair"


def part_4(tab):
    tab = sorted(tab, key=lambda tup: tup[1])
    stop = False
    while(stop == False):
        b_min = input("\nNombre minimal de lettres (q pour quitter) : ")
        b_max = "foo"
        while(not b_min.isnumeric() or int(b_min) <= 1):
            if(b_min == "q" or b_min == "Q"):
                stop = True
                break
            elif(not b_min.isnumeric()):
                print("OOPS, min_number needs to be a number ! \n")
            elif(int(b_min) <= 1):
                print("OOPS, min_number needs to be greather than 1 !\n")
            else:
                pass
            b_min = input("\nNombre minimal de lettres (q pour quitter) : ")
        while(stop == False and not b_max.isnumeric() and b_max > b_min):
            if(b_max == "q" or b_max == "Q"):
                stop = True
                break
            elif(b_min > b_max):
                print("OOPS, max number needs to be greater than min number !\n")
            b_max = input("\nNombre maximal de lettres : ")
        if(stop == False):
            storage = []
            for x, y in tab:
                if(len(x) >= int(b_min) and len(x) < int(b_max)):
                    storage.append(x)
                else:
                    pass
            result = f"\t{get_parite(storage)}\tmin {b_min}\tmax {b_max}"
            f = codecs.open("mots.txt", "a", "utf-8")
            print(f"\nnombre maximal de lettres : {b_max}\n{result}")
            f.write(f"{result}\n")
            i = 0
            while(i < len(storage)):  # Affichage et écriture dans le fichier
                if(get_parite(storage) == "pair"):
                    print(f"{storage[i]} {storage[i+1]}")
                    f.write(f"{storage[i]} {storage[i+1]}\n")
                    i += 1
                else:
                    f.write(f"{storage[i]}\n")
                    print(storage[i])
                i += 1
            f.close()
        else:
            print("\nAu revoir !")

# ########################
# # Appels de fonctions ##
# ########################
kw_file = registry("kw_file.txt")
zen_file = registry("this_file.txt")

dico = comparaison(kw_file, zen_file)
part1_affichage(dico)

jim = registry("chanson_jim.txt")
tableau_jim = p2_stats_globales(jim)
jim_sorted = part2_affichage(tableau_jim, jim)

graphique(jim_sorted)

part_4(jim_sorted)
