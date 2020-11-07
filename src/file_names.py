from pathlib import Path
import os

BASE = Path(os.path.dirname(__file__)).parent
CLIENT_SYN = os.path.join(BASE, "keywords/client_synonyms.txt")
COMPANY_SYN = os.path.join(BASE, "keywords/company_synonyms.txt")
PERMISSIVE_VERBS = os.path.join(BASE, "keywords/permissive_verbs.txt")
OBLIGATORY_VERBS = os.path.join(BASE, "keywords/obligatory_verbs.txt")
OBLIGATORY_VERBS_CONST = os.path.join(BASE, "keywords/obligatory_verbs_constant.txt")
REPLACEMENTS = os.path.join(BASE, "keywords/replacements.txt")