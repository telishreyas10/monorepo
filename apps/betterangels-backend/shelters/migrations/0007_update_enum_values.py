# migrations/0007_update_enum_values.py

from django.db import migrations
import shelters.enums
import django_choices_field.fields


def update_enum_values(apps, schema_editor, model_name, field_name, value_mapping):
    for old_value, new_value in value_mapping.items():
        schema_editor.execute(
            f"UPDATE {model_name} SET {field_name} = '{new_value}' WHERE {field_name} = '{old_value}'"
        )


def update_enum_values_forward(apps, schema_editor):
    enum_mappings = {
        "shelters_sheltertype": {
            "A Bridge Home": "a_bridge_home",
            "Crisis Housing": "crisis_housing",
            "Emergency Shelter": "emergency_shelter",
            "Faith Based": "faith_based",
            "Interim Housing": "interim_housing",
            "Permanent Housing": "permanent_housing",
            "Project Home Key (PHK)": "project_homekey",
            "Rapid Rehousing": "rapid_rehousing",
            "Recuperative Care": "recuperative_care",
            "Roadmap Home": "roadmap_home",
            "Safe Park LA": "safe_park_la",
            "Sober Living": "sober_living",
            "Tiny Home Village": "tiny_home_village",
            "Transitional Housing": "transitional_housing",
            "Winter Shelter": "winter_shelter",
        },
        "shelters_population": {
            "B7 Bridge Housing for Persons Exiting Justice System Institutions": "justice_system_exiting",
            "Enhanced Bridge Housing for Women": "enhanced_bridge_housing_women",
            "Enhanced Bridge Housing for Older Adults": "enhanced_bridge_housing_older_adults",
            "Adults": "adults",
            "Boys": "boys",
            "Children": "children",
            "Domestic Violence (DV/IPV)": "domestic_violence",
            "Families": "families",
            "Girls": "girls",
            "HIV/AIDS": "hiv_and_aids",
            "Human Trafficking": "human_trafficking",
            "LGBTQ": "lgbtq",
            "Men": "men",
            "Seniors (55+)": "seniors",
            "Veterans": "veterans",
            "Women": "women",
            "Youth (TAY)": "youth",
        },
        "shelters_immediateneed": {
            "Clothing": "clothing",
            "Food": "food",
            "Showers": "showers",
        },
        "shelters_generalservice": {
            "Case Management": "case_management",
            "Childcare": "childcare",
            "Computers": "computers",
            "Financial Literacy/Assistance": "financial_literacy_assistance",
            "Housing Navigation": "housing_navigation",
            "Legal Assistance": "legal_assistance",
            "Mail": "mail",
            "Phone": "phone",
            "Transportation": "transportation",
        },
        "shelters_healthservice": {
            "Medication Administration": "medication_administration",
            "Medication Monitoring": "medication_monitoring",
            "Mental Health": "mental_health",
            "Substance Use Treatment": "substance_use_treatment",
        },
        "shelters_careerservice": {
            "Job Training": "job_training",
            "Life Skills Training": "life_skills_training",
            "Tutoring": "tutoring",
        },
        "shelters_funder": {
            "DHS": "dhs",
            "DMH": "dmh",
            "Federal Funding": "federal_funding",
            "HOPWA": "hopwa",
            "LAHSA": "lahsa",
            "Private": "private",
            "City of Los Angeles": "city_of_los_angeles",
        },
        "shelters_accessibility": {
            "Medical Equipment Permitted": "medical_equipment_permitted",
            "Wheelchair Accessible": "wheelchair_accessible",
        },
        "shelters_storage": {
            "Amnesty Lockers": "amnesty_lockers",
            "Lockers": "lockers",
            "Storage": "storage",
        },
        "shelters_parking": {
            "Auto or Small Truck": "auto_or_small_truck",
            "Bicycle": "bicycle",
            "Motorcycle": "motorcycle",
            "RV": "rv",
        },
        "shelters_entryrequirement": {
            "Medicaid or Medicare": "medicaid_or_medicare",
            "Photo ID": "photo_id",
            "Referral": "referral",
            "Reservation": "reservation",
        },
        "shelters_city": {
            "Agoura Hills": "agoura_hills",
            "Alhambra": "alhambra",
            "Arcadia": "arcadia",
            "Artesia": "artesia",
            "Avalon": "avalon",
            "Azusa": "azusa",
            "Baldwin Park": "baldwin_park",
            "Bell": "bell",
            "Bellflower": "bellflower",
            "Bell Gardens": "bell_gardens",
            "Beverly Hills": "beverly_hills",
            "Bradbury": "bradbury",
            "Burbank": "burbank",
            "Calabasas": "calabasas",
            "Carson": "carson",
            "Cerritos": "cerritos",
            "Claremont": "claremont",
            "Commerce": "commerce",
            "Compton": "compton",
            "Covina": "covina",
            "Cudahy": "cudahy",
            "Culver City": "culver_city",
            "Diamond Bar": "diamond_bar",
            "Downey": "downey",
            "Duarte": "duarte",
            "El Monte": "el_monte",
            "El Segundo": "el_segundo",
            "Gardena": "gardena",
            "Glendale": "glendale",
            "Glendora": "glendora",
            "Hawaiian Gardens": "hawaiian_gardens",
            "Hawthorne": "hawthorne",
            "Hermosa Beach": "hermosa_beach",
            "Hidden Hills": "hidden_hills",
            "Hollywood": "hollywood",
            "Huntington Park": "huntington_park",
            "Industry": "industry",
            "Inglewood": "inglewood",
            "Irwindale": "irwindale",
            "La Canada Flintridge": "la_canada_flintridge",
            "La Habra Heights": "la_habra_heights",
            "La Mirada": "la_mirada",
            "La Puente": "la_puente",
            "La Verne": "la_verne",
            "Lakewood": "lakewood",
            "Lancaster": "lancaster",
            "Lawndale": "lawndale",
            "Lomita": "lomita",
            "Long Beach": "long_beach",
            "Los Angeles": "los_angeles",
            "Lynwood": "lynwood",
            "Malibu": "malibu",
            "Manhattan Beach": "manhattan_beach",
            "Maywood": "maywood",
            "Monrovia": "monrovia",
            "Montebello": "montebello",
            "Monterey Park": "monterey_park",
            "Norwalk": "norwalk",
            "Palmdale": "palmdale",
            "Palos Verdes Estates": "palos_verdes_estates",
            "Paramount": "paramount",
            "Pasadena": "pasadena",
            "Pico Rivera": "pico_rivera",
            "Pomona": "pomona",
            "Rancho Palos Verdes": "rancho_palos_verdes",
            "Redondo Beach": "redondo_beach",
            "Rolling Hills": "rolling_hills",
            "Rolling Hills Estates": "rolling_hills_estates",
            "Rosemead": "rosemead",
            "San Dimas": "san_dimas",
            "San Fernando": "san_fernando",
            "San Gabriel": "san_gabriel",
            "San Marino": "san_marino",
            "Santa Clarita": "santa_clarita",
            "Santa Fe Springs": "santa_fe_springs",
            "Santa Monica": "santa_monica",
            "Sierra Madre": "sierra_madre",
            "Signal Hill": "signal_hill",
            "South El Monte": "south_el_monte",
            "South Gate": "south_gate",
            "South Pasadena": "south_pasadena",
            "Temple City": "temple_city",
            "Torrance": "torrance",
            "Vernon": "vernon",
            "Venice": "venice",
            "Walnut": "walnut",
            "West Covina": "west_covina",
            "West Hollywood": "west_hollywood",
            "Westlake Village": "westlake_village",
            "West Los Angeles": "west_los_angeles",
            "Whittier": "whittier",
        },
        "shelters_pet": {
            "Cats": "cats",
            "Dogs >25lbs": "dogs_over_25lbs",
            "Dogs <25lbs": "dogs_under_25lbs",
            "Emotional Support": "emotional_support",
            "Exotics": "exotics",
            "Service Animal": "service_animal",
        },
        "shelters_sleepingoption": {
            "Bunk beds": "bunk_beds",
            "Dormitory": "dormitory",
            "Low Barrier": "low_barrier",
            "Motel": "motel",
            "Shared Rooms": "shared_rooms",
            "Single Room": "single_room",
        },
    }

    for model_name, value_mapping in enum_mappings.items():
        update_enum_values(apps, schema_editor, model_name, "name", value_mapping)


