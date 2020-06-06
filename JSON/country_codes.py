from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回两个字母的国别名"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
