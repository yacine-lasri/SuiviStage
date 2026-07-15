-- *****************************************************************************************
-- *****************************************************************************************
-- *****************************************************************************************
-- *****************************************************************************************
-- EMSI CASA
-- 3IIR
-- T-SQL SQL Server
-- 2025/2026
-- *****************************************************************************************
-- *****************************************************************************************
-- *****************************************************************************************
-- *****************************************************************************************


-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- EXAMEN 2025
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- schéam de la BD
-- On considère une base de données relationnelle nommée GestionRH utilisée pour la gestion 
-- du personnel d’une entreprise. Le schéma logique de cette base de données et le dictionnaire 
-- de données sont donnés ci-dessous : 

-- EMPLOYE(matricule, Nom, Prenom, Date_naissance, Date_embauche, Salaire) 
-- EVOLUTION(ID_evolution, Matricule, Date_evolution, Ancien_salaire, PCT_augmentation, Motif)
-- ABSENCE(ID_absence, Matricule, Date_debut, Date_fin, Motif)


-- EMPLOYE	La table EMPLOYE enregistre les informations personnelles, professionnelles et 
-- administratives de chaque employé, telles que son matricule, nom, prénom, date de naissance, date d’embauche, salaire annuel, le service auquel il appartient et son grade.
-- 	Matricule		INT				PK			Identifiant unique de l’employé
-- 	Nom				VARCHAR(50)		NOT NULL	Nom de famille de l’employé
-- 	Prenom			VARCHAR(50)		NOT NULL	Prénom de l’employé
-- 	Date_naissance	DATE	NOT 	NULL		Date de naissance
-- 	Date_embauche	DATE	NOT 	NULL		Date d’entrée dans l’entreprise
-- 	Salaire			DECIMAL(10,2)	NOT NULL	Salaire mensuel
				
-- EVOLUTION	La table EVOLUTION permet de suivre les évolutions de carrière des employés. 
-- Elle contient des données sur les changements de salaire, les augmentations, les primes accordées, 
-- les dates de ces évolutions et les motifs associés.
-- 	ID_evolution		INT IDENTITY(1,1)	PK	Identifiant de l’évolution
-- 	Matricule			INT					FK, fait référence à EMPLOYE(Matricule)	Employé concerné
-- 	Date_evolution		DATE				NOT NULL	Date de l’évolution
-- 	Ancien_salaire		DECIMAL(10,2)		NOT NULL	Salaire avant évolution
-- 	PCT_augmentation	DECIMAL(5,2)		Pourcentage d’augmentation
-- 	Motif				VARCHAR(100)		Motif de l’évolution
				
-- ABSENCE	La table ABSENCE enregistre les périodes d’absence des employés avec les dates de 
-- début et de fin ainsi que le motif de chaque absence.
-- 	ID_absence	INT IDENTITY (1,1)	PK	I		dentifiant de l’absence
-- 	Matricule	INT					FK, 		Fait référence à EMPLOYE(Matricule)	Employé concerné
-- 	Date_debut	DATE				NOT NULL	Début de l’absence
-- 	Date_fin	DATE				NOT NULL	Fin de l’absence
-- 	Motif		VARCHAR(100)					Motif de l’absence

-- *****************************************************
-- QUESTION 1 : (5 pts)
-- 1.1.   Créer une fonction fn_NbrAbsence qui calcule le nombre total d'absences (en jours) 
-- d’un employé dont le matricule est passé en argument. Pour ce, vous pouvez utiliser 
-- la fonction DATEDIFF (DAY, DateDebut, DateFin) pour récupérer la différence entre 2 dates 
-- en nombre de jours. (4 pts)

-- *****************************************************
-- 1.2.	 Afficher, pour chaque employé de la table EMPLOYE, son matricule, son nom ainsi que 
-- le nombre total de jours d’absences. (1 pt)

-- *****************************************************	
-- QUESTION 2 : (4 pts)
-- Créer une procédure sp_AjouterAbsence permettant d'enregistrer une nouvelle absence pour un employé donné. 
-- La procédure prend en paramètre le matricule de l’employé, la date de début, la date de fin et 
-- le motif de l’absence.  
-- Gérer l’exception si le matricule fournit ne correspond à aucun employé (Erreur numéro 547), 
-- ou si la date de début est supérieure à la date de fin (date_début>date_fin). 
-- En cas d’erreur, la procédure affiche le numéro et le message d’erreur appropriés.

