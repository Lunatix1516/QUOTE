import flet as ft

def main(page: ft.Page):
    page.title = "Quote Translator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Quotes + source + origin
    quotes = {
        "English": {
            "text": "The only limit to our realization of tomorrow is our doubts of today.",
            "source": "- Franklin D. Roosevelt",
            "origin": "Speech (1940)"
        },
        "Spanish": {
            "text": "El único límite para lograr el mañana son nuestras dudas de hoy.",
            "source": "- Franklin D. Roosevelt",
            "origin": "Discurso (1940)"
        },
        "French": {
            "text": "La seule limite à notre réalisation de demain est nos doutes d'aujourd'hui.",
            "source": "- Franklin D. Roosevelt",
            "origin": "Discours (1940)"
        }
    }

    # Default language
    selected_language = "English"

    # Quote text
    quote_text = ft.Text(
        value=quotes[selected_language]["text"],
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    # Author
    source_text = ft.Text(
        value=quotes[selected_language]["source"],
        size=16,
        italic=True
    )

    # Origin (NEW)
    origin_text = ft.Text(
        value=quotes[selected_language]["origin"],
        size=14,
        color="grey"
    )

    # Change language function
    def change_language(e):
        lang = e.control.value
        quote_text.value = quotes[lang]["text"]
        source_text.value = quotes[lang]["source"]
        origin_text.value = quotes[lang]["origin"]
        page.update()

    # Radio buttons
    radio_group = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="English", label="English"),
            ft.Radio(value="Spanish", label="Spanish"),
            ft.Radio(value="French", label="French"),
        ]),
        value="English",
        on_change=change_language
    )

    # Layout
    page.add(
        ft.Text("Quote Translator", size=30, weight="bold"),
        ft.Container(height=20),
        quote_text,
        source_text,
        origin_text,  # shows origin here
        ft.Container(height=20),
        radio_group
    )

ft.app(target=main)