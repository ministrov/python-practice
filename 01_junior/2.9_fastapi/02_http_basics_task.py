# -*- coding: utf-8 -*-
"""
Блок 2.9, тема 1: HTTP-основы — практика
════════════════════════════════════════════════════════════════════════
Домен — books (книжная полка), тот же принцип, что items в демо
(01_http_basics_demo.py), но свой класс и свои методы — не копировать
из демо, писать самостоятельно по аналогии.

Задания 1-6: реализовать методы BooksHandler.
Задания 7-8: написать сценарий реальных запросов к серверу.
Задания 9-10: письменные ответы (без кода).

Решение — прямо в этом файле, на месте `# YOUR CODE HERE`. Коммит —
после каждого решённого задания.
"""

import http.client
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

books: dict[int, dict[str, str]] = {}
next_id = 1

print(http.client)


class BooksHandler(BaseHTTPRequestHandler):
    """Обработчик HTTP-запросов для пути /books и /books/<id>."""

    def _send_json(self, status: int, payload: object | None) -> None:
        body = b"" if payload is None else json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _read_json_body(self) -> dict[str, str]:
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        return json.loads(raw)

    def _parse_book_id(self) -> int | None:
        parts = self.path.strip("/").split("/")
        if len(parts) != 2:
            return None
        try:
            return int(parts[1])
        except ValueError:
            return None

    # Задание 1.
    # Реализуй do_GET:
    #   - если self.path == "/books" — верни весь словарь books,
    #     статус 200 (через self._send_json)
    #   - иначе распарси id через self._parse_book_id(); если книга
    #     с таким id есть в books — верни её, статус 200
    #   - если книги нет (или id не распарсился) — верни
    #     {"detail": "Not Found"}, статус 404

    def do_GET(self) -> None:
        if self.path == "/books":
            self._send_json(200, books)
            return
        book_id = self._parse_book_id()
        if book_id is not None and book_id in books:
            self._send_json(200, books[book_id])
            return
        self._send_json(404, {"detail": "Not Found"})
     # do_GET вызывается сервером САМ, когда пришёл GET-запрос — см.
        # объяснение диспетчеризации по do_<МЕТОД> в комментарии над классом.
        # def do_GET(self) -> None:
        #     if self.path == "/items":
        #         # Клиент попросил всю коллекцию целиком — отдаём словарь как есть.
        #         self._send_json(200, items)
        #         return
        #     # Иначе пробуем достать id из пути вида "/items/<id>".
        #     item_id = self._parse_item_id()
        #     if item_id is not None and item_id in items:
        #         # id распарсился И такая запись есть — отдаём именно её.
        #         self._send_json(200, items[item_id])
        #         return
        #     # Либо id не распарсился, либо записи с таким id нет — оба случая 404.
        #     self._send_json(404, {"detail": "Not Found"})

    # Задание 2.
    # Реализуй do_POST:
    #   - если self.path != "/books" — верни 404 {"detail": "Not Found"}
    #   - иначе прочитай тело через self._read_json_body(), сохрани
    #     новую книгу в books под ключом next_id (не забудь
    #     global next_id и next_id += 1 после сохранения)
    #   - ответ: статус 201, заголовок Location: /books/<новый id>,
    #     тело — сохранённая книга (send_response/send_header/
    #     end_headers/wfile.write вручную, как в do_POST демо —
    #     _send_json не подходит, потому что нужен доп. заголовок Location)
    def do_POST(self) -> None:
        # YOUR CODE HERE:
        pass

    # Задание 3.
    # Реализуй do_PUT — полная замена книги:
    #   - если id не распарсился или книги с таким id нет — 404
    #   - иначе books[book_id] = self._read_json_body() целиком,
    #     ответ 200 с новой книгой
    def do_PUT(self) -> None:
        # YOUR CODE HERE:
        pass

    # Задание 4.
    # Реализуй do_PATCH — частичное обновление книги:
    #   - если id не распарсился или книги с таким id нет — 404
    #   - иначе books[book_id].update(self._read_json_body()) —
    #     ТОЛЬКО переданные поля, остальные не трогать,
    #     ответ 200 с обновлённой книгой
    def do_PATCH(self) -> None:
        # YOUR CODE HERE:
        pass

    # Задание 5.
    # Реализуй do_DELETE:
    #   - если id не распарсился или книги с таким id нет — 404
    #   - иначе удали книгу из books (del), ответ 204 без тела
    #     (self._send_json(204, None))
    def do_DELETE(self) -> None:
        # YOUR CODE HERE:
        pass

    def log_message(self, format: str, *args: object) -> None:
        pass


# Задание 6.
# Напиши функцию request(method, path, port, body=None) — она должна
# сделать реальный HTTP-запрос к localhost:port (через
# http.client.HTTPConnection), напечатать "МЕТОД ПУТЬ -> статус причина"
# и тело ответа. Смотри request() в 01_http_basics_demo.py как образец
# структуры (conn.request/getresponse/read/json.loads), но НЕ копируй —
# перепиши сама/сам, разобравшись в шагах.
def request(method: str, path: str, port: int, body: dict[str, str] | None = None) -> None:
    # YOUR CODE HERE:
    pass


if __name__ == "__main__":
    server = HTTPServer(("localhost", 0), BooksHandler)
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    # Задание 7.
    # Через request(...) выполни сценарий:
    #   1. POST /books с телом {"title": "Dune", "author": "Herbert"}
    #   2. POST /books с телом {"title": "1984", "author": "Orwell"}
    #   3. GET /books — должны быть видны обе книги
    # YOUR CODE HERE:

    # Задание 8.
    # Продолжи сценарий:
    #   4. PATCH /books/1 с телом {"read": "true"} — только это поле
    #      добавится к первой книге
    #   5. DELETE /books/2 — вторая книга удаляется, статус 204
    #   6. GET /books/2 — теперь 404, книга удалена
    # YOUR CODE HERE:

    server.shutdown()


# Задание 9 (письменно, в комментарии ниже).
# Объясни своими словами: почему DELETE обычно отвечает 204 без тела,
# а не 200 с пустым JSON-объектом? Что означает "нет тела" в терминах
# самого запроса-как-вызова-функции (раздел 0 демо)?
#
# ТВОЙ ОТВЕТ:


# Задание 10 (письменно, в комментарии ниже).
# PUT и PATCH оба "обновляют" сущность и оба часто возвращают 200.
# В чём разница между ними НЕ в коде статуса, а в самой семантике
# запроса — что произойдёт с полями, которые НЕ передали в теле?
#
# ТВОЙ ОТВЕТ:
