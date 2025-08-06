#xml_parser.py
from lxml import etree

def parse_cpe_xml(xml_file):
    # Define namespaces for CPE XML
    ns = {'default': "http://cpe.mitre.org/dictionary/2.0",
            'cpe-23': "http://scap.nist.gov/schema/cpe-extension/2.3"
            }
    
    cpe_entries = []
    try:
        tree = etree.parse(xml_file)
        root = tree.getroot()
    except (etree.XMLSyntaxError, FileNotFoundError) as e:
        raise ValueError(f"Error parsing XML file: {e}")

    # Extract CPE entries
    for cpe_item in root.findall('default:cpe-item', ns):
        # CPE Title
        cpe_title = cpe_item.findtext('default:title', default="N/A", namespaces=ns)

        # CPE 2.2 URI
        cpe_22_uri = cpe_item.get('name', "N/A")

        # CPE 2.3 URI
        cpe_23_elem = cpe_item.find('cpe-23:cpe23-item', ns)
        cpe_23_uri = cpe_23_elem.get('name') if cpe_23_elem is not None else "N/A"

        # Reference links
        references = []
        for ref in cpe_item.findall('default:references/default:reference', ns):
            href = ref.get('href')
            if href:
                references.append(href)

        # Deprecation dates
        cpe_22_deprecation = cpe_item.get('deprecation_date', "N/A")
        if cpe_22_deprecation != "N/A":
            cpe_22_deprecation = cpe_22_deprecation.split('T')[0]

        cpe_23_deprecation = "N/A"
        if cpe_23_elem is not None:
            dep_elem = cpe_23_elem.find('cpe-23:deprecation', ns)
            if dep_elem is not None:
                date = dep_elem.get('date')
                if date:
                    cpe_23_deprecation = date.split('T')[0]

        # Add entry
        cpe_entries.append({
            'cpe_title': cpe_title,
            'cpe_22_uri': cpe_22_uri,
            'cpe_23_uri': cpe_23_uri,
            'reference_links': references,
            'cpe_22_deprecation_date': cpe_22_deprecation,
            'cpe_23_deprecation_date': cpe_23_deprecation
        })

    return cpe_entries