-- *****************************************************
-- QUESTION 3 : (7 pts)
-- 3.1.  Créer une procédure sp_AugmentationSalaire qui prend en paramètres :
-- 	Le matricule de l’employé
-- 	Le pourcentage d’augmentation (ex. 10%)
-- 	Le motif 
-- La procédure doit mettre à jour le salaire de l’employé, puis enregistrer cette opération dans 
-- la table EVOLUTION (en insérant le matricule, la date d’aujourd’hui (GETDATE()), l’ancien salaire, 
-- le pourcentage d’augmentation et le motif).
-- Gérer l’exception si le matricule fourni n’existe pas. (6 pts)

-- *****************************************************
-- 3.2.  Augmenter de 10% le salaire de l’employé ayant le matricule 1001, en utilisant 
-- la procédure sp_augmentationSalaire. (1pt)

-- *****************************************************	
-- QUESTION 4 : (4pts)
-- Ecrire un trigger trg_DeleteEmp sur la table ABSENCE permettant d’archiver chaque absence 
-- supprimée dans une table d’archive nommée ABSENCE_ARCHIVE, qui contient les mêmes attributs 
-- que la table ABSENCE, plus une colonne DATE_SUPPRESSION de type DATE.
-- La table ABSENCE_ARCHIV est supposée être déjà créée.

-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- EXAMEN RATTRAPAGE JUILLET 2025
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- ENONCE

-- On considère une base de données relationnelle nommée GestionNotesExamens utilisée pour 
-- la gestion des notes des examens des étudiants d’une école d’ingénieurs. Le schéma logique de cette base de données et le dictionnaire de données sont donnés ci-dessous (Fig. 1 et Tab. 1) : 

-- ETUDIANTS(NumEtd, NomEtd, PrenomEtd, CinEtd, ClasseEtd)
-- COURS(NumCours, NomCours, VolHCours)
-- NOTES_EXAMENS(NumCours, NumEtd, NoteExamCours) 

-- ETUDIANTS	La table ETUDIANTS contient tous les étudiants de l’école. Chaque étudiant est 
-- identifié par son numéro unique NumEtd, son nom NomEtd, prénom PrenomEtd, 
-- le numéro unique de sa carte d’identité CinEtd et sa classe ClasseEtd, à laquelle l’étudiant 
-- appartient. Chaque étudiant appartient à une seule classe mais dans une classe, on trouve 
-- plusieurs étudiants.
-- 	NumEtd		INTEGER		PK						Identifiant unique de l’étudiant
-- 	NomEtd		VARCHAR(20)	NOT NULL				Nom de famille de  l’étudiant
-- 	PrenomEtd	VARCHAR(20)	NOT NULL				Prénom de  l’étudiant
-- 	CinEtd		VARCHAR(20)	NOT NULL and UNIQUE		Numéro de la carte d’identité de  l’étudiant
-- 	ClasseEtd	INTEGER	NOT NULL					Numéro de la classe de l’étudiant

-- COURS	La table COURS contient tous les cours dispensés suivis par les étudiants et 
-- dans lesquels chaque étudiant PASSE OBLIGATOIREMENT un examen. Chaque cours est donné 
-- par son numéro unique NumCours, son nom NomCours unique aussi et son volume horaire VolHCours
-- 	NumCours	INTEGER		PK						Identifiant unique du cours
-- 	NomCours	VARCHAR(20)	NOT NULL and UNIQUE		Nom unique du cours
--  VolHCours	INTEGER		NOT NULL				Le volume horaire du cours

