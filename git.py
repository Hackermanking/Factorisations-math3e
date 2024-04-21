import sympy as sp

# Définir le logo ASCII
logo_ascii = """
██╗   ██╗███████╗██╗  ██╗ █████╗ ██╗   ██╗███████╗██████╗ 
██║   ██║██╔════╝██║  ██║██╔══██╗██║   ██║██╔════╝██╔══██╗
██║   ██║███████╗███████║███████║██║   ██║█████╗  ██████╔╝
╚██╗ ██╔╝╚════██║██╔══██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
 ╚████╔╝ ███████║██║  ██║██║  ██║╚██████╔╝███████╗██║  ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

# Couleurs pour le texte
M = "\033[1;31m"  # Rouge
warna = "\033[1;33m"  # Jaune
P = "\033[1;35m"  # Pourpre
H = "\033[1;32m"  # Vert
bblack = "\033[1;30m"  # Noir

def factoriser_expression(expression):
    expression_factorisee = sp.factor(expression)
    return expression_factorisee

if __name__ == "__main__":
    print(logo_ascii)  # Afficher le logo ASCII
    expression = input("Entrez l'expression à factoriser : ")
    expression_sympy = sp.sympify(expression)
    expression_factorisee = factoriser_expression(expression_sympy)
    print("Expression factorisée :", expression_factorisee)

    # Description formatée avec des couleurs
    owner_description = f"{M}Owner    : {M}Princi Sz{M}"
    tool_name_description = f"TOOL NAME : {warna}{P}get-cokkies&token{P}{warna}"
    groupe_fb_description = f"GROUPE-FB   : [TERMUX-COMAND]"
    statue_description = f"STATUE : {H}FREE{H}"
    facebook_description = f"Facebook : {bblack}Princi Sz{bblack}"
    tools_description = f"Tools    : {warna}[{M}VERSION 1.0{warna}]{warna}"

    # Imprimer les descriptions
    print(owner_description)
    print(tool_name_description)
    print(groupe_fb_description)
    print(statue_description)
    print(facebook_description)
    print(tools_description)