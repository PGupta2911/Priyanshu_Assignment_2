import sqlite3

# Step 1: Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect(':memory:')  # Using in-memory database for simplicity
cursor = conn.cursor()

# Step 2: Create the Patients table
cursor.execute('''
CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT NOT NULL,
    conditions TEXT
)
''')

# Step 3: Insert sample data into the table
patients_data = [
    (1, 'Daniel', 'YFEV COUGH'),
    (2, 'Alice', ''),
    (3, 'Bob', 'DIAB100 MYOP'),
    (4, 'George', 'ACNE DIAB100'),
    (5, 'Alain', 'DIAB201'),
]
cursor.executemany('INSERT INTO Patients (patient_id, patient_name, conditions) VALUES (?, ?, ?)', patients_data)

# Step 4: Query to find patients with conditions starting with 'DIAB1'
query = '''
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE '%DIAB1%'
'''
cursor.execute(query)

# Step 5: Fetch and display results
results = cursor.fetchall()
print("Patients with Type I Diabetes:")
print("+------------+--------------+--------------+")
print("| patient_id | patient_name | conditions   |")
print("+------------+--------------+--------------+")
for row in results:
    print(f"| {row[0]:<10} | {row[1]:<12} | {row[2]:<12} |")
print("+------------+--------------+--------------+")

# Step 6: Close the connection
conn.close()
