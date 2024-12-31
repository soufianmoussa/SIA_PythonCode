-- Créer une base de données
CREATE DATABASE MaBaseDeDonnees;

-- Utiliser la base de données créée
USE MaBaseDeDonnees;

-- Créer la table Performance_Financiere
CREATE TABLE Performance_Financiere (
    Date DATE NOT NULL,
    Région VARCHAR(100) NOT NULL,
    Revenu_Ventes_MAD INT NOT NULL,
    Coût_Production_MAD INT NOT NULL,
    Bénéfice_Net_MAD INT NOT NULL,
    Véhicules_Vendus INT NOT NULL,
    Clients_Nouveaux INT NOT NULL,
    Cash_Flow_MAD INT NOT NULL,
    Dette_Totale_MAD INT NOT NULL,
    Investissements_MAD INT NOT NULL,
    Coût_Publicité_MAD INT NOT NULL
);