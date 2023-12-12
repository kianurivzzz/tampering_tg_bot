import pygsheets
from pygsheets.client import Client

from config import SHEETS_TOKEN_PATH

class GoogleTable:
    def __init__(
        self,
        credence_service_file: str='',
        googlesheet_file_url: str=''
    ) -> None:

        self.credence_service_file: str = credence_service_file
        self.googlesheet_file_url: str = googlesheet_file_url


    def _get_googlesheet_by_url(
        self, googlesheet_client: pygsheets.client.Client
    ) -> pygsheets.Spreadsheet:

        try:
            sheets: pygsheets.Spreadsheet = googlesheet_client.open_by_url(
                self.googlesheet_file_url
            )
        except:
            return 'Нет доступа к таблице'
        return sheets


    def _get_googlesheet_client(self) -> Client:

        return pygsheets.authorize(
            service_file=self.credence_service_file
        )


    def get_worksheet(self, name_sheet):
        googlesheet_client: pygsheets.client.Client = self._get_googlesheet_client()
        wks: pygsheets.Spreadsheet = self._get_googlesheet_by_url(googlesheet_client)

        print('Таблица:', wks)


        try:
            return wks.worksheet(property='title', value=name_sheet)
        except:
            return 'Ошибка', Exception


def get_table(table, name_sheet):

        table = GoogleTable(
            credence_service_file=SHEETS_TOKEN_PATH,
            googlesheet_file_url=table
        )

        try:
            return table.get_worksheet(name_sheet)
        except:
            return 'Нет доступа к таблице'


def get_sheet(table, number):
    return get_table(table, number)