def update_enum_values_backward(apps, schema_editor):
    # Reverse the mappings for each model and field
    enum_mappings = {
        "shelters_sheltertype": {
            "a_bridge_home": "A Bridge Home",
            "crisis_housing": "Crisis Housing",
            "emergency_shelter": "Emergency Shelter",
            "faith_based": "Faith Based",
            "interim_housing": "Interim Housing",
            "permanent_housing": "Permanent Housing",
            "project_homekey": "Project Home Key (PHK)",
            "rapid_rehousing": "Rapid Rehousing",
            "recuperative_care": "Recuperative Care",
            "roadmap_home": "Roadmap Home",
            "safe_park_la": "Safe Park LA",
            "sober_living": "Sober Living",
            "tiny_home_village": "Tiny Home Village",
            "transitional_housing": "Transitional Housing",
            "winter_shelter": "Winter Shelter",
        },
        "shelters_population": {
            "justice_system_exiting": "B7 Bridge Housing for Persons Exiting Justice System Institutions",
            "enhanced_bridge_housing_women": "Enhanced Bridge Housing for Women",
            "enhanced_bridge_housing_older_adults": "Enhanced Bridge Housing for Older Adults",
            "adults": "Adults",
            "boys": "Boys",
            "children": "Children",
            "domestic_violence": "Domestic Violence (DV/IPV)",
            "families": "Families",
            "girls": "Girls",
            "hiv_and_aids": "HIV/AIDS",
            "human_trafficking": "Human Trafficking",
            "lgbtq": "LGBTQ",
            "men": "Men",
            "seniors": "Seniors (55+)",
            "veterans": "Veterans",
            "women": "Women",
            "youth": "Youth (TAY)",
        },
        "shelters_immediateneed": {
            "clothing": "Clothing",
            "food": "Food",
            "showers": "Showers",
        },
        "shelters_generalservice": {
            "case_management": "Case Management",
            "childcare": "Childcare",
            "computers": "Computers",
            "financial_literacy_assistance": "Financial Literacy/Assistance",
            "housing_navigation": "Housing Navigation",
            "legal_assistance": "Legal Assistance",
            "mail": "Mail",
            "phone": "Phone",
            "transportation": "Transportation",
        },
        "shelters_healthservice": {
            "medication_administration": "Medication Administration",
            "medication_monitoring": "Medication Monitoring",
            "mental_health": "Mental Health",
            "substance_use_treatment": "Substance Use Treatment",
        },
        "shelters_careerservice": {
            "job_training": "Job Training",
            "life_skills_training": "Life Skills Training",
            "tutoring": "Tutoring",
        },
        "shelters_funder": {
            "dhs": "DHS",
            "dmh": "DMH",
            "federal_funding": "Federal Funding",
            "hopwa": "HOPWA",
            "lahsa": "LAHSA",
            "private": "Private",
            "city_of_los_angeles": "City of Los Angeles",
        },
        "shelters_accessibility": {
            "medical_equipment_permitted": "Medical Equipment Permitted",
            "wheelchair_accessible": "Wheelchair Accessible",
        },
        "shelters_storage": {
            "amnesty_lockers": "Amnesty Lockers",
            "lockers": "Lockers",
            "storage": "Storage",
        },
        "shelters_parking": {
            "auto_or_small_truck": "Auto or Small Truck",
            "bicycle": "Bicycle",
            "motorcycle": "Motorcycle",
            "rv": "RV",
        },
        "shelters_entryrequirement": {
            "medicaid_or_medicare": "Medicaid or Medicare",
            "photo_id": "Photo ID",
            "referral": "Referral",
            "reservation": "Reservation",
        },
        "shelters_city": {
            "agoura_hills": "Agoura Hills",
            "alhambra": "Alhambra",
            "arcadia": "Arcadia",
            "artesia": "Artesia",
            "avalon": "Avalon",
            "azusa": "Azusa",
            "baldwin_park": "Baldwin Park",
            "bell": "Bell",
            "bellflower": "Bellflower",
            "bell_gardens": "Bell Gardens",
            "beverly_hills": "Beverly Hills",
            "bradbury": "Bradbury",
            "burbank": "Burbank",
            "calabasas": "Calabasas",
            "carson": "Carson",
            "cerritos": "Cerritos",
            "claremont": "Claremont",
            "commerce": "Commerce",
            "compton": "Compton",
            "covina": "Covina",
            "cudahy": "Cudahy",
            "culver_city": "Culver City",
            "diamond_bar": "Diamond Bar",
            "downey": "Downey",
            "duarte": "Duarte",
            "el_monte": "El Monte",
            "el_segundo": "El Segundo",
            "gardena": "Gardena",
            "glendale": "Glendale",
            "glendora": "Glendora",
            "hawaiian_gardens": "Hawaiian Gardens",
            "hawthorne": "Hawthorne",
            "hermosa_beach": "Hermosa Beach",
            "hidden_hills": "Hidden Hills",
            "hollywood": "Hollywood",
            "huntington_park": "Huntington Park",
            "industry": "Industry",
            "inglewood": "Inglewood",
            "irwindale": "Irwindale",
            "la_canada_flintridge": "La Canada Flintridge",
            "la_habra_heights": "La Habra Heights",
            "la_mirada": "La Mirada",
            "la_puente": "La Puente",
            "la_verne": "La Verne",
            "lakewood": "Lakewood",
            "lancaster": "Lancaster",
            "lawndale": "Lawndale",
            "lomita": "Lomita",
            "long_beach": "Long Beach",
            "los_angeles": "Los Angeles",
            "lynwood": "Lynwood",
            "malibu": "Malibu",
            "manhattan_beach": "Manhattan Beach",
            "maywood": "Maywood",
            "monrovia": "Monrovia",
            "montebello": "Montebello",
            "monterey_park": "Monterey Park",
            "norwalk": "Norwalk",
            "palmdale": "Palmdale",
            "palos_verdes_estates": "Palos Verdes Estates",
            "paramount": "Paramount",
            "pasadena": "Pasadena",
            "pico_rivera": "Pico Rivera",
            "pomona": "Pomona",
            "rancho_palos_verdes": "Rancho Palos Verdes",
            "redondo_beach": "Redondo Beach",
            "rolling_hills": "Rolling Hills",
            "rolling_hills_estates": "Rolling Hills Estates",
            "rosemead": "Rosemead",
            "san_dimas": "San Dimas",
            "san_fernando": "San Fernando",
            "san_gabriel": "San Gabriel",
            "san_marino": "San Marino",
            "santa_clarita": "Santa Clarita",
            "santa_fe_springs": "Santa Fe Springs",
            "santa_monica": "Santa Monica",
            "sierra_madre": "Sierra Madre",
            "signal_hill": "Signal Hill",
            "south_el_monte": "South El Monte",
            "south_gate": "South Gate",
            "south_pasadena": "South Pasadena",
            "temple_city": "Temple City",
            "torrance": "Torrance",
            "vernon": "Vernon",
            "venice": "Venice",
            "walnut": "Walnut",
            "west_covina": "West Covina",
            "west_hollywood": "West Hollywood",
            "westlake_village": "Westlake Village",
            "west_los_angeles": "West Los Angeles",
            "whittier": "Whittier",
        },
        "shelters_pet": {
            "cats": "Cats",
            "dogs_over_25lbs": "Dogs >25lbs",
            "dogs_under_25lbs": "Dogs <25lbs",
            "emotional_support": "Emotional Support",
            "exotics": "Exotics",
            "service_animal": "Service Animal",
        },
        "shelters_sleepingoption": {
            "bunk_beds": "Bunk beds",
            "dormitory": "Dormitory",
            "low_barrier": "Low Barrier",
            "motel": "Motel",
            "shared_rooms": "Shared Rooms",
            "single_room": "Single Room",
        },
    }

    for model_name, value_mapping in enum_mappings.items():
        update_enum_values(apps, schema_editor, model_name, "name", value_mapping)


