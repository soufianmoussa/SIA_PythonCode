from faker import Faker
import pyodbc
import time

# Initialiser Faker avec la langue anglaise pour des mois en anglais
faker = Faker('en_US')

def connect_to_database():
    """Connect to the SQL Server database using Windows Authentication."""
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'  # Remplacez si le serveur a un autre nom
        'DATABASE=justatest;'
        'Trusted_Connection=yes;'  # Utilise l'authentification Windows
    )
    return conn

def generate_random_data():
    """Génère des données aléatoires avec Faker."""
    return {
        "Date": faker.date_between(start_date="-5y", end_date="today").strftime('%d %B %Y'),
        "Région": faker.random_element(["Agadir", "Rabat", "Casablanca", "Tanger", "Marrakech"]),
        "Revenu_Ventes_MAD": faker.random_int(min=100000, max=1000000),
        "Coût_Production_MAD": faker.random_int(min=50000, max=500000),
        "Bénéfice_Net_MAD": faker.random_int(min=20000, max=300000),
        "Véhicules_Vendus": faker.random_int(min=10, max=200),
        "Clients_Nouveaux": faker.random_int(min=1, max=100),
        "Cash_Flow_MAD": faker.random_int(min=10000, max=500000),
        "Dette_Totale_MAD": faker.random_int(min=100000, max=1000000),
        "Investissements_MAD": faker.random_int(min=50000, max=200000),
        "Coût_Publicité_MAD": faker.random_int(min=10000, max=50000),
    }

def insert_data(conn, data):
    """Insert data into the Performance_Financiere table."""
    cursor = conn.cursor()
    query = """
        INSERT INTO Performance_Financiere (
            Date, Région, Revenu_Ventes_MAD, Coût_Production_MAD,
            Bénéfice_Net_MAD, Véhicules_Vendus, Clients_Nouveaux,
            Cash_Flow_MAD, Dette_Totale_MAD, Investissements_MAD,
            Coût_Publicité_MAD
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (
        data["Date"], data["Région"], data["Revenu_Ventes_MAD"],
        data["Coût_Production_MAD"], data["Bénéfice_Net_MAD"],
        data["Véhicules_Vendus"], data["Clients_Nouveaux"],
        data["Cash_Flow_MAD"], data["Dette_Totale_MAD"],
        data["Investissements_MAD"], data["Coût_Publicité_MAD"]
    ))
    conn.commit()
    print(f"Data inserted: {data}")

def main():
    conn = connect_to_database()
    try:
        while True:
            data = generate_random_data()
            insert_data(conn, data)
            time.sleep(20)  
    except KeyboardInterrupt:
        print("Script stopped.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
