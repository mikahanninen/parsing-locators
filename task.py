import re

WINDOWS_LOCATOR_STRATEGIES = {
    "name": "name",
    "class_name": "class_name",
    "class": "class_name",
    "control_type": "control_type",
    "type": "control_type",
    "automation_id": "automation_id",
    "id": "automation_id",
    "partial name": "partial name",
    "regexp": "regexp",
    "parent": "parent",
}

def parsing(locator):
    regex = rf"({':|'.join(WINDOWS_LOCATOR_STRATEGIES.keys())}:|or|and)('{{1}}(.+)'{{1}}|(\S+))?"
    parts = re.finditer(regex, locator, re.IGNORECASE)
    
    locators = []
    match_type = "all"
    
    for part in parts:
        groups = part.groups()
        if groups[0].lower() == "or":
            match_type = "any"
        elif groups[0].lower() == "and":
            pass
        else:
            strategy, _ = groups[0].split(":")
            value = groups[2] if groups[2] else groups[3]
            locators.append([WINDOWS_LOCATOR_STRATEGIES[strategy], value])
    return locators

def print_parsing(locator):
    result = parsing(locator)
    print(result)

if __name__ == "__main__":
    print_parsing("name:lol")
    print_parsing("partial name:'abc dev' and class:aaa")
