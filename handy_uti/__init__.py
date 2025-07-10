from importlib.metadata import version

__version__ = version("handy-uti")


page_metadata = {
    "yt_transcriber": {
        "title": "YouTube Transcriber",
        "color": "red",
        "icon": "youtube_activity",
        "description": "Extract captions if available, transcribe the audio with AI otherwise",
    },
    "token_counter": {
        "title": "Token Counter",
        "color": "violet",
        "icon": "assignment",
        "description": "Count tokens used in a text for different LLM models",
    },
    "mistral_ocr": {
        "title": "Mistral OCR",
        "color": "orange",
        "icon": "scanner",
        "description": "Turn PDF or Image to Markdown with Mistral AI OCR",
    },
    "md2epub": {
        "title": "MD to EPUB",
        "color": "violet",
        "icon": "markdown",
        "description": "Convert markdown with images to epub",
    },
    "direct_link": {
        "title": "Direct Link",
        "color": "blue",
        "icon": "link",
        "description": "Get direct link of Google Drive or Github file",
    },
    "apn_tester": {
        "title": "APNs Tester",
        "color": "blue",
        "icon": "mark_chat_unread",
        "description": "Test Apple Push Notification With Ease",
    },
    "rm_drm": {
        "title": "Remove DRM",
        "color": "orange",
        "icon": "key",
        "description": "Remove DRM of Your Own Ebook from Adobe Digital Edition",
    },
    "groq_models": {
        "title": "Groq Models",
        "color": "orange",
        "icon": "lightbulb",
        "description": "List all currently active and available models in Groq",
    },
    "pypi_name_checker": {
        "title": "PyPI Name Checker",
        "color": "blue",
        "icon": "check_circle",
        "description": "Check the availability of PyPi package names",
    },
    "astrobro_updater": {
        "title": "Astrobro Updater",
        "color": "orange",
        "icon": "planet",
        "description": "Update [Astrobro](https://hoishing.github.io/astrobro/) JSON files with city names and country codes",
    },
}