-- NOTES_EXAMENS	La table NOTES_EXAMENS contient les notes obtenues dans les examens passés 
-- par les étudiants dans les cours suivis. Chaque ligne de cette table, donne la note NoteExamCours 
-- obtenu par l’étudiant NumEtd dans le cours NumCours. La clé primaire de cette table est 
-- le couple (NumEtd, NumCours) ce qui veut dire qu’un étudiant NumEtd ne passe qu’un examen 
-- dans un même cours NumCours.
-- 	NumCours		INTEGER		NOT NULL							Numéro du cours dans lequel l’examen est passé. 
--																	Fait référence à NumCours dans la table COURS
-- 	NumEtd			INTEGER		NOT NULL							Numéro de l’étudiant ayant passé l’examen 
-- 																	dans le cours NumCours. 
-- 																	Fait référence à NumEtd dans la table ETUDIANTS
-- 	NoteExamCours	DECIMAL(4,2)NOT NULL and  0<=NoteExamCours<=20	La note obtenue à l’examen du cours 
-- 																	NumCours par l’étudiant NumEtd. 
-- 																	Par défaut, ce champs prend 0

-- Et on considère les règles de gestion suivantes : 
-- Règle 1 : tous les cours ont le même coefficient 1
-- Règle 2 : Toute absence dans un examen donne 0 comme note d’examen dans ce cours (valeur par défaut)
-- Règle 3 : la moyenne générale d’un étudiant est la somme de ses notes obtenues dans les examens 
-- passés divisée par le nombre de ces examens
-- Règle 4 : la moyenne d’une classe dans un cours est la somme des notes obtenues, par tous 
-- les étudiants de cette classe, dans l’examen de ce cours, divisée par le nombre d’étudiants 
-- de cette classe.
-- Règle 5 : la moyenne d’un cours est la somme des notes obtenues, par tous les étudiants, 
-- dans l’examen de ce cours, divisée par le nombre d’étudiants ayant passé l’examen de ce cours. 

-- QUESTION 1 : (5 pts)
-- 1.1.   Créer une fonction fn_MoyGenEtd qui calcule et retourne la moyenne d’un étudiant 
-- passé en argument par son numéro NumEtd. (4 points)
	
-- 1.2.	 Ecrire une requête SQL qui affiche, pour chaque étudiant, dans la table ETUDIANTS, 
-- sa moyenne générale en utilisant la fonction fn_MoyGenEtd définie ci-dessus. (1 pt)

-- QUESTION 2 : (5 pts)
-- Créer une fonction fn_MoyenGeneClassCours, qui prend en argument le numéro d’un cours et 
-- le numéro d’une classe, calcule la moyenne générale de cette classe dans ce cours (voir Règle 4).
-- Si le cours n’existe pas, la fonction doit retourner -1 et si la classe n’existe pas, 
-- la fonction retourne -2, Sinon, elle retourne la moyenne générale.

-- QUESTION 3 : (6 pts)
-- 3.1.  Créer une procédure SP_SyntheseNote qui ne prend aucun argument :
-- La procédure doit calculer la moyenne de chaque classe pour chaque cours et les stocke dans 
-- la table TabSynthMoyenClassCours définie par :
-- NumClasse le numéro de la classe, NumCours le numéro du cours, NomCours le nom du cours, 
-- MoyeGenCours la moyenne générale de la classe NumClasse dans le cours NumCours, DateCalcul 
-- la date du calcul qui est la date d’aujourd’hui (GETDATE()). 
-- On suppose la table TabSynthMoyenClassCours déjà créée.


-- QUESTION 4 : (4pts)
-- Ecrire un trigger trg_TrModifNotes qui archive les modifications des notes, dans la table 
-- Notes_Examens, et les stocke dans la table ArchiModifsNotes définies par 
-- les colonnes suivantes :
-- NumModif, de type INT IDENTITY, pour numéroter les lignes dans cette table,
-- NumCours, le numéro du cours concerné par la modification de la note,
-- NumEtd, le numéro de l’étudiant concerné par la modification de la note,
-- OldNote, l’ancienne note avant modification,
-- NewNote, la nouvelle note après modification,
-- DtModif, la date de modification. C’est la date d’aujourd’hui (GETDATE()),
-- NomUser, le nom de l’utilisateur ayant modifié la note (CURRENT_USER()).

-- On suppose cette table déjà créée. 

