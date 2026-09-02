# -*- coding: utf-8 -*-
"""
Блок 2.9, тема 1: HTTP-основы
════════════════════════════════════════════════════════════════════════
До FastAPI — сам протокол, на чистом stdlib (http.server + http.client),
без сторонних библиотек. FastAPI (тема 3) — это просто удобная обёртка
над тем же самым протоколом, который ты увидишь здесь напрямую.

Темы:
  0. Мост: HTTP-запрос ~ вызов функции по сети
  1. Методы: GET/POST/PUT/PATCH/DELETE — семантика
  2. Статус-коды: категории 1xx-5xx
  3. Заголовки: request vs response
  4. Тело запроса/ответа: JSON (json.dumps/loads — уже знакомо из 2.4)
  5. Всё вместе: мини CRUD-сервис "items" + реальные запросы к нему
"""

import http.client
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# ════════════════════════════════════════════════════════════════════════
# 0. Мост: HTTP-запрос ~ вызов функции по сети
# ════════════════════════════════════════════════════════════════════════
# Ты уже писал функции вида:
#
#     def create_ticket(id: int, title: str, priority: str) -> Ticket:
#         ...
#
# Вызов функции — это: "имя" + "аргументы" → "возвращаемое значение".
# HTTP-запрос устроен ровно так же, просто через сеть, а не в памяти
# одного процесса:
#
#     функция                        HTTP-запрос
#     ────────────────────────────   ────────────────────────────────
#     имя функции                    метод + путь (POST /items)
#     аргументы                      заголовки + тело запроса
#     return значение                статус-код + тело ответа
#     raise ValueError(...)          статус-код 4xx/5xx + тело с ошибкой
#
# Клиент "вызывает" сервер через сеть, сервер выполняет код и "возвращает"
# результат — с одной разницей: вызов может физически не дойти (сеть
# упала), поэтому у HTTP есть отдельная категория кодов для "запрос не
# дошёл или сервер сломался" (5xx) в отличие от "дошёл, но данные
# неправильные" (4xx) — это разделение будет важно в теме 5
# (обработка ошибок).


# ════════════════════════════════════════════════════════════════════════
# 1. Методы: GET/POST/PUT/PATCH/DELETE — семантика
# ════════════════════════════════════════════════════════════════════════
# GET     — прочитать данные, ничего не меняя (аналог обращения к
#           словарю по ключу: `items[1]`, без побочных эффектов)
# POST    — создать новую сущность (аналог `items.append(x)` — каждый
#           вызов добавляет ЕЩЁ ОДНУ запись, даже с теми же данными)
# PUT     — заменить сущность ЦЕЛИКОМ (аналог `items[1] = new_item` —
#           старые поля, которых нет в новом объекте, теряются)
# PATCH   — обновить сущность ЧАСТИЧНО (аналог `items[1].update(...)`
#           или смены одного поля dataclass — остальные поля не трогает)
# DELETE  — удалить сущность (аналог `del items[1]`)
#
# Один и тот же путь ("/items/1") ведёт себя по-разному в зависимости
# ИМЕННО от метода — путь описывает "какая сущность", метод — "что с
# ней сделать".


# ════════════════════════════════════════════════════════════════════════
# 2. Статус-коды: категории 1xx-5xx
# ════════════════════════════════════════════════════════════════════════
# 1xx — информационные (встречаются редко, пропускаем)
# 2xx — успех:
#       200 OK              — успех, есть тело ответа (GET/PUT/PATCH)
#       201 Created         — успех, создана новая сущность (POST)
#       204 No Content      — успех, тела ответа НЕТ (DELETE)
# 3xx — редирект (например 301 — ресурс переехал на другой URL)
# 4xx — ошибка НА СТОРОНЕ КЛИЕНТА (запрос дошёл, но он неправильный):
#       400 Bad Request     — некорректные данные в теле запроса
#       404 Not Found       — такой сущности/пути не существует
#       422 Unprocessable   — данные не прошли валидацию (Pydantic,
#                             тема 4, будет отдавать именно этот код)
# 5xx — ошибка НА СТОРОНЕ СЕРВЕРА (сервер сломался при обработке):
#       500 Internal Server Error — необработанное исключение в коде
#
# Параллель с исключениями (блок 2.7): 4xx ~ ValueError (клиент передал
# то, чего не должен был), 5xx ~ необработанный баг в самом сервере.


# ════════════════════════════════════════════════════════════════════════
# 3. Заголовки: request vs response
# ════════════════════════════════════════════════════════════════════════
# Заголовки — это просто пары ключ-значение (как dict), которые едут
# ОТДЕЛЬНО от тела, с метаданными о запросе/ответе.
#
# В запросе (клиент → сервер), например:
#   Content-Type: application/json   — "тело запроса в формате JSON"
#   Authorization: Bearer <token>    — "вот кто я" (тема 2.9.5, DI)
#
# В ответе (сервер → клиент), например:
#   Content-Type: application/json   — "тело ответа в формате JSON"
#   Content-Length: 42               — размер тела в байтах
#   Location: /items/1               — где искать только что созданную
#                                       сущность (обычно вместе с 201)


# ════════════════════════════════════════════════════════════════════════
# 4. Тело запроса/ответа: JSON
# ════════════════════════════════════════════════════════════════════════
# json.dumps()/json.loads() ты уже использовал в блоке 2.4
# (16_io_and_files). Здесь то же самое, просто тело едет не в файл,
# а по сети: json.dumps(dict) → bytes → в тело запроса/ответа,
# и обратно json.loads(bytes) на другом конце.


