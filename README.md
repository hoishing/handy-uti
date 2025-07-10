# Handy Utilities with Streamlit

> Handy Utilities For Daily Life Hacks

## Utilities

| Feature | Description | Screenshot |
| --- | --- | :---: |
| YouTube Transcriber | Extract captions if available, transcribe the audio with AI otherwise | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/yt_transcriber.webp) |
| Token Counter | Count tokens used in a text for different LLM models | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/token_counter.webp) |
| Mistral OCR | Turn PDF or Image to Markdown with Mistral AI OCR | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/mistral_ocr.webp) |
| MD to EPUB | Convert markdown with images to epub | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/md2epub.webp) |
| Direct Link | Get direct link of Google Drive or Github file | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/direct_link.webp) |
| APNs Tester | Test Apple Push Notification With Ease | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/apn_tester.webp) |
| Remove DRM | Remove DRM of Your Own Ebook from Adobe Digital Edition | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/rm_drm.webp) |
| Groq Models | List all currently active and available models in Groq | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/groq_models.webp) |
| PyPI Name Checker | Check the availability of PyPi package names | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/pypi_name_checker.webp) |
| Astrobro Updater | Update [Astrobro](https://hoishing.github.io/astrobro/) JSON files with city names and country codes | [📷](https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/astrobro_updater.webp) |

## Usage

- Run Directly with `uvx`

```bash
uvx handy-uti

# update with latest version
uvx handy-uti@latest
```

- Install Locally

```bash
uv tool install handy-uti

# then start the streamlit app
handy-uti
```

## API Keys

- api key fields in the app will be auto-filled after providing the `.env` file (optional)

```bash
uvx handy-uti path/to/your/.env
```

- content of `.env` file

```ini
GOOGLE_API_KEY=your-google-api-key
GROQ_API_KEY=your-groq-api-key
MISTRAL_API_KEY=your-mistral-api-key
HUGGINGFACE_API_KEY=your-huggingface-api-key
```

## Questions?

Open a [github issue] or ping me on [LinkedIn]

[github issue]: https://github.com/hoishing/handy-utils/issues
[LinkedIn]: https://www.linkedin.com/in/kng2
