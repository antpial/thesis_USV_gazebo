#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import math

WORLD_FILE = "/home/antoni/gazebo_maritime_ws/src/gazebo_maritime/worlds/sydney_regatta.sdf"
KML_FILE = "/home/antoni/gazebo_maritime_ws/src/autopilot/autopilot/checkpoints_list.kml"

def read_kml_coordinates(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    ns = {"kml": "http://www.opengis.net/kml/2.2"}

    coords = []
    for placemark in root.findall(".//kml:Placemark", ns):
        name = placemark.find("kml:name", ns).text
        coord_text = placemark.find(".//kml:coordinates", ns).text.strip()
        lon, lat, *alt = map(float, coord_text.split(","))
        coords.append((name, lon, lat, alt[0] if alt else 0.0))
    return coords

def approx_enu(lat, lon):
    lat0 = -33.724223
    lon0 = 150.679736
    m_per_deg_lat = 111132.92 - 559.82 * math.cos(2*math.radians(lat0)) + 1.175 * math.cos(4*math.radians(lat0))
    m_per_deg_lon = 111412.84 * math.cos(math.radians(lat0)) - 93.5 * math.cos(3*math.radians(lat0))
    d_lat = lat - lat0
    d_lon = lon - lon0
    north = d_lat * m_per_deg_lat
    east  = d_lon * m_per_deg_lon
    return east, north

def generate_marker_models(points, radius=10.0, length=2.0, r=0, g=1, b=0, a=0.5):
    """Zwraca listę elementów <model> gotowych do wklejenia do <world>"""
    models = []
    for i, (name, lon, lat, alt) in enumerate(points):
        x, y = approx_enu(lat, lon)
        model_name = f"marker_cylinder_{i+1}"

        model_elem = ET.Element("model", name=model_name)
        pose = ET.SubElement(model_elem, "pose")
        pose.text = f"{x} {y} 0 0 0 0"
        ET.SubElement(model_elem, "static").text = "true"

        link = ET.SubElement(model_elem, "link", name="link")
        visual = ET.SubElement(link, "visual", name="visual")
        geometry = ET.SubElement(visual, "geometry")
        cylinder = ET.SubElement(geometry, "cylinder")
        ET.SubElement(cylinder, "radius").text = str(radius)
        ET.SubElement(cylinder, "length").text = str(length)

        material = ET.SubElement(visual, "material")
        ET.SubElement(material, "ambient").text = f"{r} {g} {b} {a}"
        ET.SubElement(material, "diffuse").text = f"{r} {g} {b} {a}"

        models.append(model_elem)
    return models

def insert_models_into_world(world_file, model_elements):
    """Wstawia nowe modele i usuwa stare markery"""
    tree = ET.parse(world_file)
    root = tree.getroot()
    world = root.find("world")
    if world is None:
        raise ValueError("Nie znaleziono elementu <world> w pliku.")

    # usuń stare markery
    old_markers = [m for m in world.findall("model") if m.attrib.get("name","").startswith("marker_cylinder_")]
    for m in old_markers:
        world.remove(m)

    # dodaj nowe
    for m in model_elements:
        world.append(m)

    ET.indent(tree, space="  ")  # dodaje wcięcia, zachowuje strukturę
    tree.write(world_file, encoding="utf-8", xml_declaration=True)
    print(f"Wstawiono {len(model_elements)} modeli do pliku {world_file}.")

if __name__ == "__main__":
    points = read_kml_coordinates(KML_FILE)
    models = generate_marker_models(points)
    insert_models_into_world(WORLD_FILE, models)
