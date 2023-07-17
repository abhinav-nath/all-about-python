import sys

import requests

# Usage:
# python country_info.py <country name>


def format_population(population):
    units = [
        "",
        "thousand",
        "million",
        "billion",
        "trillion",
    ]  # Add more units as needed
    unit_index = max(0, min(len(units) - 1, (len(str(population)) - 1) // 3))

    formatted_population = (
        f"{population / (1000 ** unit_index):.2f} {units[unit_index]}"
    )
    return formatted_population


def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            country_data = data[
                0
            ]  # The API returns a list of country data; we get the first item.

            name = country_data["name"]["common"]
            population = country_data["population"]
            formatted_population = format_population(population)
            capital = country_data.get("capital", ["N/A"])[0]
            region = country_data.get("region", "N/A")
            subregion = country_data.get("subregion", "N/A")
            continents = ", ".join(country_data.get("continents", ["N/A"]))
            languages = ", ".join(lang for lang in country_data["languages"].values())
            currencies = ", ".join(
                f"{curr['name']} ({curr['symbol']})"
                for curr in country_data["currencies"].values()
            )
            area = country_data.get("area", "N/A")
            borders = ", ".join(country_data.get("borders", ["N/A"]))
            timezones = ", ".join(country_data.get("timezones", ["N/A"]))
            calling_codes_root = country_data.get("idd", {}).get("root", "N/A")
            calling_codes_suffixes = country_data.get("idd", {}).get("suffixes", [])
            calling_codes = ", ".join(
                f"{calling_codes_root}{suffix}" for suffix in calling_codes_suffixes
            )
            demonym = country_data.get("demonyms", {}).get("eng", "N/A")
            latlng = country_data.get("latlng", ["N/A"])
            lat, lng = latlng if len(latlng) == 2 else ("N/A", "N/A")

            print(f"Country: {name}")
            print(f"Population: {formatted_population}")
            print(f"Capital: {capital}")
            print(f"Region: {region}")
            print(f"Subregion: {subregion}")
            print(f"Continents: {continents}")
            print(f"Languages: {languages}")
            print(f"Currencies: {currencies}")
            print(f"Area: {area} sq. km")
            print(f"Borders: {borders}")
            print(f"Timezones: {timezones}")
            print(f"Calling Codes: {calling_codes}")
            print(f"Demonym: {demonym}")
            print(f"Latitude: {lat}")
            print(f"Longitude: {lng}")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the country name as a command-line argument.")
        sys.exit(1)

    country_name = " ".join(sys.argv[1:])
    get_country_info(country_name)
