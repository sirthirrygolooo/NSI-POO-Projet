@echo off

REM nomme la fenêtre 
title NSI POO project launcher 
cls

REM definition de la fonction principale  

:MAIN
cls
::: **********************************************
::: ************ Faites votre choix  *************
::: [S] - Lancer le programme
::: [V] - Voir ma version active de python
::: [I] - Installer les modules nécessaires
::: [E] - Quitter
::: **********************************************

REM ligne qui permet d'afficher les lignes du fichier qui commencent par :::
for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A


REM choix de l'utilisateur avec redirection vers la fonction qui correspond a l'action voulue

choice /c SVIE /m ">>>"
IF ERRORLEVEL 4 GOTO END
IF ERRORLEVEL 3 GOTO INS
IF ERRORLEVEL 2 GOTO VER
IF ERRORLEVEL 1 GOTO START 

REM fonction qui lance juste le programme
:START
python main.py
exit

REM montre à l'utilisateur sa version de python
:VER
cls
python --version
pause
GOTO MAIN 

REM Installe les bibliothèques requises contenues dans le fichier requirements.txt avec pip
:INS 
pip install -r requirements.txt
pause
GOTO MAIN

REM Fonction qui permet de quitter le programme
:END
CHOICE /c YN /m "Voulez vous vraiment quitter ? "

REM confirmation du choix
IF ERRORLEVEL 2 GOTO MAIN
IF ERRORLEVEL 1 exit
exit