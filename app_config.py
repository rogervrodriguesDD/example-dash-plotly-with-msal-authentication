import os

CLIENT_ID = "Here-is-the-app-registration-client-id" # Application (client) ID of app registration

# Importando Client Secret (arquivo disponível apenas em DEV)
if os.path.exists('Client-Secret-DEV'):
    with open('Client-Secret-DEV', 'r') as f:
        CLIENT_SECRET = f.read()

else: # Em ambiente de Produção
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Em caso de falta da chave
if not CLIENT_SECRET:
    raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