-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- Examen Final
-- Matière : SQL Server
-- Année Universitaire : 2018 - 2019 Date : 14/06/2019
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- Examen Final
-- Matière : SQL Server
-- Année Universitaire : 2018 - 2019 Date : 14/06/2019
-- Durée : 1h30
-- Documents du cours et tps autorisés
-- Les questions sont suffisamment expliquées, reportez vos remarques sur votre copie
-- Il sera tenu compte de la clarté et de la simplicité des réponses
-- Les réponses sont à donner directement sur les feuilles de l’examen à l’emplacement
-- réservé pour ça.

-- On considère une base de données utilisée par une compagnie aérienne pour enregistrer 
-- des informations sur des villes (nom), des avions (nom, capacité et ville dans laquelle 
-- ils se trouvent), des pilotes (nom et ville dans laquelle ils se trouvent), et les vols 
-- effectués par cette compagnie (impliquant un avion, un pilote, une ville de départ, 
-- une ville d’arrivée, une heure de départ et une heure d’arrivée).
-- Le schéma logique de cette base de données et le dictionnaire de données sont donnés ci-dessous :

-- AVIONS(No_av, Nom_av, cap, No_ville)
-- PILOTES(No_pil, Nom_pil, No_ville)
-- villes(No_ville, Nom_ville)
-- VOLS(No_vol, No_av, No_pil, No_ville_d, No_ville_a, Heure_d, Heure_a)

-- et le dictionnaire de données:

-- 	***** 	******** 	********** 				****  		**********
--  Table 	Attribut 	Sémantique 				Type 		Contrainte
-- 	***** 	******** 	********** 				****  		**********
-- AVIONS 	No_av 		Numéro de l’avion 		INT 		Primary key
-- AVIONS 	Nom_av 		Le nom de l’avion 		Varchar(50) NOT NULL
-- AVIONS 	cap 		Capacité de l’avion 	INT 		NOT NULL
-- AVIONS 	No_ville 	Le numéro de la ville 	INT			Foreign key. Fait référence à No_ville dans
--						où est affecté l’avion				la table VILLES

-- 	***** 	******** 	********** 				****  		**********
--  Table 	Attribut 	Sémantique 				Type 		Contrainte
-- 	***** 	******** 	********** 				****  		**********					  
-- PILOTES 	No_pil 		Numéro du pilote 		INT 			Primary key
-- PILOTES 	Nom_pil 	Nom du pilote 			Varchar(50) 	NOT NULL
-- PILOTES 	No_ville 	Ville du pilote 		INT 			Foreign key. Fait référence à No_ville dans
-- 																la table VILLES

-- 	***** 	******** 	********** 				****  		**********
--  Table 	Attribut 	Sémantique 				Type 		Contrainte
-- 	***** 	******** 	********** 				****  		**********
-- VILLES 	No_ville 	Numéro de la ville 		INT 			Primary key
-- VILLES 	Nom_ville 	Nom de la ville 		Varchar(50) 	NOT NULL

-- 	***** 	******** 	********** 				****  		**********
--  Table 	Attribut 	Sémantique 				Type 		Contrainte
-- 	***** 	******** 	********** 				****  		**********
-- VOLS 	No_vol 		Numéro du vol 			INT 			Primary key
-- VOLS 	No_av 		Numéro de l’avion du volINT 			Foreign key. Fait référence à No_av dans la 
-- 																table AVIONS
-- VOLS 	No_pil 		Numéro du pilote du vol INT 			Foreign key. Fait référence à No_pil dans la
--																table PILOTES
-- VOLS 	No_ville_d 	Numéro de la ville du 	INT  			Foreign key. Fait référence à No_ville dans
--  					départ du vol  							la table VILLES
-- VOLS 	No_ville_a 	Numéro de la ville  	INT 			Foreign key. Fait référence à No_ville dans
-- 						d’arrivée du vol  						la table VILLES
-- VOLS 	Heure_d 	L’heure du départ du	DATETIME 		NOT NULL
-- 						vol (avec la date et 
--  					l’heure)
-- VOLS 	Heure_a 	L’heure d’arrivée du vol DATETIME 		NOT NULL et doit être > Heure_d
-- 						(avec la date et l’heure)


-- Il est à noter que le type DATETIME (celui des attributs heure_a et heure_d) donne la date et l’heure.


