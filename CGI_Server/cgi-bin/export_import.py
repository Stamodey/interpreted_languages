import sqlite3
import json
import xml.etree.ElementTree as ET

def export_to_json():
    conn = sqlite3.connect('D:/универ/lab10-11/architecture.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM styles")
    data = cursor.fetchall()
    with open("styles.json", "w") as f:
        json.dump(data, f)

def export_to_xml():
    conn = sqlite3.connect('D:/универ/lab10-11/architecture.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM styles")
    data = cursor.fetchall()

    root = ET.Element("styles")
    for row in data:
        style = ET.SubElement(root, "style")
        ET.SubElement(style, "id").text = str(row[0])
        ET.SubElement(style, "name").text = row[1]
        ET.SubElement(style, "description").text = row[2]

    tree = ET.ElementTree(root)
    tree.write("styles.xml")

if __name__ == "__main__":
    export_to_json()
    export_to_xml()
