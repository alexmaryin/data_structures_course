import os
import requests


def translate_file(url, params, filepath, mimetype):
    basename = os.path.basename(filepath)
    files = {"file": (basename, open(filepath, 'rb'), mimetype)}
    shortname = os.path.splitext(os.path.basename(filepath))[0]
    ext = url.split("/")[-1]
    file_exts = {
        "text": ".txt",
        "docx": ".docx",
        "html": ".html",
    }

    try:
        resp = requests.post(url, params=params, files=files)
    except requests.exceptions.RequestException as err:
        print(err)
    else:
        if resp.status_code != 200:
            if "application/json" in resp.headers.get("Content-Type"):
                print(resp.json())
            else:
                print(resp.status_code)
        else:
            if params['as'] == "json":
                data = resp.json()
                status = data["status"]
                print(status)
                if status == 200:
                    print(data["data"])
                else:
                    print(data["message"])
            else:
                out = os.path.join(
                    os.path.abspath("out"), f"{shortname}{file_exts[ext]}")
                with open(out, "wb") as f:
                    f.write(resp.content)


def translate_text(url, params):
    try:
        resp = requests.post(url, params=params)
    except requests.exceptions.RequestException as err:
        print(err)
    else:
        if resp.status_code != 200:
            if "application/json" in resp.headers.get("Content-Type"):
                print(resp.json())
            else:
                print(resp.status_code)
        else:
            if params['as'] == "json":
                data = resp.json()
                status = data["status"]
                print(status)
                if status == 200:
                    print(data["data"])
                else:
                    print(data["message"])
            else:
                print(resp.text)


def main():
    # ---------------------------------------------------------
    # устанавливем текущую рабочую директорию  (если нужно)
    # os.chdir(os.path.dirname(__file__))
    url = "https://fasttranslator.herokuapp.com/api/v1.0/file/to/text"
    # ответ будет возвращен как файл
    params = {"lang": "ru-uk", "as": "file"}

    # указываем кодировку исходных текстовых файлов
    # translate_file(url, params, r"test_utf8.txt", "text/plain; charset=utf-8")
    # translate_file(url, params, r"test_1251.txt", "text/plain; charset=windows-1251")
    # translate_file(url, params, r"test_866.txt",  "text/plain; charset=866")

    # ---------------------------------------------------------
    url = "https://fasttranslator.herokuapp.com/api/v1.0/file/to/text"
    # ответ будет возвращен как json с переводом
    # params = {"lang":"en-uk", "as":"json"}
    # filepath = r"test.docx"
    # mimetype = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    # для docx кодировка не требуется
    # translate_file(url, params, filepath, mimetype)

    # перевод текста
    # ------------------------------------------------------------
    text = '''Однажды, в студеную зимнюю пору,
Я из лесу вышел; был сильный мороз.
Гляжу, поднимается медленно в гору
Лошадка, везущая хворосту воз.'''
    url = "https://fasttranslator.herokuapp.com/api/v1.0/text/to/text"
    params = {"lang": "ru-en", "as": "json", "source": text}
    # в online repl можно запускать только это
    translate_text(url, params)


if __name__ == "__main__":
    main()