-- Q1. On suppose que les tables VILLES, PILOTES et AVIONS déjà créées. Créer la table VOLS
-- en tenant compte des contraintes défini sur les colonnes de la table.

-- Q2. Lorsqu’un avion est retiré de la flotte, on veut archiver tous les vols effectués par cet avion
-- dans une table ArchVol de même schéma que la table VOLS. Ecrire un trigger sur la table
-- AVIONS qui archive les vols de l’avion supprimé.

-- Q3. Ecrire une procédure permettant d’effectuer l’ajout dans la base de données d’un nouveau
-- vol impliquant des villes, des avions et des pilotes déjà existants. Cette procédure doit permettre
-- d’exprimer le pilote et les villes impliquées par leur nom, et non leur identifiant, comme dans
-- l’exemple suivant :
-- Exec ajouter_vol(10, 1, 'toto', 'Casa', 'New York',
--  TO_DATETIME ('10-Septembre-19 14:10', 'DD-Mon-RR HH24:MI'),
--  TO_ DATETIME ('10-Septembre-19 18:10', 'DD-Mon-RR HH24:MI'));
-- N.B : On considère que l’utilisateur passe des paramètres cohérents : un identifiant d’avion qui existe,
-- et des noms de villes et de pilote qui correspondent chacun à un seul élément de la base de données.

-- Q4. Ecrire une fonction TotalHeurePilot qui retourne le nombre d’heure de vol d’un pilote passé
-- en paramètre par son numéro no_pil. Pour ce, vous pouvez utiliser la fonction
-- DATEDIFF(HOUR, @DateDebut, @DateFin) AS [Durée en Heures] pour récupérer la
-- différence entre 2 datestime en nombre d’heure


-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- D'AUTRES EXERCICES POUR S'ENTRAINER ET PREPARER L'EXAMEN
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- =========================================================================================
-- ****************************************************************************************
-- 1. A FAIRE
-- ****************************************************************************************
-- Exercice 2 : Créer une fonction `CA_Employe` qui retourne le chiffre d’affaires total réalisé 
-- par un employé.


-- ****************************************************************************************
-- 2. A FAIRE
-- ****************************************************************************************
-- Exercice 4 : Créer une procédure qui met à jour les commissions des employés : si leur chiffre 
-- d'affaires dépasse un seuil, augmentation de leur salaire, sinon baisse de leur commission 
-- (jamais négative).
-- les arguments de la procedure sont
-- le seuil du chiffre d'affaire
-- le taux d'augmentation,
-- le taux de diminution de la commission 

-- ****************************************************************************************
-- 3. A FAIRE
-- ****************************************************************************************
-- Exercice 1 : Afficher le nom et la ville d’un client donné. Gérer l’exception si le client 
-- n’existe pas (par nom, ERREUR ).
-- argument de la procedure le nom du client
-- Hypothese 1: plusieurs clients peuvent avoir le même nom
-- dans ce cas, il faut utiliser un curseur 
-- Hypothese 2: le nom est unique

-- *****************************************************************************************
-- 4. A FAIRE 
-- *****************************************************************************************
-- Exercice 1 : Créer un trigger qui vérifie que la quantité stockée d’un produit est suffisante 
-- avant l’insertion dans `Ligne_Commande`.
-- Hypothese: un produit est stocké dans un seul stock
-- les commandes qui ne vérifie la règle, seront stockée dans une table log 
-- les commandes qui ne vérifie la règle, seront stockée dans une table log 

create table TabLogInsertDetailsComs(
	Nolig				INT				IDENTITY	,
	NoCom				INT							,
	NoProd				INT							,
	QteCom				INT							,
	PvProd				DECIMAL(10,2)				,
	QteStock			INT							,
	QteSecur			INT							,
	QteManq				INT							,	-- quantité manquante
	DtInsert			DATE						,
	Oper				VARCHAR(50)						-- opérateur 
);



-- *****************************************************************************************
-- *****************************************************************************************
-- *****************************************************************************************
-- *****************************************************************************************
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
--									Fonctions et Procédures
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
-- Exercice 1 : Créer une procédure `Sup_Employe` qui supprime un employé donné. 
-- Gérer l’exception si l’employé a déjà géré des commandes.
-- ERREUR FK numéro 547

-- ****************************************************************************************
-- 1. A FAIRE
-- ****************************************************************************************
-- Exercice 2 : Créer une fonction `CA_Employe` qui retourne le chiffre d’affaires total réalisé 
-- par un employé.


-- Exercice 3 : Créer une procédure qui augmente les salaires des employés recrutés avant une année donnée. 
-- Archiver les augmentations dans une table `e_augmentation`.
-- La proecdue a comme argument l'année de recrutement et le taux d'augmentation
-- Pour récupérer l'année d'une date, utiliser la fonction YEAR ( date ) qui retourne l'année 
-- sous forme de INT

-- ****************************************************************************************
-- 2. A FAIRE
-- ****************************************************************************************
-- Exercice 4 : Créer une procédure qui met à jour les commissions des employés : si leur chiffre 
-- d'affaires dépasse un seuil, augmentation de leur salaire, sinon baisse de leur commission 
-- (jamais négative).
-- les arguments de la procedure sont
-- le seuil du chiffre d'affaire
-- le taux d'augmentation,
-- le taux de diminution de la commission 

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
--					Gestion des Exceptions
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
-- ****************************************************************************************
-- 3. A FAIRE
-- ****************************************************************************************
-- Exercice 1 : Afficher le nom et la ville d’un client donné. Gérer l’exception si le client 
-- n’existe pas (par nom, ERREUR ).
-- argument de la procedure le nom du client
-- Hypothese 1: plusieurs clients peuvent avoir le même nom
-- dans ce cas, il faut utiliser un curseur 
-- Hypothese 2: le nom est unique

-- Exercice 2 : Calculer le rapport entre le total des paiements et le paiement d’un client donné. 
-- Gérer les exceptions division par zéro et client inexistant.

-- Exercice 3 : Vérifier si un client a commandé un produit donné. Stocker le résultat dans une table 
-- `Etat_Commande`. Gérer les erreurs si le client ou le produit n’existe pas.
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
--											Curseurs
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
-- Exercice 1 : Créer un curseur qui affiche le nom complet de chaque client ayant effectué au moins 
-- une commande.

-- Exercice 2 : Créer un curseur qui affiche, pour chaque employé, les commandes qu’il a gérées 
-- (avec date de commande et statut).

-- Exercice 3 : Créer un curseur qui met à jour le stock de sécurité de tous les produits si le stock 
-- actuel est inférieur à un seuil donné.

-- Exercice 4 : Créer un curseur qui insère dans une table `Resultat` les produits dont le prix 
-- conseillé est supérieur à un seuil (500, 1000, etc.).
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
--							Triggers
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

-- *****************************************************************************************
-- *******************************  a faire ************************************************
-- *****************************************************************************************
-- Exercice 1 : Créer un trigger qui vérifie que la quantité stockée d’un produit est suffisante 
-- avant l’insertion dans `Ligne_Commande`.
-- Hypothese: un produit est stocké dans un seul stock
-- les commandes qui ne vérifie la règle, seront stockée dans une table log 
-- les commandes qui ne vérifie la règle, seront stockée dans une table log 

create table TabLogInsertDetailsComs(
	Nolig				INT				IDENTITY	,
	NoCom				INT							,
	NoProd				INT							,
	QteCom				INT							,
	PvProd				DECIMAL(10,2)				,
	QteStock			INT							,
	QteSecur			INT							,
	QteManq				INT							,	-- quantité manquante
	DtInsert			DATE						,
	Oper				VARCHAR(50)						-- opérateur 
);

-- *****************************************************************************************
-- *****************************************************************************************
-- *****************************************************************************************
-- *****************************************************************************************



-- Exercice 2 : Créer un trigger qui empêche la suppression d’un client s’il a encore 
-- des commandes actives.

-- Exercice 3 : Créer un trigger qui met à jour automatiquement la date d’entrée d’un employé 
-- si elle est NULL à l’insertion.

-- Exercice 4 : Créer un trigger qui vérifie, lors de l’insertion d’un produit, que son prix 
-- conseillé est cohérent (non négatif et supérieur à un minimum 