# ════════════════════════════════════════════════════════════════════════
# 5. Всё вместе: мини CRUD-сервис "items" + реальные запросы
# ════════════════════════════════════════════════════════════════════════
# "База данных" — обычный словарь в памяти процесса (никакого
# SQLAlchemy — это чистый протокол, БД подключим в теме 6).
#
# Как это работает "под капотом" (stdlib-магия, на которой стоит
# HTTPServer): ты даёшь HTTPServer класс-наследник BaseHTTPRequestHandler.
# На КАЖДЫЙ входящий запрос сервер сам создаёт экземпляр этого класса и
# сам вызывает метод с именем do_<HTTP-МЕТОД> — do_GET, do_POST и т.д.
# Диспетчеризация "какой метод дернуть" уже сделана базовым классом по
# имени HTTP-метода запроса — поэтому здесь нет ручного
# `if method == "GET": ...`.
#
# Внутри каждого do_* метода `self` — это как раз этот экземпляр-на-один-
# запрос, и у него уже готовы (заполнены базовым классом ДО вызова do_*):
#   self.path    — путь запроса, например "/items/1"
#   self.headers — заголовки запроса
#   self.rfile   — поток ЧТЕНИЯ тела запроса (как открытый файл)
#   self.wfile   — поток ЗАПИСИ тела ответа (как открытый файл)

items: dict[int, dict[str, str]] = {}
next_id = 1


class ItemsHandler(BaseHTTPRequestHandler):
    """Обработчик HTTP-запросов для пути /items и /items/<id>."""

    # Три приватных метода ниже (префикс "_" = внутреннее, не часть
    # API do_*) — вынесенное наружу дублирование, которое иначе
    # повторялось бы в каждом do_GET/do_POST/... по отдельности.

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

    def _parse_item_id(self) -> int | None:
        parts = self.path.strip("/").split("/")
        if len(parts) != 2:
            return None
        try:
            return int(parts[1])
        except ValueError:
            return None

    # do_GET вызывается сервером САМ, когда пришёл GET-запрос — см.
    # объяснение диспетчеризации по do_<МЕТОД> в комментарии над классом.
    def do_GET(self) -> None:
        if self.path == "/items":
            self._send_json(200, items)
            return
        item_id = self._parse_item_id()
        if item_id is not None and item_id in items:
            self._send_json(200, items[item_id])
            return
        self._send_json(404, {"detail": "Not Found"})

    # Ответ собран вручную (send_response/send_header/end_headers/
    # wfile.write), а не через _send_json — потому что нужен ДОПОЛНИТЕЛЬНЫЙ
    # заголовок Location, которого у _send_json нет.
    def do_POST(self) -> None:
        global next_id
        if self.path != "/items":
            self._send_json(404, {"detail": "Not Found"})
            return
        data = self._read_json_body()
        items[next_id] = data
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.send_header("Location", f"/items/{next_id}")
        body = json.dumps(data).encode("utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        next_id += 1

    def do_PUT(self) -> None:
        item_id = self._parse_item_id()
        if item_id is None or item_id not in items:
            self._send_json(404, {"detail": "Not Found"})
            return
        items[item_id] = self._read_json_body()
        self._send_json(200, items[item_id])

    def do_PATCH(self) -> None:
        item_id = self._parse_item_id()
        if item_id is None or item_id not in items:
            self._send_json(404, {"detail": "Not Found"})
            return
        items[item_id].update(self._read_json_body())
        self._send_json(200, items[item_id])

    def do_DELETE(self) -> None:
        item_id = self._parse_item_id()
        if item_id is None or item_id not in items:
            self._send_json(404, {"detail": "Not Found"})
            return
        del items[item_id]
        self._send_json(204, None)

    def log_message(self, format: str, *args: object) -> None:
        pass  # отключаем стандартный лог сервера, чтобы не мешал выводу демо


def request(method: str, path: str, port: int, body: dict[str, str] | None = None) -> None:
    """Отправить реальный HTTP-запрос к локальному серверу и напечатать ответ."""
    conn = http.client.HTTPConnection("localhost", port)
    headers = {"Content-Type": "application/json"} if body is not None else {}
    data = json.dumps(body).encode("utf-8") if body is not None else None
    conn.request(method, path, body=data, headers=headers)
    resp = conn.getresponse()
    raw = resp.read()
    parsed = json.loads(raw) if raw else None
    print(f"{method} {path} -> {resp.status} {resp.reason}")
    print(f"  Content-Type: {resp.getheader('Content-Type')}", end="")
    location = resp.getheader("Location")
    if location:
        print(f", Location: {location}", end="")
    print()
    print(f"  body: {parsed}")
    conn.close()


if __name__ == "__main__":
    # port=0 — просим ОС саму выдать свободный порт (чтобы не ловить
    # "порт занят"); реальный порт потом читаем из server.server_port.
    server = HTTPServer(("localhost", 0), ItemsHandler)
    port = server.server_port
    # server.serve_forever() — бесконечный цикл (как while True), он
    # БЛОКИРУЕТ поток, в котором выполняется. Без отдельного потока
    # код ниже (все request(...)) никогда бы не запустился — программа
    # зависла бы на serve_forever(). daemon=True — поток умрёт вместе
    # с основной программой сам, вручную останавливать не нужно.
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    request("GET", "/items", port)                                    # 200, пусто
    request("POST", "/items", port, {"title": "Buy milk"})             # 201
    request("GET", "/items/1", port)                                   # 200
    request("PUT", "/items/1", port, {"title": "Buy milk and bread"})  # 200, замена целиком
    request("PATCH", "/items/1", port, {"done": "false"})              # 200, добавили поле
    request("DELETE", "/items/1", port)                                # 204, без тела
    request("GET", "/items/1", port)                                   # 404, уже удалено
    request("GET", "/nope", port)                                      # 404, неизвестный путь

    server.shutdown()
