import PySimpleGUI as sg
import logging
from auth import auth_service


layout = [
    [sg.T("Put in your TD Ameritrade API Key:")],
    [sg.I(k='tda_key')],
    [sg.B("Exit"), sg.B("Continue")],
        ]

window = sg.Window("Token Generator", layout)


def main():

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Continue":
            tda_api_key = values['tda_key']
            token = auth_service(tda_api_key)
            token_popup = sg.Window("Token", [
                [sg.T("Copy your token out of this window (CTRL+C for copy):")],
                [sg.Multiline(token, size=(50, 10))],
                [sg.B("Exit")]
                                            ])
            while True:
                event, values = token_popup.read()
                if event == "Exit" or event == sg.WIN_CLOSED:
                    token_popup.close()
                    window.close()
                    break


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        filename='error.log', encoding='utf-8', level=logging.INFO)
    try:
        main()
    except Exception as Argument:
        print(f'ERROR EXCEPTION: {Argument}')
        logging.error(Argument)
