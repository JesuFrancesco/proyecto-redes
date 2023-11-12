#Imports
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES=["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID="18p2Sp54yEv4Fb8PEHO4sr0f1uJXlRD7UjZov2qC2Gmc"
range_name='Sheet1!A1:C6'

def llamargooglesheets(lista):
    
    #Largo de la lista
    listalen=len(lista)

    credentials=None
    if os.path.exists("token.jason"):
        credentials= Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow= InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials= flow.run_local_server(port=0)
        with open("token.json","w") as token:
            token.write(credentials.to_json())

    #Exportar datos a Google Sheets
    try:
        service=build("sheets","v4",credentials=credentials)
        sheets=service.spreadsheets()
        #Borrar datos previos
        for row in range(2,6):
            for column in range(1,7):
                letra = chr(ord('A') + column - 1)
                result=sheets.values().clear(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!{letra}{row}").execute()
        #Importar nuevos datos
        for row in range(2,listalen+2):
            paqPorc=lista[row-2].paqPerdidos/10
            result=sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!A{row}",
                                          valueInputOption="USER_ENTERED", body={"values":[[f"{lista[row-2].Ejecucion}"]]}).execute()
            result=sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!B{row}",
                                          valueInputOption="USER_ENTERED", body={"values":[[f"{lista[row-2].Servidor}"]]}).execute()
            result=sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!C{row}",
                                          valueInputOption="USER_ENTERED", body={"values":[[f"{str(lista[row-2].latencia).replace('.',',')}"]]}).execute()
            result=sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!D{row}",
                                          valueInputOption="USER_ENTERED", body={"values":[[f"{str(paqPorc).replace('.',',')}"]]}).execute()
            result=sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!E{row}",
                                          valueInputOption="USER_ENTERED", body={"values":[[f"{str(lista[row-2].velSubida).replace('.',',')}"]]}).execute()
            result=sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!F{row}",
                                          valueInputOption="USER_ENTERED", body={"values":[[f"{str(lista[row-2].velDescarga).replace('.',',')}"]]}).execute()

    except HttpError as error:
        print(error)