import re

def check_allergies_extended(product_text: str, user_allergies: list) -> str:
    """
    Checks if the product text contains any allergens based on user input,
    including synonyms for each allergen.
    
    Args:
        product_text (str): The extracted nutrition label text.
        user_allergies (list of str): List of allergens selected by the user 
                                      (e.g., ['dairy', 'peanuts', 'gluten']).
    
    Returns:
        str: A warning message if potential allergens are found; otherwise,
             a message indicating no allergens detected.
    """
    # Normalize the product text to lowercase.
    normalized_text = product_text.lower()

    # Mapping from generic allergen names to common synonyms/keywords.
    allergy_synonyms = {
        "dairy": ["milk", "cheese", "butter", "curd", "yogurt", "cream", "whey", "casein"],
        "peanuts": ["peanut", "groundnut", "arachis"],
        "gluten": ["wheat", "barley", "rye", "oats", "gluten"],
        "soy": ["soy", "soybean", "tofu", "edamame", "soymilk"],
        "tree nuts": ["almond", "cashew", "walnut", "pecan", "hazelnut", "pistachio", "macadamia"],
        "egg": ["egg", "albumin"],
        # Add additional allergens and synonyms as needed.
    }

    found_allergens = []

    # For each user-specified allergen, check for any synonym in the text.
    for allergy in user_allergies:
        allergy_lower = allergy.lower()
        synonyms = allergy_synonyms.get(allergy_lower, [allergy_lower])
        
        # Use regex with word boundaries to avoid partial matches.
        for synonym in synonyms:
            if re.search(r'\b' + re.escape(synonym) + r'\b', normalized_text):
                found_allergens.append(allergy)
                break  # Stop checking synonyms once a match is found.

    if found_allergens:
        return f"WARNING: The product contains {', '.join(found_allergens)} which may cause an allergic reaction."
    else:
        return "No allergens detected in the product."