class Migration(migrations.Migration):

    dependencies = [
        ("shelters", "0006_alter_shelter_options_shelter_reviewed"),  # Update with the correct previous migration
    ]

    operations = [
        migrations.AlterField(
            model_name="funder",
            name="name",
            field=django_choices_field.fields.TextChoicesField(
                blank=True,
                choices=[
                    ("dhs", "DHS"),
                    ("dmh", "DMH"),
                    ("federal_funding", "Federal Funding"),
                    ("hopwa", "HOPWA"),
                    ("lahsa", "LAHSA"),
                    ("private", "Private"),
                    ("city_of_los_angeles", "City of Los Angeles"),
                ],
                choices_enum=shelters.enums.FunderChoices,
                max_length=19,
                null=True,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="population",
            name="name",
            field=django_choices_field.fields.TextChoicesField(
                blank=True,
                choices=[
                    ("adults", "Adults"),
                    ("boys", "Boys"),
                    ("children", "Children"),
                    ("domestic_violence", "Domestic Violence (DV/IPV)"),
                    ("families", "Families"),
                    ("girls", "Girls"),
                    ("hiv_and_aids", "HIV/AIDS"),
                    ("human_trafficking", "Human Trafficking"),
                    ("lgbtq", "LGBTQ"),
                    ("men", "Men"),
                    ("seniors", "Seniors (55+)"),
                    ("veterans", "Veterans"),
                    ("women", "Women"),
                    ("youth", "Youth (TAY)"),
                    ("justice_system_exiting", "B7 Bridge Housing for Persons Exiting Justice System Institutions"),
                    ("enhanced_bridge_housing_women", "Enhanced Bridge Housing for Women"),
                    ("enhanced_bridge_housing_older_adults", "Enhanced Bridge Housing for Older Adults"),
                ],
                choices_enum=shelters.enums.PopulationChoices,
                max_length=36,
                null=True,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="sheltertype",
            name="name",
            field=django_choices_field.fields.TextChoicesField(
                blank=True,
                choices=[
                    ("a_bridge_home", "A Bridge Home"),
                    ("crisis_housing", "Crisis Housing"),
                    ("emergency_shelter", "Emergency Shelter"),
                    ("faith_based", "Faith Based"),
                    ("interim_housing", "Interim Housing"),
                    ("permanent_housing", "Permanent Housing"),
                    ("project_homekey", "Project Home Key (PHK)"),
                    ("rapid_rehousing", "Rapid Rehousing"),
                    ("recuperative_care", "Recuperative Care"),
                    ("roadmap_home", "Roadmap Home"),
                    ("safe_park_la", "Safe Park LA"),
                    ("sober_living", "Sober Living"),
                    ("tiny_home_village", "Tiny Home Village"),
                    ("transitional_housing", "Transitional Housing"),
                    ("winter_shelter", "Winter Shelter"),
                ],
                choices_enum=shelters.enums.ShelterChoices,
                max_length=20,
                null=True,
                unique=True,
            ),
        ),
        migrations.RunPython(update_enum_values_forward, update_enum_values_backward),
    ]